import json
import os
from typing import Any, Dict, List, Optional

from core.navigation_v2.navigation_state import check_repository_availability, discover_note_parts
from .topic_resolver import ResolvedTopic, resolve_topic
from .checkpoint import PipelineCheckpointManager


CATEGORY_FILES = [
    ("easy", "{base}_easy.json", 50, "{prefix}_E_"),
    ("medium", "{base}_medium.json", 50, "{prefix}_M_"),
    ("hard", "{base}_hard.json", 50, "{prefix}_H_"),
    ("statement_based", "{base}_statement_based.json", 50, "{prefix}_S_"),
    ("pyq", "{base}_pyq.json", 50, "{prefix}_PYQ_"),
    ("reasoning", "{base}_reasoning.json", 25, "{prefix}_R_"),
    ("match_the_following", "{base}_match_the_following.json", 25, "{prefix}_MF_"),
    ("chronology", "{base}_chronology.json", 25, "{prefix}_C_"),
    ("grand_test", "{base}_grand_test.json", 100, "{prefix}_GT_"),
]


class TopicDiscovery:
    """
    Topic discovery engine for Nova AI.
    Discovers notes, blueprints, questions, and pipeline states for any canonical topic.
    """

    @classmethod
    def discover(cls, topic: ResolvedTopic) -> Dict[str, Any]:
        subj = topic.subject
        base = topic.base_name
        pfx = topic.id_prefix

        # 1. Notes discovery
        parts_map = discover_note_parts(subj, base)
        notes_info = {
            "found": len(parts_map) > 0,
            "parts_count": len(parts_map),
            "parts_map": parts_map
        }

        # 2. Blueprint discovery
        bp_path = f"data/blueprints/{subj}/{base}_blueprint.json"
        bp_exists = os.path.exists(bp_path)
        bp_info = {
            "exists": bp_exists,
            "path": bp_path,
            "subtopics_count": 0,
            "articles_count": 0,
            "traps_count": 0
        }
        if bp_exists:
            try:
                with open(bp_path, "r", encoding="utf-8") as f:
                    bp_data = json.load(f)
                bp_info["subtopics_count"] = len(bp_data.get("subtopics", []))
                bp_info["articles_count"] = len(bp_data.get("articles", []))
                bp_info["traps_count"] = len(bp_data.get("tnpsc_traps", []))
            except Exception:
                pass

        # 3. Questions discovery
        q_dir = f"data/questions/{subj}"
        questions_info = {}
        total_core = 0
        grand_test_count = 0

        for cat, fname_tpl, expected_count, pfx_tpl in CATEGORY_FILES:
            fname = fname_tpl.format(base=base)
            fpath = os.path.join(q_dir, fname)
            exists = os.path.exists(fpath)
            actual_count = 0
            is_valid_json = False

            if exists:
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if isinstance(data, list):
                        actual_count = len(data)
                        is_valid_json = True
                except Exception:
                    pass

            if cat == "grand_test":
                grand_test_count = actual_count
            else:
                total_core += actual_count

            questions_info[cat] = {
                "file": fname,
                "path": fpath,
                "exists": exists,
                "expected": expected_count,
                "count": actual_count,
                "is_valid_json": is_valid_json,
                "prefix": pfx_tpl.format(prefix=pfx)
            }

        # 4. Checkpoint discovery
        ckpt_mgr = PipelineCheckpointManager(topic.topic_id)
        status_data = ckpt_mgr.load()

        return {
            "topic": {
                "subject": subj,
                "topic_id": topic.topic_id,
                "repository_id": topic.repository_id,
                "display_title": topic.display_title,
                "base_name": base,
                "id_prefix": pfx,
                "total_parts": topic.total_parts
            },
            "notes": notes_info,
            "blueprint": bp_info,
            "questions": questions_info,
            "counts": {
                "core": total_core,
                "grand_test": grand_test_count,
                "overall": total_core + grand_test_count,
                "target_core": 325,
                "target_gt": 100,
                "target_overall": 425
            },
            "pipeline_status": status_data
        }

    @classmethod
    def print_summary(cls, disc: Dict[str, Any]) -> None:
        t = disc["topic"]
        print("=" * 70)
        print(f"DISCOVERY REPORT: {t['display_title']} ({t['topic_id']})")
        print("=" * 70)
        print(f"Subject:       {t['subject'].upper()}")
        print(f"Repository ID: {t['repository_id']}")
        print(f"ID Prefix:     {t['id_prefix']}")
        print(f"Notes:         {'FOUND' if disc['notes']['found'] else 'NOT FOUND'} ({disc['notes']['parts_count']} parts)")
        for pnum, ppath in disc['notes']['parts_map'].items():
            print(f"  - Part {pnum}: {ppath}")

        bp = disc["blueprint"]
        print(f"Blueprint:     {'READY' if bp['exists'] else 'MISSING'} ({bp['path']})")
        if bp["exists"]:
            print(f"  - Subtopics: {bp['subtopics_count']} | Articles: {bp['articles_count']} | Traps: {bp['traps_count']}")

        cnt = disc["counts"]
        print(f"Question Progress:")
        print(f"  - Core Questions:   {cnt['core']}/{cnt['target_core']}")
        print(f"  - Grand Test:       {cnt['grand_test']}/{cnt['target_gt']}")
        print(f"  - Overall Topic:    {cnt['overall']}/{cnt['target_overall']}")

        print("\nCategories Detail:")
        for cat, qinfo in disc["questions"].items():
            status_tag = f"[COMPLETE] {qinfo['count']}/{qinfo['expected']}" if qinfo['count'] == qinfo['expected'] and qinfo['count'] > 0 else f"[PENDING]  {qinfo['count']}/{qinfo['expected']}"
            print(f"  - {cat:20}: {status_tag} ({qinfo['file']})")

        print(f"\nPipeline State: {disc['pipeline_status'].get('state', 'UNKNOWN')}")
        print("=" * 70)
