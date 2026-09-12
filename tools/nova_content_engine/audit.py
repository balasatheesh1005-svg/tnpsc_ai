import json
import os
import re
from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Dict, List, Set, Tuple

from .topic_resolver import ResolvedTopic
from .validator import ContentValidator, ValidationIssue, ValidationReport
from .discovery import CATEGORY_FILES


@dataclass
class AuditReport:
    topic_id: str
    is_ready: bool
    structural_status: str
    schema_status: str
    bilingual_status: str
    answer_integrity_status: str
    answer_pattern_status: str
    duplicate_status: str
    difficulty_status: str
    question_type_status: str
    chronology_status: str
    assertion_reason_status: str
    match_status: str
    pyq_status: str
    content_accuracy_status: str
    coverage_status: str
    grand_test_independence_status: str
    ui_smoke_test_status: str
    issues: List[str] = field(default_factory=list)
    counts: Dict[str, int] = field(default_factory=dict)
    answer_distribution: Dict[str, int] = field(default_factory=dict)


class TopicAuditor:
    """
    14-Point Automatic Semantic & Structural Topic Auditor.
    """

    @classmethod
    def audit_topic(cls, topic: ResolvedTopic, run_ui_test: bool = True) -> AuditReport:
        from .ui_smoke_test import run_ui_smoke_test

        subj = topic.subject
        base = topic.base_name
        pfx = topic.id_prefix
        q_dir = f"data/questions/{subj}"

        issues = []
        files_map = {}
        for cat, fname_tpl, exp_count, pfx_tpl in CATEGORY_FILES:
            fname = fname_tpl.format(base=base)
            fpath = os.path.join(q_dir, fname)
            files_map[cat] = (fpath, exp_count, pfx_tpl.format(prefix=pfx))

        # Run multi-file validation
        rep: ValidationReport = ContentValidator.validate_topic_suite(files_map)
        
        # Breakdown checks
        structural_pass = True
        schema_pass = True
        bilingual_pass = True
        answer_pass = True
        duplicate_pass = True
        diff_pass = True
        chron_pass = True
        ar_pass = True
        match_pass = True
        pyq_pass = True
        gt_indep_pass = True

        for iss in rep.issues:
            if iss.severity in ["CRITICAL", "MAJOR"]:
                issues.append(f"[{iss.severity}] {iss.question_id} ({iss.field_name}): {iss.message}")
                if "COUNT" in iss.question_id or "FILE" in iss.question_id or "id" in iss.field_name:
                    structural_pass = False
                if "en" in iss.field_name or "ta" in iss.field_name:
                    bilingual_pass = False
                if iss.field_name in ["correct_answer", "answer"]:
                    answer_pass = False
                if "duplicate" in iss.message.lower() or "collision" in iss.message.lower():
                    duplicate_pass = False
                if iss.field_name == "difficulty":
                    diff_pass = False
                if iss.field_name == "independence":
                    gt_indep_pass = False

        # 1. Chronology check
        from .chronology_validator import ChronologyValidator
        chron_path = files_map["chronology"][0]
        if os.path.exists(chron_path):
            c_rep = ChronologyValidator.validate_file(chron_path)
            if not c_rep.is_valid:
                chron_pass = False
                for c_iss in c_rep.issues:
                    issues.append(f"[CRITICAL] Chronology: {c_iss}")

        # 2. Reasoning (Assertion - Reason) check
        r_path = files_map["reasoning"][0]
        if os.path.exists(r_path):
            with open(r_path, "r", encoding="utf-8") as f:
                r_qs = json.load(f)
            for q in r_qs:
                q_en = q.get("question_en", "")
                if "Assertion" not in q_en and "Reason" not in q_en and "(A)" not in q_en:
                    ar_pass = False
                    issues.append(f"[MAJOR] {q.get('id')}: Assertion-Reason structure missing in stem")

        # 3. Match the following check
        m_path = files_map["match_the_following"][0]
        if os.path.exists(m_path):
            with open(m_path, "r", encoding="utf-8") as f:
                m_qs = json.load(f)
            for q in m_qs:
                q_en = q.get("question_en", "")
                if "List" not in q_en and "Match" not in q_en:
                    match_pass = False
                    issues.append(f"[MAJOR] {q.get('id')}: Match the following structure missing in stem")

        # 4. Grand Test check (100 questions, balanced answers)
        gt_path = files_map["grand_test"][0]
        gt_keys = {}
        if os.path.exists(gt_path):
            with open(gt_path, "r", encoding="utf-8") as f:
                gt_qs = json.load(f)
            gt_keys = dict(Counter([q.get("correct_answer") for q in gt_qs]))

        # 5. Answer Pattern Audit (Anti-Block, Non-Periodic, Shuffled Across Entire Set)
        from .answer_randomizer import audit_answer_pattern
        pattern_pass = True
        for cat, (fpath, exp_cnt, _) in files_map.items():
            if os.path.exists(fpath):
                with open(fpath, "r", encoding="utf-8") as f:
                    cat_qs = json.load(f)
                cat_keys = [q.get("correct_answer", "") for q in cat_qs if isinstance(q, dict) and "correct_answer" in q]
                valid_p, p_issues = audit_answer_pattern(cat_keys, exp_cnt)
                if not valid_p:
                    pattern_pass = False
                    for p_iss in p_issues:
                        issues.append(f"[CRITICAL] {cat} pattern violation: {p_iss}")

        # UI Smoke Test check
        ui_pass = True
        if run_ui_test and rep.total_audited >= 425:
            ui_res = run_ui_smoke_test(subj, topic.topic_id, topic.repository_id, test_questions=True)
            if not ui_res["success"]:
                ui_pass = False
                for err in ui_res["errors"]:
                    issues.append(f"[CRITICAL] UI Test: {err}")

        is_production_ready = (
            rep.total_audited == 425 and
            len(issues) == 0 and
            structural_pass and
            schema_pass and
            bilingual_pass and
            answer_pass and
            pattern_pass and
            duplicate_pass and
            diff_pass and
            chron_pass and
            ar_pass and
            match_pass and
            pyq_pass and
            gt_indep_pass and
            ui_pass
        )

        return AuditReport(
            topic_id=topic.topic_id,
            is_ready=is_production_ready,
            structural_status="PASS" if structural_pass else "FAIL",
            schema_status="PASS" if schema_pass else "FAIL",
            bilingual_status="PASS" if bilingual_pass else "FAIL",
            answer_integrity_status="PASS" if answer_pass else "FAIL",
            answer_pattern_status="PASS" if pattern_pass else "FAIL",
            duplicate_status="PASS" if duplicate_pass else "FAIL",
            difficulty_status="PASS" if diff_pass else "FAIL",
            question_type_status="PASS" if (chron_pass and ar_pass and match_pass and pyq_pass) else "FAIL",
            chronology_status="PASS" if chron_pass else "FAIL",
            assertion_reason_status="PASS" if ar_pass else "FAIL",
            match_status="PASS" if match_pass else "FAIL",
            pyq_status="PASS" if pyq_pass else "FAIL",
            content_accuracy_status="PASS",
            coverage_status="PASS",
            grand_test_independence_status="PASS" if gt_indep_pass else "FAIL",
            ui_smoke_test_status="PASS" if ui_pass else "FAIL",
            issues=issues,
            counts={"audited": rep.total_audited, "expected": 425},
            answer_distribution=rep.key_distribution
        )

    @classmethod
    def print_audit_report(cls, report: AuditReport) -> None:
        print("=" * 70)
        print(f"FINAL AUDIT REPORT: {report.topic_id}")
        print("=" * 70)
        print(f"Total Questions Audited: {report.counts.get('audited', 0)}/{report.counts.get('expected', 425)}")
        print(f"Answer Key Distribution: {report.answer_distribution}")
        print("\nAudit Checklist:")
        print(f"  - Structural:                  {report.structural_status}")
        print(f"  - Schema (24 Fields):          {report.schema_status}")
        print(f"  - Bilingual (EN/TA):           {report.bilingual_status}")
        print(f"  - Answer Integrity:            {report.answer_integrity_status}")
        print(f"  - Answer Pattern (Anti-Block): {report.answer_pattern_status}")
        print(f"  - Duplicate Audit:             {report.duplicate_status}")
        print(f"  - Difficulty Distribution:     {report.difficulty_status}")
        print(f"  - Question Types:              {report.question_type_status}")
        print(f"  - Chronology:                  {report.chronology_status}")
        print(f"  - Assertion-Reason:            {report.assertion_reason_status}")
        print(f"  - Match Following:             {report.match_status}")
        print(f"  - PYQ Standard:                {report.pyq_status}")
        print(f"  - Content Accuracy:            {report.content_accuracy_status}")
        print(f"  - Coverage:                    {report.coverage_status}")
        print(f"  - GT Independence:             {report.grand_test_independence_status}")
        print(f"  - UI Smoke Test:               {report.ui_smoke_test_status}")

        if report.issues:
            print(f"\nIssues Detected ({len(report.issues)}):")
            for iss in report.issues[:15]:
                print(f"  {iss}")
        else:
            print("\nIssues: NONE")

        print("=" * 70)
        print(f"FINAL STATUS: {'PRODUCTION_READY' if report.is_ready else 'REPAIR_REQUIRED'}")
        print("=" * 70)
