# -*- coding: utf-8 -*-
import argparse
import os
import re
import sys
from typing import List, Optional, Tuple

if __package__ is None or __package__ == "":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
    from tools.nova_content_engine.topic_resolver import resolve_topic, set_active_topic, ResolvedTopic
    from tools.nova_content_engine.discovery import TopicDiscovery
    from tools.nova_content_engine.blueprint_manager import BlueprintManager
    from tools.nova_content_engine.checkpoint import PipelineCheckpointManager, PipelineState
    from tools.nova_content_engine.validator import ContentValidator
    from tools.nova_content_engine.generator_runner import GeneratorRunner
    from tools.nova_content_engine.audit import TopicAuditor
    from tools.nova_content_engine.ui_smoke_test import run_ui_smoke_test
    from tools.nova_content_engine.auto_chain import AutoChainPipeline
else:
    from .topic_resolver import resolve_topic, set_active_topic, ResolvedTopic
    from .discovery import TopicDiscovery
    from .blueprint_manager import BlueprintManager
    from .checkpoint import PipelineCheckpointManager, PipelineState
    from .validator import ContentValidator
    from .generator_runner import GeneratorRunner
    from .audit import TopicAuditor
    from .ui_smoke_test import run_ui_smoke_test
    from .auto_chain import AutoChainPipeline

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def print_section25_status(topic: ResolvedTopic) -> None:
    """Prints status matching Section 25 format."""
    disc = TopicDiscovery.discover(topic)
    q = disc["questions"]
    bp = disc["blueprint"]

    bp_status = "READY" if bp["exists"] else "MISSING"

    # Part 1
    p1_count = q["easy"]["count"] + q["medium"]["count"] + q["hard"]["count"]
    if p1_count == 150:
        p1_status = "COMPLETE 150/150"
    elif p1_count > 0:
        p1_status = f"RUNNING {p1_count}/150"
    else:
        p1_status = "PENDING"

    # Part 2A
    p2a_count = q["statement_based"]["count"] + q["pyq"]["count"]
    if p2a_count == 100:
        p2a_status = "COMPLETE 100/100"
    elif p2a_count > 0:
        p2a_status = f"RUNNING {p2a_count}/100"
    else:
        p2a_status = "PENDING"

    # Part 2B
    p2b_count = q["reasoning"]["count"] + q["match_the_following"]["count"] + q["chronology"]["count"]
    if p2b_count == 75:
        p2b_status = "COMPLETE 75/75"
    elif p2b_count > 0:
        p2b_status = f"RUNNING {p2b_count}/75"
    else:
        p2b_status = "PENDING"

    # Part 3
    p3_count = q["grand_test"]["count"]
    if p3_count == 100:
        p3_status = "COMPLETE 100/100"
    elif p3_count > 0:
        p3_status = f"RUNNING {p3_count}/100"
    else:
        p3_status = "PENDING"

    core_count = p1_count + p2a_count + p2b_count
    gt_count = p3_count
    overall_count = core_count + gt_count

    print(f"Topic:\n{topic.display_title}\n")
    print(f"Blueprint:\n{bp_status}\n")
    print(f"Part 1:\n{p1_status}\n")
    print(f"Part 2A:\n{p2a_status}\n")
    print(f"Part 2B:\n{p2b_status}\n")
    print(f"Part 3:\n{p3_status}\n")
    print(f"Core:\n{core_count}/325\n")
    print(f"Grand Test:\n{gt_count}/100\n")
    print(f"Overall:\n{overall_count}/425\n")
    print("Auto-chain:\nENABLED")


