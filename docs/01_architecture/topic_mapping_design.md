# Topic Mapping Design Specification

## Overview

This specification details the schema, registry structure, and lookup API for TNPSC Nova AI's topic metadata system.

---

## Topic Metadata Schema

Every topic entry in `data/structure/{subject}_structure.json` is defined by the following standard JSON metadata object:

```json
{
  "topic_id": "polity_historical_background_part1",
  "repository_id": "polity_historical_background",
  "display_title": "Historical Background Part 1",
  "part": 1,
  "total_parts": 4,
  "subject": "polity"
}
```

### Attribute Definitions

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `topic_id` | String | Permanent unique ID for the specific note part / payload |
| `repository_id` | String | Permanent ID pointing to the complete practice question repository |
| `display_title` | String | UI display string rendered in breadcrumbs, titles, and cards |
| `part` | Integer | Part index for split notes (1-indexed) |
| `total_parts` | Integer | Total count of note parts for the topic area |
| `subject` | String | Lowercase subject identifier (e.g. `polity`, `history`) |

---

## Single-Part & Legacy Topic Normalization

For topics that are not divided into multiple parts (or legacy simple string entries in structure JSONs), the system automatically constructs a 1:1 mapping:

```json
{
  "topic_id": "polity_making_of_indian_constitution",
  "repository_id": "polity_making_of_indian_constitution",
  "display_title": "Making of Indian Constitution",
  "part": 1,
  "total_parts": 1,
  "subject": "polity"
}
```

---

## Loader API Contract (`core/topics_loader.py`)

- `get_topic_metadata_list(subject: str) -> List[Dict]`
  Loads and normalizes all topic metadata for a subject.
- `get_topic_metadata_by_id(subject: str, topic_id_or_title: str) -> Dict`
  Resolves metadata by `topic_id`, `repository_id`, or legacy title string.
- `load_questions(repository_id: str, repository_type: str) -> List[Dict]`
  Loads practice questions directly via `repository_id`.
