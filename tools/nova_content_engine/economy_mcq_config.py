# -*- coding: utf-8 -*-
"""
Economy MCQ Engine Taxonomy and Configuration.
Maps all 25 canonical Economy topics to deterministic ID prefixes, slugs,
and category target distributions matching the Nova AI architecture.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class EconomyTopicConfig:
    topic_id: str
    repository_id: str
    display_title: str
    canonical_slug: str
    id_prefix: str
    total_parts: int = 3
    subject: str = "economy"


# 25 Canonical Economy Topics with Unique Deterministic ID Prefixes
ECONOMY_TOPICS: List[EconomyTopicConfig] = [
    EconomyTopicConfig(
        topic_id="economy_nature_and_structure_of_indian_economy",
        repository_id="economy_nature_and_structure_of_indian_economy",
        display_title="Nature and Structure of Indian Economy",
        canonical_slug="nature_and_structure_of_indian_economy",
        id_prefix="NSIE",
    ),
    EconomyTopicConfig(
        topic_id="economy_national_income",
        repository_id="economy_national_income",
        display_title="National Income",
        canonical_slug="national_income",
        id_prefix="NI",
    ),
    EconomyTopicConfig(
        topic_id="economy_planning_commission",
        repository_id="economy_planning_commission",
        display_title="Planning Commission",
        canonical_slug="planning_commission",
        id_prefix="PC",
    ),
    EconomyTopicConfig(
        topic_id="economy_five_year_plans",
        repository_id="economy_five_year_plans",
        display_title="Five Year Plans",
        canonical_slug="five_year_plans",
        id_prefix="FYP",
    ),
    EconomyTopicConfig(
        topic_id="economy_niti_aayog",
        repository_id="economy_niti_aayog",
        display_title="NITI Aayog",
        canonical_slug="niti_aayog",
        id_prefix="NA",
    ),
    EconomyTopicConfig(
        topic_id="economy_national_development_council",
        repository_id="economy_national_development_council",
        display_title="National Development Council",
        canonical_slug="national_development_council",
        id_prefix="NDC",
    ),
    EconomyTopicConfig(
        topic_id="economy_sources_of_revenue",
        repository_id="economy_sources_of_revenue",
        display_title="Sources of Revenue",
        canonical_slug="sources_of_revenue",
        id_prefix="SR",
    ),
    EconomyTopicConfig(
        topic_id="economy_fiscal_policy",
        repository_id="economy_fiscal_policy",
        display_title="Fiscal Policy",
        canonical_slug="fiscal_policy",
        id_prefix="FP",
    ),
    EconomyTopicConfig(
        topic_id="economy_monetary_policy",
        repository_id="economy_monetary_policy",
        display_title="Monetary Policy",
        canonical_slug="monetary_policy",
        id_prefix="MP",
    ),
    EconomyTopicConfig(
        topic_id="economy_reserve_bank_of_india",
        repository_id="economy_reserve_bank_of_india",
        display_title="Reserve Bank of India (RBI)",
        canonical_slug="reserve_bank_of_india",
        id_prefix="RBI",
    ),
    EconomyTopicConfig(
        topic_id="economy_banking",
        repository_id="economy_banking",
        display_title="Banking",
        canonical_slug="banking",
        id_prefix="BNK",
    ),
    EconomyTopicConfig(
        topic_id="economy_nabard",
        repository_id="economy_nabard",
        display_title="NABARD",
        canonical_slug="nabard",
        id_prefix="NAB",
    ),
    EconomyTopicConfig(
        topic_id="economy_finance_commission",
        repository_id="economy_finance_commission",
        display_title="Finance Commission",
        canonical_slug="finance_commission",
        id_prefix="FC",
    ),
    EconomyTopicConfig(
        topic_id="economy_gst",
        repository_id="economy_gst",
        display_title="GST",
        canonical_slug="gst",
        id_prefix="GST",
    ),
    EconomyTopicConfig(
        topic_id="economy_agriculture",
        repository_id="economy_agriculture",
        display_title="Agriculture",
        canonical_slug="agriculture",
        id_prefix="AGR",
    ),
    EconomyTopicConfig(
        topic_id="economy_industrial_growth",
        repository_id="economy_industrial_growth",
        display_title="Industrial Growth",
        canonical_slug="industrial_growth",
        id_prefix="IG",
    ),
    EconomyTopicConfig(
        topic_id="economy_msme",
        repository_id="economy_msme",
        display_title="MSME",
        canonical_slug="msme",
        id_prefix="MSME",
    ),
    EconomyTopicConfig(
        topic_id="economy_food_security",
        repository_id="economy_food_security",
        display_title="Food Security",
        canonical_slug="food_security",
        id_prefix="FS",
    ),
    EconomyTopicConfig(
        topic_id="economy_poverty",
        repository_id="economy_poverty",
        display_title="Poverty",
        canonical_slug="poverty",
        id_prefix="POV",
    ),
    EconomyTopicConfig(
        topic_id="economy_unemployment",
        repository_id="economy_unemployment",
        display_title="Unemployment",
        canonical_slug="unemployment",
        id_prefix="UNE",
    ),
    EconomyTopicConfig(
        topic_id="economy_population",
        repository_id="economy_population",
        display_title="Population",
        canonical_slug="population",
        id_prefix="POP",
    ),
    EconomyTopicConfig(
        topic_id="economy_health",
        repository_id="economy_health",
        display_title="Health",
        canonical_slug="health",
        id_prefix="HLT",
    ),
    EconomyTopicConfig(
        topic_id="economy_education",
        repository_id="economy_education",
        display_title="Education",
        canonical_slug="education",
        id_prefix="EDU",
    ),
    EconomyTopicConfig(
        topic_id="economy_mgnrega",
        repository_id="economy_mgnrega",
        display_title="MGNREGA",
        canonical_slug="mgnrega",
        id_prefix="MGN",
    ),
    EconomyTopicConfig(
        topic_id="economy_ayushman_bharat",
        repository_id="economy_ayushman_bharat",
        display_title="Ayushman Bharat",
        canonical_slug="ayushman_bharat",
        id_prefix="AB",
    ),
]

ECONOMY_TOPIC_MAP: Dict[str, EconomyTopicConfig] = {
    t.canonical_slug: t for t in ECONOMY_TOPICS
}
ECONOMY_TOPIC_ID_MAP: Dict[str, EconomyTopicConfig] = {
    t.topic_id: t for t in ECONOMY_TOPICS
}
ECONOMY_PREFIX_MAP: Dict[str, str] = {
    t.canonical_slug: t.id_prefix for t in ECONOMY_TOPICS
}

# Standard Category Naming and File Specifications
ECONOMY_CATEGORY_SPEC: List[Tuple[str, str, int, str]] = [
    ("easy", "{base}_easy.json", 50, "{prefix}_E_"),
    ("medium", "{base}_medium.json", 50, "{prefix}_M_"),
    ("hard", "{base}_hard.json", 50, "{prefix}_H_"),
    ("statement_based", "{base}_statement_based.json", 50, "{prefix}_SB_"),
    ("pyq", "{base}_pyq.json", 50, "{prefix}_PYQ_"),
    ("reasoning", "{base}_reasoning.json", 25, "{prefix}_AR_"),
    ("match_the_following", "{base}_match_the_following.json", 25, "{prefix}_MF_"),
    ("chronology", "{base}_chronology.json", 25, "{prefix}_CHRONO_"),
    ("grand_test", "{base}_grand_test.json", 100, "{prefix}_GT_"),
]

# Aliases for category code normalization
CATEGORY_CODE_MAP = {
    "easy": "E",
    "medium": "M",
    "hard": "H",
    "statement": "SB",
    "statement_based": "SB",
    "reasoning": "AR",
    "assertion_reason": "AR",
    "match": "MF",
    "match_the_following": "MF",
    "chronology": "CHRONO",
    "pyq": "PYQ",
    "pyq_practice": "PYQ",
    "grand_test": "GT",
    "grand": "GT",
}

# Legacy protected files (Nature and Structure of Indian Economy)
ECONOMY_LEGACY_FILES = {
    "nature_and_structure_of_indian_economy_easy.json",
    "nature_and_structure_of_indian_economy_medium.json",
    "nature_and_structure_of_indian_economy_hard.json",
}


def get_economy_topic_config(query_or_id: str) -> Optional[EconomyTopicConfig]:
    """Resolves an Economy topic config by slug, topic_id, or display_title."""
    if not query_or_id:
        return None
    clean = query_or_id.strip().lower()
    if clean.startswith("economy_"):
        clean_slug = clean[len("economy_"):]
    else:
        clean_slug = clean

    if clean in ECONOMY_TOPIC_ID_MAP:
        return ECONOMY_TOPIC_ID_MAP[clean]
    if clean_slug in ECONOMY_TOPIC_MAP:
        return ECONOMY_TOPIC_MAP[clean_slug]

    # Match by display title
    for t in ECONOMY_TOPICS:
        if t.display_title.lower() == clean or clean in t.display_title.lower():
            return t
    return None
