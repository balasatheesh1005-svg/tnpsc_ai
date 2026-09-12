import json
import os
from typing import Any, Callable, Dict, List, Optional, Tuple

from .topic_resolver import ResolvedTopic
from .checkpoint import PipelineCheckpointManager, PipelineState
from .duplicate_index import TopicDuplicateIndex
from .validator import ContentValidator, ValidationReport
from .blueprint_manager import BlueprintManager
from .discovery import TopicDiscovery, CATEGORY_FILES


PART_CATEGORIES = {
    "part1": [
        ("easy", 50, [25, 25]),
        ("medium", 50, [25, 25]),
        ("hard", 50, [25, 25]),
    ],
    "part2a": [
        ("statement_based", 50, [25, 25]),
        ("pyq", 50, [25, 25]),
    ],
    "part2b": [
        ("reasoning", 25, [25]),
        ("match_the_following", 25, [25]),
        ("chronology", 25, [25]),
    ],
    "part3": [
        ("grand_test", 100, [25, 25, 25, 25]),
    ]
}


class GeneratorRunner:
    """
    Orchestrates batch generation, duplicate checking, immediate validation,
    targeted repair, checkpointing, and resume logic.
    """

    def __init__(self, topic: ResolvedTopic):
        self.topic = topic
        self.ckpt_mgr = PipelineCheckpointManager(topic.topic_id, topic.display_title)
        self.dup_index = TopicDuplicateIndex(topic.topic_id)
        self.blueprint = BlueprintManager.load_or_build(topic)
        self._load_existing_into_index()

    def _load_existing_into_index(self) -> None:
        subj = self.topic.subject
        base = self.topic.base_name
        q_dir = f"data/questions/{subj}"
        paths = []
        for cat, fname_tpl, _, _ in CATEGORY_FILES:
            fp = os.path.join(q_dir, fname_tpl.format(base=base))
            if os.path.exists(fp):
                paths.append(fp)
        self.dup_index.load_from_files(paths)

    def is_part_complete(self, part_key: str) -> Tuple[bool, str]:
        """
        Idempotency check:
        Returns (is_complete, message).
        """
        subj = self.topic.subject
        base = self.topic.base_name
        pfx = self.topic.id_prefix
        q_dir = f"data/questions/{subj}"

        spec_list = PART_CATEGORIES.get(part_key, [])
        all_present = True
        total_count = 0

        for cat, exp_count, _ in spec_list:
            fname = f"{base}_{cat}.json"
            fpath = os.path.join(q_dir, fname)
            if not os.path.exists(fpath):
                all_present = False
                break
            rep = ContentValidator.validate_file(fpath, expected_count=exp_count, expected_prefix=f"{pfx}_")
            if not rep.is_valid:
                all_present = False
                break
            total_count += rep.total_audited

        if all_present and total_count > 0:
            return True, f"{part_key.upper()}_ALREADY_COMPLETE ({total_count} questions valid)"
        return False, ""

    def preflight_check(self, part_key: str) -> Tuple[bool, str]:
        """Preflight check before running a part."""
        if part_key == "part3":
            # Grand Test Gate: Core must be 325 and valid
            core_complete = True
            for pk in ["part1", "part2a", "part2b"]:
                is_comp, _ = self.is_part_complete(pk)
                if not is_comp:
                    core_complete = False
                    break
            if not core_complete:
                return False, "Grand Test Gate Error: Core 325 questions must be complete and valid before Part 3 can start."
        return True, "Preflight checks passed"

    def execute_dry_run(self, part_key: str) -> Dict[str, Any]:
        """Performs a safe dry run without generating any MCQs."""
        print(f"[NOVA] Performing safe dry run for {part_key.upper()} on '{self.topic.display_title}'...")
        is_complete, comp_msg = self.is_part_complete(part_key)
        can_proceed, preflight_msg = self.preflight_check(part_key)

        status = {
            "part": part_key,
            "topic": self.topic.display_title,
            "topic_id": self.topic.topic_id,
            "is_already_complete": is_complete,
            "completion_message": comp_msg,
            "preflight_allowed": can_proceed,
            "preflight_message": preflight_msg,
            "duplicate_index_count": self.dup_index.count(),
            "blueprint_loaded": bool(self.blueprint),
            "dry_run_success": True
        }
        print(f"[NOVA] Dry run completed: {status}")
        return status