def parse_natural_command(text: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Parses natural language strings into (command, sub_arg, topic_hint).
    Supports:
      'Generate Part 1 MCQ' -> ('generate', 'part1', None)
      'Generate Part 2A MCQ' -> ('generate', 'part2a', None)
      'Generate Part 2B MCQ' -> ('generate', 'part2b', None)
      'Generate Part 3' -> ('generate', 'part3', None)
      'Generate Topic' / 'Complete Topic' -> ('generate', None, None)
      'Generate Part 1 MCQ for Centre–State Relations' -> ('generate', 'part1', 'Centre–State Relations')
      'status for Governor' -> ('status', None, 'Governor')
    """
    t = text.strip()
    topic_hint = None

    # Extract topic hint if 'for <topic>' is present
    topic_match = re.search(r"\bfor\s+(.+)$", t, re.IGNORECASE)
    if topic_match:
        topic_hint = topic_match.group(1).strip()
        t = re.sub(r"\bfor\s+(.+)$", "", t, flags=re.IGNORECASE).strip()

    t_lower = t.lower()

    if "status" in t_lower:
        return "status", None, topic_hint
    if "discover" in t_lower:
        return "discover", None, topic_hint
    if "blueprint" in t_lower:
        return "blueprint", None, topic_hint
    if "part 1" in t_lower or "part1" in t_lower:
        return "generate", "part1", topic_hint
    if "part 2a" in t_lower or "part2a" in t_lower:
        return "generate", "part2a", topic_hint
    if "part 2b" in t_lower or "part2b" in t_lower:
        return "generate", "part2b", topic_hint
    if "part 3" in t_lower or "part3" in t_lower or "grand test" in t_lower:
        return "generate", "part3", topic_hint
    if "generate topic" in t_lower or "complete topic" in t_lower or "complete" in t_lower:
        return "generate", None, topic_hint
    if "validate" in t_lower or "audit" in t_lower:
        return "validate", None, topic_hint
    if "smoke" in t_lower or "ui" in t_lower:
        return "smoke_test", None, topic_hint

    return None, None, topic_hint


def build_help_parser() -> argparse.ArgumentParser:
    """Build the parser used for side-effect-free CLI help output."""
    parser = argparse.ArgumentParser(
        prog="nova-content-engine",
        description="TNPSC Nova AI content-engine workflow CLI",
    )
    parser.add_argument(
        "command",
        nargs="*",
        help="status, discover, blueprint, generate, validate, smoke_test, or a natural-language command",
    )
    parser.add_argument("--topic", help="Topic name, slug, or topic ID")
    parser.add_argument("--subject", default="polity", help="Subject namespace (default: polity)")
    parser.add_argument("--dry-run", action="store_true", help="Plan generation without writing files")
    parser.add_argument("--part-only", action="store_true", help="Run only the requested content part")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if "--help" in argv or "-h" in argv:
        build_help_parser().print_help()
        return 0

    # Separate flags from arguments
    dry_run = "--dry-run" in argv
    part_only = "--part-only" in argv
    
    # Check for --topic and --subject in argv
    topic_arg = None
    subject_arg = "polity"
    cleaned_argv = []
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg in ["--dry-run", "--part-only"]:
            i += 1
        elif arg == "--topic" and i + 1 < len(argv):
            topic_arg = argv[i + 1]
            i += 2
        elif arg.startswith("--topic="):
            topic_arg = arg.split("=", 1)[1]
            i += 1
        elif arg == "--subject" and i + 1 < len(argv):
            subject_arg = argv[i + 1]
            i += 2
        elif arg.startswith("--subject="):
            subject_arg = arg.split("=", 1)[1]
            i += 1
        else:
            cleaned_argv.append(arg)
            i += 1

    # Check natural command from joined cleaned_argv
    cmd = None
    target = None
    if cleaned_argv:
        joined_text = " ".join(cleaned_argv)
        nat_cmd, nat_target, nat_topic = parse_natural_command(joined_text)
        if nat_cmd:
            cmd = nat_cmd
            target = nat_target
            if nat_topic and not topic_arg:
                topic_arg = nat_topic
        elif cleaned_argv[0] in ["status", "discover", "blueprint", "generate", "complete", "run", "validate", "smoke_test"]:
            cmd = cleaned_argv[0]
            if len(cleaned_argv) > 1:
                target = cleaned_argv[1]
    else:
        cmd = "status"

    if not cmd:
        cmd = "status"

    # 1. Topic Resolution
    topic: ResolvedTopic = resolve_topic(topic_arg, subject=subject_arg)

    # 2. Command Dispatch
    if cmd == "status":
        print_section25_status(topic)
        return 0

    elif cmd == "discover":
        disc = TopicDiscovery.discover(topic)
        TopicDiscovery.print_summary(disc)
        return 0

    elif cmd == "blueprint":
        bp = BlueprintManager.load_or_build(topic)
        print(f"[NOVA] Blueprint: {topic.display_title}")
        print(f"  - Target: {bp.get('target')}")
        print(f"  - Subtopics: {len(bp.get('subtopics', []))}")
        print(f"  - Articles: {len(bp.get('articles', []))}")
        print(f"  - TNPSC Traps: {len(bp.get('tnpsc_traps', []))}")
        ckpt = PipelineCheckpointManager(topic.topic_id, topic.display_title)
        ckpt.save(state=PipelineState.BLUEPRINT_READY, notes="Blueprint verified")
        print(f"[NOVA] Status updated: BLUEPRINT_READY")
        return 0

    elif cmd in ["generate", "complete", "run"]:
        auto_pipeline = AutoChainPipeline(topic)
        start_part = target
        if not start_part:
            start_part = auto_pipeline.get_first_incomplete_part()

        res = auto_pipeline.execute_auto_chain(
            start_part=start_part,
            part_only=part_only,
            dry_run=dry_run
        )
        return 0 if res.get("success") else 1

    elif cmd == "validate":
        print(f"[NOVA] Running automatic multi-file validation for '{topic.display_title}'...")
        rep = TopicAuditor.audit_topic(topic, run_ui_test=False)
        TopicAuditor.print_audit_report(rep)
        return 0 if rep.is_ready else 1

    elif cmd == "smoke_test":
        print(f"[NOVA] Running automated UI smoke test for '{topic.display_title}'...")
        res = run_ui_smoke_test(topic.subject, topic.topic_id, topic.repository_id, test_questions=True)
        print(f"[NOVA] UI Smoke Test Result: {'PASS' if res['success'] else 'FAIL'}")
        for step in res["steps_passed"]:
            print(f"  [PASS] {step}")
        if res["errors"]:
            print("Errors:")
            for err in res["errors"]:
                print(f"  [FAIL] {err}")
        return 0 if res["success"] else 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
