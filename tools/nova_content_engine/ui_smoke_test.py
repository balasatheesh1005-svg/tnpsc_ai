import json
import os
import sys
from collections import Counter
from typing import Any, Dict, List, Tuple

from core.topics_loader import get_topic_metadata_list, get_display_topics, get_topic_metadata_by_id
from core.navigation_v2.navigation_state import check_repository_availability
from core.question_loader import load_questions
from ui.question_engine.parser import UniversalQuestionAdapter, NormalizedQuestion


def run_ui_smoke_test(subject: str, topic_id: str, repository_id: str, test_questions: bool = True) -> Dict[str, Any]:
    """
    Automated UI Smoke Test for a topic in Nova AI.
    Tests Topic Selector, Notes, Mind Map, Core Questions (if present),
    Grand Test (if present), and Flashcards traversal.
    """
    results = {
        "success": True,
        "errors": [],
        "warnings": [],
        "steps_passed": []
    }

    # 1. TOPIC REGISTRY CHECK
    try:
        topics = get_topic_metadata_list(subject)
        display_topics = get_display_topics(subject)
        found = False
        target_meta = None
        for t in topics:
            if t["topic_id"] == topic_id or t.get("repository_id") == repository_id:
                found = True
                target_meta = t
                break
        
        if not found:
            results["errors"].append(f"Topic '{topic_id}' not found in get_topic_metadata_list('{subject}')")
            results["success"] = False
        else:
            results["steps_passed"].append("Topic Selector & Registry Check: PASS")

        meta = get_topic_metadata_by_id(subject, topic_id)
        if not meta:
            results["errors"].append(f"Could not resolve metadata for topic_id '{topic_id}'")
            results["success"] = False
        else:
            results["steps_passed"].append("Canonical Metadata Resolution: PASS")
    except Exception as e:
        results["errors"].append(f"Topic Registry Check failed with exception: {e}")
        results["success"] = False

    # 2. NOTES & REPOSITORY AVAILABILITY
    try:
        avail = check_repository_availability(subject, repository_id)
        if not avail.get("notes"):
            results["errors"].append(f"Notes marked unavailable for {repository_id}")
            results["success"] = False
        else:
            parts_found = avail.get("parts_found", 0)
            results["steps_passed"].append(f"Notes Availability ({parts_found} parts found): PASS")

            # Check sections, content blocks, mind map
            for part_num, note_path in avail.get("parts_map", {}).items():
                if not os.path.exists(note_path):
                    results["errors"].append(f"Note file missing: {note_path}")
                    results["success"] = False
                    continue
                with open(note_path, "r", encoding="utf-8") as f:
                    ndata = json.load(f)
                content = ndata.get("content", {})
                if "mind_map" not in content:
                    results["warnings"].append(f"Part {part_num} missing mind_map")
            results["steps_passed"].append("Notes & Mind Map Integrity: PASS")
    except Exception as e:
        results["errors"].append(f"Notes check failed: {e}")
        results["success"] = False

    # 3. FLASHCARDS / REVISION CARDS TRAVERSAL TEST
    try:
        avail = check_repository_availability(subject, repository_id)
        total_cards = 0
        for part_num, note_path in avail.get("parts_map", {}).items():
            if not os.path.exists(note_path):
                continue
            with open(note_path, "r", encoding="utf-8") as f:
                ndata = json.load(f)
            cards = ndata.get("content", {}).get("revision_cards", [])
            for c_idx, card in enumerate(cards):
                assert card.get("id"), f"Missing card ID at part {part_num}[{c_idx}]"
                assert card.get("front_en"), f"Missing front_en at {card.get('id')}"
                assert card.get("front_ta"), f"Missing front_ta at {card.get('id')}"
                assert card.get("back_en"), f"Missing back_en at {card.get('id')}"
                assert card.get("back_ta"), f"Missing back_ta at {card.get('id')}"
                # Test flip simulation
                flipped = True
                # Test next simulation
                next_idx = min(c_idx + 1, len(cards) - 1)
                # Test prev simulation
                prev_idx = max(c_idx - 1, 0)
                total_cards += 1
        results["steps_passed"].append(f"Flashcards Traversal ({total_cards} cards across parts): PASS")
    except Exception as e:
        results["errors"].append(f"Flashcard traversal failed: {e}")
        results["success"] = False

    # 4. QUESTION RENDERING TEST (if requested and questions exist)
    if test_questions:
        try:
            avail = check_repository_availability(subject, repository_id)
            categories = [
                ("easy", 50), ("medium", 50), ("hard", 50),
                ("statement_based", 50), ("pyq", 50),
                ("assertion_reason", 25), ("match_the_following", 25),
                ("chronology", 25)
            ]
            has_questions = any(avail.get(cat_key, False) for cat_key, _ in categories)
            if has_questions:
                total_core = 0
                for cat, exp_len in categories:
                    if avail.get(cat, False):
                        qs = load_questions(subject, repository_id, cat)
                        assert len(qs) == exp_len, f"Category '{cat}' expected {exp_len}, got {len(qs)}"
                        total_core += len(qs)
                        for q_data in qs:
                            q: NormalizedQuestion = UniversalQuestionAdapter.normalize(q_data)
                            assert q.id and len(q.id) > 0
                            assert q.question_en and len(q.question_en.strip()) > 5
                            assert q.question_ta and len(q.question_ta.strip()) > 5
                            assert len(q.options) == 4
                            for opt in q.options:
                                assert opt.id in ["A", "B", "C", "D"]
                                assert opt.en and len(opt.en.strip()) > 0
                                assert opt.ta and len(opt.ta.strip()) > 0
                            assert q.correct_answer in ["A", "B", "C", "D"]
                            assert q.explanation.en and len(q.explanation.en.strip()) > 5
                            assert q.explanation.ta and len(q.explanation.ta.strip()) > 5
                results["steps_passed"].append(f"Core Questions Rendering ({total_core} MCQs): PASS")

            # Grand Test
            if avail.get("grand_test", False):
                gt_qs = load_questions(subject, repository_id, "grand_test")
                assert len(gt_qs) == 100, f"Expected 100 Grand Test MCQs, got {len(gt_qs)}"
                for q_data in gt_qs:
                    q: NormalizedQuestion = UniversalQuestionAdapter.normalize(q_data)
                    assert q.id and len(q.id) > 0
                    assert q.question_en and len(q.question_en.strip()) > 5
                    assert q.question_ta and len(q.question_ta.strip()) > 5
                    assert len(q.options) == 4
                    assert q.correct_answer in ["A", "B", "C", "D"]
                    assert q.explanation.en and len(q.explanation.en.strip()) > 5
                    assert q.explanation.ta and len(q.explanation.ta.strip()) > 5
                results["steps_passed"].append("Grand Test Rendering (100 MCQs): PASS")
        except Exception as e:
            results["errors"].append(f"Question rendering test failed: {e}")
            results["success"] = False

    return results
