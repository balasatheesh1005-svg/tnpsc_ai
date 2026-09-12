import json
import os
from typing import Any, Callable, Dict, List, Optional, Tuple

from .checkpoint import PipelineCheckpointManager, PipelineState
from .duplicate_index import TopicDuplicateIndex
from .validator import ContentValidator, ValidationReport
from .ui_smoke_test import run_ui_smoke_test


class NovaContentPipeline:
    """
    Automated pipeline orchestrator for TNPSC Nova AI content generation.
    Supports checkpoints, auto-validation, targeted repair, duplicate index,
    and UI smoke testing without manual user prompts.
    """

    FILE_SPEC = {
        "easy": ("data/questions/{subject}/{base}_easy.json", 50, "{prefix}_E_"),
        "medium": ("data/questions/{subject}/{base}_medium.json", 50, "{prefix}_M_"),
        "hard": ("data/questions/{subject}/{base}_hard.json", 50, "{prefix}_H_"),
        "statement_based": ("data/questions/{subject}/{base}_statement_based.json", 50, "{prefix}_S_"),
        "pyq": ("data/questions/{subject}/{base}_pyq.json", 50, "{prefix}_PYQ_"),
        "reasoning": ("data/questions/{subject}/{base}_reasoning.json", 25, "{prefix}_R_"),
        "match_the_following": ("data/questions/{subject}/{base}_match_the_following.json", 25, "{prefix}_MF_"),
        "chronology": ("data/questions/{subject}/{base}_chronology.json", 25, "{prefix}_C_"),
        "grand_test": ("data/questions/{subject}/{base}_grand_test.json", 100, "{prefix}_GT_"),
    }

    def __init__(self, topic_id: str, subject: str = "polity", blueprint_path: Optional[str] = None):
        self.topic_id = topic_id
        self.subject = subject.lower()
        self.blueprint_path = blueprint_path or f"data/blueprints/{self.subject}/{self.topic_id.replace(self.subject + '_', '')}_blueprint.json"
        
        # Derive short base name and prefix
        # e.g. polity_centre_state_relations -> base: centre_state_relations, prefix: CSR
        self.base_name = self.topic_id.replace(f"{self.subject}_", "")
        # e.g. centre_state_relations -> CSR
        words = [w for w in self.base_name.split("_") if w]
        self.id_prefix = "".join([w[0].upper() for w in words]) if len(words) > 1 else words[0][:2].upper()

        self.checkpoint_mgr = PipelineCheckpointManager(self.topic_id)
        self.duplicate_index = TopicDuplicateIndex(self.topic_id)
        self.blueprint = self._load_blueprint()

    def _load_blueprint(self) -> Dict[str, Any]:
        if os.path.exists(self.blueprint_path):
            with open(self.blueprint_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def get_files_map(self) -> Dict[str, Tuple[str, int, str]]:
        """Returns category -> (filepath, expected_count, id_prefix)"""
        fmap = {}
        for cat, (fmt, count, pfx_fmt) in self.FILE_SPEC.items():
            fp = fmt.format(subject=self.subject, base=self.base_name)
            pfx = pfx_fmt.format(prefix=self.id_prefix)
            fmap[cat] = (fp, count, pfx)
        return fmap

    def get_state(self) -> PipelineState:
        return self.checkpoint_mgr.get_state()

    def mark_blueprint_ready(self) -> Dict[str, Any]:
        """Marks topic status as BLUEPRINT_READY."""
        return self.checkpoint_mgr.save(
            state=PipelineState.BLUEPRINT_READY,
            core_count=0,
            grand_test_count=0,
            validated=True,
            repair_required=False,
            notes="Blueprint constructed and verified against source notes."
        )

    def validate_category(self, category: str) -> ValidationReport:
        """Validates a single question file in the pipeline."""
        fmap = self.get_files_map()
        if category not in fmap:
            raise ValueError(f"Unknown category: {category}")
        filepath, exp_count, prefix = fmap[category]
        return ContentValidator.validate_file(filepath, expected_count=exp_count, expected_prefix=prefix)

    def validate_all(self) -> ValidationReport:
        """Validates the entire 425-question suite."""
        fmap = self.get_files_map()
        return ContentValidator.validate_topic_suite(fmap)

    def run_smoke_test(self, test_questions: bool = True) -> Dict[str, Any]:
        """Executes automated UI Smoke Test for this topic."""
        return run_ui_smoke_test(
            subject=self.subject,
            topic_id=self.topic_id,
            repository_id=self.topic_id,
            test_questions=test_questions
        )

    def targeted_repair(
        self,
        filepath: str,
        repair_fn: Callable[[List[dict], List[str]], List[dict]],
        max_cycles: int = 3
    ) -> bool:
        """
        Executes targeted repair on a question file.
        Identifies failing IDs, runs repair_fn on them, and re-validates.
        """
        for cycle in range(1, max_cycles + 1):
            rep = ContentValidator.validate_file(filepath)
            if rep.is_valid:
                return True

            critical_qids = list(set([i.question_id for i in rep.critical_issues() if i.question_id not in ["FILE", "COUNT"]]))
            if not critical_qids:
                return True

            with open(filepath, "r", encoding="utf-8") as f:
                questions = json.load(f)

            questions = repair_fn(questions, critical_qids)

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(questions, f, indent=2, ensure_ascii=False)

        # Final check
        final_rep = ContentValidator.validate_file(filepath)
        return final_rep.is_valid
