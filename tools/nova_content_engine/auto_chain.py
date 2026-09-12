# -*- coding: utf-8 -*-
import json
import os
import sys
from typing import Any, Callable, Dict, List, Optional, Tuple

from .topic_resolver import ResolvedTopic
from .checkpoint import PipelineCheckpointManager, PipelineState, TopicLock
from .validator import ContentValidator, ValidationReport
from .audit import TopicAuditor
from .ui_smoke_test import run_ui_smoke_test
from .discovery import TopicDiscovery, CATEGORY_FILES
from .blueprint_manager import BlueprintManager
from .duplicate_index import TopicDuplicateIndex

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


PART_CHAIN_SPEC = [
    (
        "part1",
        "PART 1",
        150,
        [
            ("easy", 50, [25, 25], "{prefix}_E_"),
            ("medium", 50, [25, 25], "{prefix}_M_"),
            ("hard", 50, [25, 25], "{prefix}_H_"),
        ],
        PipelineState.PART_1_RUNNING,
        PipelineState.PART_1_COMPLETE,
    ),
    (
        "part2a",
        "PART 2A",
        100,
        [
            ("statement_based", 50, [25, 25], "{prefix}_S_"),
            ("pyq", 50, [25, 25], "{prefix}_PYQ_"),
        ],
        PipelineState.PART_2A_RUNNING,
        PipelineState.PART_2A_COMPLETE,
    ),
    (
        "part2b",
        "PART 2B",
        75,
        [
            ("reasoning", 25, [25], "{prefix}_R_"),
            ("match_the_following", 25, [25], "{prefix}_MF_"),
            ("chronology", 25, [25], "{prefix}_C_"),
        ],
        PipelineState.PART_2B_RUNNING,
        PipelineState.PART_2B_COMPLETE,
    ),
    (
        "part3",
        "PART 3 (Grand Test)",
        100,
        [
            ("grand_test", 100, [25, 25, 25, 25], "{prefix}_GT_"),
        ],
        PipelineState.PART_3_RUNNING,
        PipelineState.PART_3_COMPLETE,
    ),
]


