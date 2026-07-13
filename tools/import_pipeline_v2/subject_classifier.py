"""Deterministic approved-taxonomy subject classifier."""
TAXONOMY = ("Polity", "History", "Geography", "Economy", "Science", "Environment", "Current Affairs", "Aptitude", "Reasoning", "Indian Society", "Tamil Society", "Art & Culture", "General Knowledge")
KEYWORDS = {
    "Polity": ("constitution", "parliament", "president", "governor", "article ", "supreme court", "panchayat"),
    "History": ("dynasty", "revolt", "independence", "satyagraha", "ancient", "medieval", "freedom movement"),
    "Geography": ("river", "monsoon", "latitude", "mountain", "soil", "climate", "plateau"),
    "Economy": ("gdp", "inflation", "budget", "bank", "rupee", "fiscal", "poverty"),
    "Science": ("physics", "chemical", "cell", "virus", "planet", "atom", "energy"),
    "Environment": ("biodiversity", "ecosystem", "pollution", "wildlife", "climate change", "forest"),
    "Aptitude": ("percentage", "ratio", "average", "profit", "simple interest", "compound interest"),
    "Reasoning": ("series", "coding", "blood relation", "direction", "analogy"),
    "Tamil Society": ("tamil nadu", "tamil society", "dravidian"),
    "Indian Society": ("caste", "tribe", "census", "gender", "population"),
    "Art & Culture": ("dance", "music", "temple", "painting", "literature", "festival"),
}


def classify(question):
    text = (str(question.get("question_en") or "") + " " + " ".join((question.get("options") or {}).values())).lower()
    best = max(((sum(word in text for word in words), subject) for subject, words in KEYWORDS.items()), default=(0, "General Knowledge"))
    return best[1] if best[0] else "General Knowledge"
