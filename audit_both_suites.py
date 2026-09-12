# -*- coding: utf-8 -*-
from tools.nova_content_engine.validator import ContentValidator

def audit():
    print("=== 1. AUDITING ELECTION COMMISSION & ELECTORAL SYSTEM ===")
    ec_files = {
        "easy": ("data/questions/polity/election_commission_easy.json", 50, "EC_E_"),
        "medium": ("data/questions/polity/election_commission_medium.json", 50, "EC_M_"),
        "hard": ("data/questions/polity/election_commission_hard.json", 50, "EC_H_"),
        "statement": ("data/questions/polity/election_commission_statement_based.json", 50, "EC_S_"),
        "reasoning": ("data/questions/polity/election_commission_reasoning.json", 25, "EC_R_"),
        "chronology": ("data/questions/polity/election_commission_chronology.json", 25, "EC_C_"),
        "match": ("data/questions/polity/election_commission_match_the_following.json", 25, "EC_MF_"),
        "pyq": ("data/questions/polity/election_commission_pyq.json", 50, "EC_PYQ_"),
        "grand_test": ("data/questions/polity/election_commission_grand_test.json", 100, "EC_GT_")
    }
    ec_rep = ContentValidator.validate_topic_suite(ec_files)
    ec_major_crit = [i for i in ec_rep.issues if i.severity in ["CRITICAL", "MAJOR"]]
    print(f"EC Status: {'PASS' if ec_rep.is_valid else 'FAIL'}")
    print(f"Total Audited: {ec_rep.total_audited}")
    print(f"Key Distribution: {ec_rep.key_distribution}")
    print(f"Major/Critical Issues: {len(ec_major_crit)}")

    print("\n=== 2. AUDITING ELECTORAL REFORMS ===")
    er_files = {
        "easy": ("data/questions/polity/electoral_reforms_easy.json", 50, "ER_E_"),
        "medium": ("data/questions/polity/electoral_reforms_medium.json", 50, "ER_M_"),
        "hard": ("data/questions/polity/electoral_reforms_hard.json", 50, "ER_H_"),
        "statement": ("data/questions/polity/electoral_reforms_statement_based.json", 50, "ER_S_"),
        "reasoning": ("data/questions/polity/electoral_reforms_reasoning.json", 25, "ER_R_"),
        "chronology": ("data/questions/polity/electoral_reforms_chronology.json", 25, "ER_C_"),
        "match": ("data/questions/polity/electoral_reforms_match_the_following.json", 25, "ER_MF_"),
        "pyq": ("data/questions/polity/electoral_reforms_pyq.json", 50, "ER_PYQ_"),
        "grand_test": ("data/questions/polity/electoral_reforms_grand_test.json", 100, "ER_GT_")
    }
    er_rep = ContentValidator.validate_topic_suite(er_files)
    er_major_crit = [i for i in er_rep.issues if i.severity in ["CRITICAL", "MAJOR"]]
    print(f"ER Status: {'PASS' if er_rep.is_valid else 'FAIL'}")
    print(f"Total Audited: {er_rep.total_audited}")
    print(f"Key Distribution: {er_rep.key_distribution}")
    print(f"Major/Critical Issues: {len(er_major_crit)}")

    print("\n==========================================")
    if ec_rep.is_valid and er_rep.is_valid:
        print("BOTH TOPICS (850 MCQs TOTAL) FULLY CERTIFIED AND PRODUCTION-READY!")
    else:
        print("Issues found in one or more suites.")

if __name__ == "__main__":
    audit()