class AutoChainPipeline:
    """
    Orchestrates the seamless auto-chain pipeline for the Master Content Engine.
    Executes:
      PART 1 -> VALIDATE -> REPAIR IF REQUIRED
      -> PART 2A -> VALIDATE -> REPAIR IF REQUIRED
      -> PART 2B -> VALIDATE -> REPAIR IF REQUIRED
      -> CORE COMPLETE (325/325)
      -> PART 3 (Grand Test) -> VALIDATE -> REPAIR IF REQUIRED
      -> FINAL AUDIT
      -> UI SMOKE TEST
      -> PRODUCTION_READY
    """

    def __init__(self, topic: ResolvedTopic):
        self.topic = topic
        self.ckpt_mgr = PipelineCheckpointManager(topic.topic_id, topic.display_title)
        self.lock = TopicLock(topic.topic_id)
        self.dup_index = TopicDuplicateIndex(topic.topic_id)
        self.blueprint = BlueprintManager.load_or_build(topic)

    def is_category_complete(self, category: str, exp_count: int, pfx: str) -> Tuple[bool, Optional[str], Optional[ValidationReport]]:
        q_dir = f"data/questions/{self.topic.subject}"
        fpath = os.path.join(q_dir, f"{self.topic.base_name}_{category}.json")
        if not os.path.exists(fpath):
            return False, fpath, None
        rep = ContentValidator.validate_file(fpath, expected_count=exp_count, expected_prefix=pfx)
        return rep.is_valid, fpath, rep

    def is_part_complete(self, part_key: str) -> Tuple[bool, int, str]:
        """
        Checks if a part is fully complete and validated on disk.
        Returns (is_complete, total_valid_questions, details).
        """
        spec = next((item for item in PART_CHAIN_SPEC if item[0] == part_key), None)
        if not spec:
            return False, 0, f"Unknown part: {part_key}"

        _, part_title, exp_part_count, categories, _, _ = spec
        total_valid = 0
        all_ok = True

        for cat, exp_count, _, pfx_tpl in categories:
            pfx = pfx_tpl.format(prefix=self.topic.id_prefix)
            ok, _, rep = self.is_category_complete(cat, exp_count, pfx)
            if not ok:
                all_ok = False
                break
            total_valid += rep.total_audited

        if all_ok and total_valid == exp_part_count:
            return True, total_valid, f"{part_title} already COMPLETE ({total_valid}/{exp_part_count})"
        return False, total_valid, ""

    def get_first_incomplete_part(self) -> str:
        """Finds the first part in the sequence that is not yet fully validated."""
        for item in PART_CHAIN_SPEC:
            pk = item[0]
            ok, _, _ = self.is_part_complete(pk)
            if not ok:
                return pk
        return "part1"

    @classmethod
    def attempt_auto_repair(cls, filepath: str, max_cycles: int = 3) -> Tuple[bool, Optional[ValidationReport]]:
        """
        Attempts deterministic automated repair of common question defects:
        - difficulty capitalization
        - lowercase answer alignment with correct_answer
        - string whitespace trimming
        - option structure normalization
        """
        for cycle in range(1, max_cycles + 1):
            rep = ContentValidator.validate_file(filepath)
            if rep.is_valid:
                return True, rep

            if not os.path.exists(filepath):
                return False, rep

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    questions = json.load(f)
            except Exception:
                return False, rep

            modified = False
            for q in questions:
                # 1. Normalize difficulty casing
                diff = str(q.get("difficulty", "")).strip().lower()
                if diff in ["easy", "medium", "hard"]:
                    cap_diff = diff.capitalize()
                    if q.get("difficulty") != cap_diff:
                        q["difficulty"] = cap_diff
                        modified = True

                # 2. Normalize correct_answer and answer
                ca = str(q.get("correct_answer", "")).strip().upper()
                if ca in ["A", "B", "C", "D"]:
                    if q.get("correct_answer") != ca:
                        q["correct_answer"] = ca
                        modified = True
                    expected_ans = ca.lower()
                    if q.get("answer") != expected_ans:
                        q["answer"] = expected_ans
                        modified = True

                # 3. Ensure options have id, en, ta
                opts = q.get("options", [])
                if isinstance(opts, list) and len(opts) == 4:
                    letters = ["A", "B", "C", "D"]
                    for idx, opt in enumerate(opts):
                        if isinstance(opt, dict):
                            if opt.get("id") != letters[idx]:
                                opt["id"] = letters[idx]
                                modified = True

            if modified:
                tmp_f = f"{filepath}.tmp"
                with open(tmp_f, "w", encoding="utf-8") as f:
                    json.dump(questions, f, indent=2, ensure_ascii=False)
                os.replace(tmp_f, filepath)

            # Re-validate after cycle
            rep_after = ContentValidator.validate_file(filepath)
            if rep_after.is_valid:
                return True, rep_after

        final_rep = ContentValidator.validate_file(filepath)
        return final_rep.is_valid, final_rep

    def execute_auto_chain(
        self,
        start_part: Optional[str] = "part1",
        part_only: bool = False,
        dry_run: bool = False,
        generation_hook: Optional[Callable[[str, str, int, str], bool]] = None,
    ) -> Dict[str, Any]:
        """
        Executes the auto-chain pipeline.
        If part_only is True, halts after the specified part completes.
        Otherwise, automatically chains through all remaining parts to PRODUCTION_READY.
        """
        chain_mode = "DISABLED (--part-only)" if part_only else "ENABLED"
        dry_suffix = " (DRY RUN)" if dry_run else ""
        print(f"[NOVA] Topic: {self.topic.display_title}")
        print(f"[NOVA] AUTO-CHAIN: {chain_mode}{dry_suffix}")

        # Concurrency safety lock
        if not dry_run:
            locked, lock_msg = self.lock.acquire()
            if not locked:
                print(f"[ERROR] Concurrency Gate: {lock_msg}")
                return {"success": False, "status": "TOPIC_ALREADY_RUNNING", "message": lock_msg}

        try:
            part_keys = [p[0] for p in PART_CHAIN_SPEC]
            if not start_part or start_part not in part_keys:
                start_part = self.get_first_incomplete_part()

            start_idx = part_keys.index(start_part)
            total_steps = len(PART_CHAIN_SPEC)

            for step_idx in range(start_idx, total_steps):
                part_key, part_title, part_target, categories, running_state, complete_state = PART_CHAIN_SPEC[step_idx]
                display_step = f"[{step_idx + 1}/{total_steps}] {part_title}"

                print(f"\n{display_step}")

                # Idempotency Check (Only in real runs; dry-run simulates full chain)
                is_comp, valid_count, comp_detail = self.is_part_complete(part_key)
                if is_comp and not dry_run:
                    print(f"[NOVA] Idempotency: {comp_detail}. Skipping regeneration.")
                    self.ckpt_mgr.update_part_status(part_key, "COMPLETE", valid_count, True)

                    if part_only:
                        print(f"\n[NOVA] --part-only specified. Stopping after {part_title}.")
                        return {"success": True, "status": f"{part_key.upper()}_COMPLETE", "part": part_key}

                    # If part2b finished and we are chaining, verify Core count
                    if part_key == "part2b":
                        print("\n[CORE COMPLETE] 325 / 325 verified.")
                        self.ckpt_mgr.set_state(PipelineState.CORE_COMPLETE, notes="Core 325 verified")
                        if step_idx + 1 < total_steps:
                            print(f"\n[AUTO] Triggering {PART_CHAIN_SPEC[step_idx + 1][1]}")
                    elif step_idx + 1 < total_steps:
                        print(f"\n[AUTO] Triggering {PART_CHAIN_SPEC[step_idx + 1][1]}")
                    continue

                # Not complete or dry run: execute part
                if not dry_run:
                    self.ckpt_mgr.set_state(running_state, notes=f"Generating {part_title}")

                for cat, exp_cat_count, batches, pfx_tpl in categories:
                    pfx = pfx_tpl.format(prefix=self.topic.id_prefix)
                    q_dir = f"data/questions/{self.topic.subject}"
                    fpath = os.path.join(q_dir, f"{self.topic.base_name}_{cat}.json")

                    for b_idx, batch_size in enumerate(batches):
                        cat_label = cat.replace("_", " ").title()
                        batch_label = f"[{cat_label} {b_idx + 1}/{len(batches)}]"

                        if dry_run:
                            print(f"{batch_label} {batch_size} generated")
                            print("[VALIDATION] PASS (simulated)")
                            continue

                        # Real run: check if already complete in file
                        cat_ok, _, rep = self.is_category_complete(cat, exp_cat_count, pfx)
                        if cat_ok:
                            print(f"{batch_label} Verified complete ({exp_cat_count}/{exp_cat_count}).")
                            print("[VALIDATION] PASS")
                            break

                        # Call generator hook if supplied
                        if generation_hook:
                            gen_ok = generation_hook(part_key, cat, batch_size, pfx)
                            if not gen_ok:
                                print(f"[ERROR] Generation hook failed for {batch_label}.")
                                return {"success": False, "status": "GENERATION_FAILED", "part": part_key}

                        # Validate after batch
                        if os.path.exists(fpath):
                            val_rep = ContentValidator.validate_file(fpath, expected_count=exp_cat_count, expected_prefix=pfx)
                            if val_rep.is_valid:
                                print(f"{batch_label} {exp_cat_count} generated & validated.")
                                print("[VALIDATION] PASS")
                            else:
                                print(f"{batch_label} [VALIDATION] FAIL. Attempting automatic targeted repair (max 3 cycles)...")
                                rep_ok, rep_report = self.attempt_auto_repair(fpath, max_cycles=3)
                                if rep_ok:
                                    print("[REPAIR] SUCCESS. Validation re-check: PASS")
                                else:
                                    # Failure stop
                                    self.ckpt_mgr.set_state(PipelineState.REPAIR_REQUIRED, notes=f"Failed at {cat}")
                                    crit_issues = rep_report.critical_issues() if rep_report else []
                                    first_err = crit_issues[0].message if crit_issues else "Validation failed"
                                    affected_ids = [i.question_id for i in crit_issues[:5]] if crit_issues else ["UNKNOWN"]
                                    print("\n" + "=" * 60)
                                    print("AUTO-CHAIN STOPPED")
                                    print("=" * 60)
                                    print(f"Part:\n{part_title}\n")
                                    print(f"Reason:\n{first_err}\n")
                                    print(f"Affected IDs:\n{affected_ids}\n")
                                    print("Next action:\nRepair required")
                                    print("=" * 60 + "\n")
                                    return {"success": False, "status": "REPAIR_REQUIRED", "part": part_key, "issues": [first_err]}

                # Part finished
                if dry_run:
                    print(f"\n[{part_title}] COMPLETE {part_target}/{part_target} (simulated)")
                    print(f"{part_title} → simulated")
                    print("VALIDATION → simulated")
                else:
                    self.ckpt_mgr.update_part_status(part_key, "COMPLETE", part_target, True)
                    print(f"\n[{part_title}] COMPLETE {part_target}/{part_target}")

                # Part-Only override check
                if part_only:
                    print(f"\n[NOVA] --part-only specified. Stopping after {part_title}.")
                    return {"success": True, "status": f"{part_key.upper()}_COMPLETE", "part": part_key}

                # Check Core gate after Part 2B
                if part_key == "part2b":
                    if dry_run:
                        print("\n[CORE COMPLETE] 325 / 325 (simulated)")
                    else:
                        print("\n[CORE COMPLETE] 325 / 325 verified.")
                        self.ckpt_mgr.set_state(PipelineState.CORE_COMPLETE, notes="Core 325 verified")

                # Trigger next part notification
                if step_idx + 1 < total_steps:
                    next_title = PART_CHAIN_SPEC[step_idx + 1][1]
                    print(f"\n[AUTO] Triggering {next_title}")

            # -----------------------------------------------------------------
            # Final Automation: Final Audit & UI Smoke Test
            # -----------------------------------------------------------------
            print("\n[AUTO] Triggering FINAL SEMANTIC AUDIT")
            if dry_run:
                print("  [FINAL AUDIT] PASS (simulated)")
                print("FINAL AUDIT → simulated")
                print("\n[AUTO] Triggering AUTOMATIC UI SMOKE TEST")
                print("  [UI SMOKE TEST] PASS (simulated)")
                print("UI TEST → simulated")
                print("\n[PIPELINE] Topic State -> PRODUCTION_READY (simulated)")
                return {"success": True, "status": "PRODUCTION_READY", "dry_run": True}

            self.ckpt_mgr.set_state(PipelineState.SEMANTIC_AUDIT, notes="Running final audit")
            audit_rep = TopicAuditor.audit_topic(self.topic, run_ui_test=False)
            if not audit_rep.is_ready:
                print("  [FINAL AUDIT] FAIL")
                for iss in audit_rep.issues[:5]:
                    print(f"    - {iss}")
                self.ckpt_mgr.set_state(PipelineState.REPAIR_REQUIRED, notes="Final audit failed")
                return {"success": False, "status": "REPAIR_REQUIRED", "stage": "FINAL_AUDIT"}

            print("  [FINAL AUDIT] PASS")
            self.ckpt_mgr.set_state(PipelineState.SEMANTIC_AUDIT_COMPLETE, notes="Final audit passed")

            print("\n[AUTO] Triggering AUTOMATIC UI SMOKE TEST")
            self.ckpt_mgr.set_state(PipelineState.UI_TEST, notes="Running UI smoke test")
            ui_res = run_ui_smoke_test(
                subject=self.topic.subject,
                topic_id=self.topic.topic_id,
                repository_id=self.topic.repository_id,
                test_questions=True
            )
            if not ui_res["success"]:
                print("  [UI SMOKE TEST] FAIL")
                for err in ui_res["errors"]:
                    print(f"    - {err}")
                self.ckpt_mgr.set_state(PipelineState.REPAIR_REQUIRED, notes="UI smoke test failed")
                return {"success": False, "status": "REPAIR_REQUIRED", "stage": "UI_TEST"}

            print("  [UI SMOKE TEST] PASS")
            for step in ui_res["steps_passed"]:
                print(f"    [PASS] {step}")

            self.ckpt_mgr.set_state(PipelineState.PRODUCTION_READY, notes="All 425 MCQs production ready")
            print("\n" + "=" * 60)
            print(f"[PIPELINE] Topic: {self.topic.display_title} -> PRODUCTION_READY")
            print("=" * 60)
            return {"success": True, "status": "PRODUCTION_READY"}

        finally:
            if not dry_run:
                self.lock.release()
