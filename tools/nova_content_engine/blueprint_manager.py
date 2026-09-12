import json
import os
import re
from typing import Any, Dict, List, Optional

from core.navigation_v2.navigation_state import discover_note_parts
from .topic_resolver import ResolvedTopic


class BlueprintManager:
    """
    Manages topic blueprints. Loads existing blueprints without regenerating,
    or synthesizes a production blueprint from notes if missing.
    """

    @classmethod
    def get_blueprint_path(cls, topic: ResolvedTopic) -> str:
        return f"data/blueprints/{topic.subject}/{topic.base_name}_blueprint.json"

    @classmethod
    def load_or_build(cls, topic: ResolvedTopic) -> Dict[str, Any]:
        bp_path = cls.get_blueprint_path(topic)
        if os.path.exists(bp_path):
            with open(bp_path, "r", encoding="utf-8") as f:
                return json.load(f)

        # If not present, synthesize from notes
        print(f"[NOVA] Blueprint not found at {bp_path}. Building blueprint from topic notes...")
        blueprint = cls.build_from_notes(topic)
        os.makedirs(os.path.dirname(bp_path), exist_ok=True)
        with open(bp_path, "w", encoding="utf-8") as f:
            json.dump(blueprint, f, indent=2, ensure_ascii=False)
        print(f"[NOVA] Saved newly synthesized blueprint to {bp_path}")
        return blueprint

    @classmethod
    def build_from_notes(cls, topic: ResolvedTopic) -> Dict[str, Any]:
        subj = topic.subject
        base = topic.base_name
        parts_map = discover_note_parts(subj, base)
        
        all_sections = []
        all_articles = []
        all_traps = []
        all_facts = []
        all_comparisons = []
        all_chronology = []

        for pnum, ppath in parts_map.items():
            if not os.path.exists(ppath):
                continue
            with open(ppath, "r", encoding="utf-8") as f:
                ndata = json.load(f)
            
            content = ndata.get("content", {})
            for k, v in content.items():
                if k.startswith("sec_"):
                    sec_item = v[0] if isinstance(v, list) and len(v) > 0 else v
                    title_dict = sec_item.get("title", {})
                    title_en = title_dict.get("en", "") if isinstance(title_dict, dict) else str(title_dict)
                    all_sections.append({
                        "key": k,
                        "title": title_en,
                        "part": pnum
                    })
                    # Extract articles
                    art_matches = re.findall(r"Article\s+(\d+[A-Z]?)", title_en)
                    for am in art_matches:
                        all_articles.append(f"Article {am}")

                elif k == "tnpsc_traps":
                    if isinstance(v, list):
                        for t in v:
                            t_title = t.get("title") or t
                            if isinstance(t_title, dict):
                                t_en = t_title.get("en", "")
                            else:
                                t_en = str(t_title)
                            all_traps.append(t_en)

                elif k in ["timeline", "chronology"]:
                    if isinstance(v, list):
                        all_chronology.extend(v)

        # Unique articles
        unique_articles = sorted(list(set(all_articles)))
        articles_list = [{"article": a, "title": f"Provisions relating to {a}"} for a in unique_articles]

        # Structure default subtopics
        subtopics = []
        if all_sections:
            # Group into 5 balanced subtopics
            chunk_size = max(1, len(all_sections) // 5)
            for idx in range(5):
                start_i = idx * chunk_size
                end_i = (idx + 1) * chunk_size if idx < 4 else len(all_sections)
                chunk = all_sections[start_i:end_i]
                names = [c["title"] for c in chunk if c["title"]]
                sub_title = " & ".join(names[:2]) if names else f"Subtopic {idx + 1}"
                subtopics.append({
                    "id": f"subtopic_{idx + 1}",
                    "name": sub_title[:80],
                    "coverage": f"Covers key provisions in {sub_title}",
                    "articles": [a for a in unique_articles[idx*3:(idx+1)*3]],
                    "key_concepts": names,
                    "tnpsc_traps": all_traps[idx*2:(idx+1)*2],
                    "question_models": ["Conceptual", "Statement", "Match"],
                    "priority": "High",
                    "core_allocation": 65,
                    "grand_test_allocation": 20
                })
        else:
            # Generic 5 subtopics
            for idx in range(1, 6):
                subtopics.append({
                    "id": f"subtopic_{idx}",
                    "name": f"{topic.display_title} Component {idx}",
                    "coverage": f"Core syllabus component {idx}",
                    "articles": [],
                    "key_concepts": [],
                    "tnpsc_traps": [],
                    "question_models": ["Standard", "Statement", "Reasoning"],
                    "priority": "High",
                    "core_allocation": 65,
                    "grand_test_allocation": 20
                })

        traps_data = [
            {"trap_id": f"TRAP_{i+1:02d}", "name": t[:50], "description": t}
            for i, t in enumerate(all_traps[:15])
        ]

        source_notes_list = [str(p) for p in parts_map.values()]

        return {
            "topic": topic.display_title,
            "topic_id": topic.topic_id,
            "repository_id": topic.repository_id,
            "display_title": topic.display_title,
            "subject": subj,
            "source_notes": source_notes_list,
            "target": {
                "core": 325,
                "grand_test": 100,
                "overall": 425
            },
            "subtopics": subtopics,
            "articles": articles_list,
            "important_cases": [],
            "commissions_committees": [],
            "constitutional_provisions": [],
            "comparison_targets": [],
            "chronology_targets": all_chronology,
            "tnpsc_traps": traps_data,
            "source_boundaries": source_notes_list + [
                "M. Laxmikanth – Indian Polity",
                "NCERT Class XI – Indian Constitution at Work",
                "Tamil Nadu Samacheer Kalvi Political Science"
            ],
            "mcq_generation_rules": {
                "avoid_repetition": True,
                "require_bilingual": True,
                "require_distractor_analysis": True,
                "require_revision_fact": True
            }
        }
