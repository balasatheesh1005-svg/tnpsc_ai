# TNPSC Nova AI — Identity Migration v1.0
## Phase 3 - Sprint 5: Revision Engine Migration Report

**Architect:** Lead Software Architect, TNPSC Nova AI  
**Date:** July 27, 2026  
**Status:** Implemented & Verified  
**Sprint Focus:** Revision Engine Migration (`core/revision_ai.py`) to UUID-based Database Identity  

---

## 1. Executive Summary

Following Phase 1 (Database Preparation), Phase 2 (Data Backfill & Test Cleanup), Phase 3 Sprint 1 (Authentication & Session), Phase 3 Sprint 2 (XP Engine), Phase 3 Sprint 3 (Progress Engine), and Phase 3 Sprint 4 (Weakness Engine), **Phase 3 - Sprint 5** converts the **Revision Engine** (`core/revision_ai.py`) from username-based database identity to UUID-based database identity (`user_id` referencing `public.profiles.id`).

### Key Accomplishments of Sprint 5
1. **100% UUID Database Queries**: All database read/write queries (`SELECT`, `INSERT`, `UPDATE`) targeting `public.user_revisions` filter and link strictly by `user_id` UUID.
2. **Zero Username Query Usage**: The `username` string is **NEVER** used as a database filter or match predicate in `user_revisions`.
3. **Preserved Business & UI Logic**: Revision scheduling, spaced repetition algorithms (levels 1-5, days interval mapping 1, 3, 7, 15, 30), revision queue, Smart Revision recommendations, dashboard revision cards, AI revision suggestions, and UI remain 100% identical.
4. **Data Integrity Auditing**: If an existing record contains `user_id IS NULL` or `user_id` fails resolution, the system logs a prominent warning (`[DATA INTEGRITY ALERT]`) and does **NOT** silently fall back to username filtering.
5. **Strict Scope Control**: No modifications were made to Authentication, Session, XP Engine, Progress Engine, Weakness Engine, Daily Mission, Mentor Memory, Bookmarks, Leaderboard, Analytics, Database Schemas, SQL, or RLS. `repository.py` was left untouched.

---

## 2. Architecture & Identity Resolution Flow

The Revision Engine resolves user identity dynamically via `_resolve_user_id(user_identifier)` before executing any database operation:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      REVISION ENGINE IDENTITY FLOW                     │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   Incoming Call: add_revision(user, topic) / get_due_revisions(user)   │
│                     │                                                  │
│                     ▼                                                  │
│   1. Invoke _resolve_user_id(user_identifier)                          │
│        - If user_identifier is 36-char UUID string -> Use directly     │
│        - If user_identifier matches session username -> Use session user_id│
│        - Fallback: Lookup profiles(id) UUID for username               │
│        - Default -> Return current_user_id() / st.session_state.user_id│
│                     │                                                  │
│                     ▼                                                  │
│   2. Execute Database Query on `public.user_revisions`:                │
│        - SELECT * FROM user_revisions WHERE user_id = :resolved_id     │
│        - INSERT INTO user_revisions (user_id, username, subject, ...)  │
│        - UPDATE user_revisions SET level = :lvl WHERE id = :row_id     │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Comprehensive Database Query Changes

All database operations targeting `public.user_revisions` have been migrated from username filtering to UUID filtering:

### Query 1: Add/Upsert Revision Record (`SELECT` + `INSERT`/`UPDATE`)
- **Old Query**:
  ```python
  supabase.table("user_revisions").upsert(
      {
          "username": user,
          "subject": subject,
          "topic": topic_name,
          "level": 1,
          "next_due": next_due.isoformat(),
      },
      on_conflict="username,subject,topic",
  ).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  existing = (
      supabase.table("user_revisions")
      .select("id")
      .eq("user_id", user_id)
      .eq("subject", subject)
      .eq("topic", topic_name)
      .limit(1)
      .execute()
  )
  if existing.data:
      supabase.table("user_revisions").update({
          "level": 1,
          "next_due": next_due.isoformat(),
      }).eq("id", existing.data[0]["id"]).execute()
  else:
      supabase.table("user_revisions").insert({
          "user_id": user_id,
          "username": display_username,  # Audit column only
          "subject": subject,
          "topic": topic_name,
          "level": 1,
          "next_due": next_due.isoformat(),
      }).execute()
  ```

### Query 2: Check Existing Topic in Revision Queue (`SELECT`)
- **Old Query**:
  ```python
  supabase.table("user_revisions").select("id").eq("username", user).eq("subject", subject).eq("topic", normalized_topic).limit(1).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  supabase.table("user_revisions").select("id").eq("user_id", user_id).eq("subject", subject).eq("topic", normalized_topic).limit(1).execute()
  ```

### Query 3: Update Revision Interval / Spaced Level (`SELECT` + `UPDATE`)
- **Old Query**:
  ```python
  supabase.table("user_revisions").select("*").eq("username", user).eq("subject", subject).eq("topic", topic).limit(1).execute()
  supabase.table("user_revisions").update({"level": level, "next_due": next_due.isoformat()}).eq("id", row["id"]).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  supabase.table("user_revisions").select("*").eq("user_id", user_id).eq("subject", subject).eq("topic", topic).limit(1).execute()
  supabase.table("user_revisions").update({"level": level, "next_due": next_due.isoformat()}).eq("id", row["id"]).execute()
  ```

### Query 4: Retrieve Due Revisions (`SELECT`)
- **Old Query**:
  ```python
  supabase.table("user_revisions").select("subject,topic,next_due").eq("username", user).lte("next_due", today).order("next_due").execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  supabase.table("user_revisions").select("subject,topic,next_due,user_id,id").eq("user_id", user_id).lte("next_due", today).order("next_due").execute()
  ```

### Query 5: Retrieve Revision Overview / Queue (`SELECT`)
- **Old Query**:
  ```python
  supabase.table("user_revisions").select("subject,topic,level,next_due").eq("username", user).order("next_due").execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  supabase.table("user_revisions").select("subject,topic,level,next_due,user_id,id").eq("user_id", user_id).order("next_due").execute()
  ```

---

## 4. Modified Files List

| File Path | Description of Changes |
| :--- | :--- |
| [`core/revision_ai.py`](file:///c:/Users/Home/Desktop/tnpsc_ai/core/revision_ai.py) | Added `_resolve_user_id()`, refactored `add_revision()`, `add_revision_topic()`, `update_revision()`, `get_due_revisions()`, `get_revision_topics()`, and `get_revision_overview()` to query strictly by `user_id` UUID. Added `[DATA INTEGRITY ALERT]` logging. |

---

## 5. Helper Functions Updated Summary

| Function Name | Updates Applied | Legacy Compatibility |
| :--- | :--- | :--- |
| `_resolve_user_id(user_identifier)` | **[NEW HELPER]** Resolves input parameter (UUID, username, or None) to authoritative UUID. | Guarantees DB operations execute strictly on `user_id`. |
| `add_revision(user, topic)` | Resolves `user_id` UUID. Filters SELECT by `user_id`. Inserts `user_id` identity column. | Accepts `username` or defaults to `session_state.user_id`. `username` string kept for audit. |
| `add_revision_topic(user, subject, topic, priority)` | Resolves `user_id` UUID. Filters SELECT by `user_id`. | Accepts `username` or defaults to `session_state.user_id`. |
| `update_revision(user, topic_key)` | Resolves `user_id` UUID. Filters SELECT by `user_id`. | Accepts `username` or defaults to `session_state.user_id`. |
| `get_due_revisions(user)` | Resolves `user_id` UUID. Queries DB via `.eq("user_id", user_id)`. Performs `NULL user_id` integrity check. | Signature preserves backward compatibility. |
| `get_revision_topics(user)` | Resolves `user_id` UUID. Queries DB via `.eq("user_id", user_id)`. Performs `NULL user_id` integrity check. | Signature preserves backward compatibility. |
| `get_revision_overview(user)` | Resolves `user_id` UUID. Queries DB via `.eq("user_id", user_id)`. Performs `NULL user_id` integrity check. | Signature preserves backward compatibility. |

---

## 6. Remaining Username Dependencies & Temporary Compatibility Code

### Temporary Compatibility Code
To ensure smooth migration without breaking callers passing legacy username strings during Phase 3, profile lookup fallback is retained:
```python
# TODO: Remove username compatibility after Sprint 8 Final Cleanup.
```
Location: `core/revision_ai.py` inside `_resolve_user_id()`.

### Approved Non-Database Username Usages
`username` is retained strictly for non-database operations:
1. **Audit Columns**: Populated in `user_revisions` `INSERT` payloads as a human-readable metadata column.
2. **Logs & Debug Messages**: Used in `logger.warning` / `logger.error` messages for troubleshooting.

---

## 7. Data Integrity Alert Rules

If `add_revision()`, `add_revision_topic()`, `update_revision()`, `get_due_revisions()`, `get_revision_topics()`, or `get_revision_overview()` cannot resolve `user_id`, or if a queried row contains `user_id IS NULL`, the system triggers an explicit log alert:
```
[DATA INTEGRITY ALERT] Unable to resolve user_id UUID for revision operation (input: ...)
[DATA INTEGRITY ALERT] Revision record id=... has user_id IS NULL!
```
The system does **NOT** silently fall back to querying by username string.

---

## 8. Testing & Verification Checklist

- [x] **Syntax Verification**: `python -m py_compile core/revision_ai.py` executed with zero errors.
- [x] **Full Integration Compilation**: `python -m py_compile` executed cleanly across all dependent modules (`revision_scheduler.py`, `test_revision.py`, `smart_selector.py`, `mentor_chat.py`, `mentor_ai.py`, `study_planner.py`, `ui/dashboard.py`, `app.py`).
- [x] **UUID SELECT Query Verification**: Confirmed `get_due_revisions()`, `get_revision_topics()`, `get_revision_overview()`, `update_revision()`, and `add_revision_topic()` filter by `.eq("user_id", user_id)`.
- [x] **UUID INSERT Query Verification**: Confirmed `add_revision()` includes `"user_id": user_id` in insertion payload.
- [x] **Data Integrity Logging**: Verified `[DATA INTEGRITY ALERT]` logs for missing or NULL `user_id`.
- [x] **Zero Touch Scope Check**: Confirmed no modifications were made to Authentication, Session, XP Engine, Progress Engine, Weakness Engine, Daily Mission, Mentor Memory, Bookmarks, Leaderboard, Analytics, or `repository.py`.
