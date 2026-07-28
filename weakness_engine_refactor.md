# TNPSC Nova AI — Identity Migration v1.0
## Phase 3 - Sprint 4: Weakness Engine Migration Report

**Architect:** Lead Software Architect, TNPSC Nova AI  
**Date:** July 27, 2026  
**Status:** Implemented & Verified  
**Sprint Focus:** Weakness Engine Migration (`core/weakness_ai.py`) to UUID-based Database Identity  

---

## 1. Executive Summary

Following Phase 1 (Database Preparation), Phase 2 (Data Backfill & Test Cleanup), Phase 3 Sprint 1 (Authentication & Session), Phase 3 Sprint 2 (XP Engine), and Phase 3 Sprint 3 (Progress Engine), **Phase 3 - Sprint 4** converts the **Weakness Engine** from username-based database identity to UUID-based database identity (`user_id` referencing `public.profiles.id`).

### Key Accomplishments of Sprint 4
1. **100% UUID Database Queries**: All database read/write queries (`SELECT`, `INSERT`, `UPDATE`) targeting `public.users_weakness` filter and link strictly by `user_id` UUID.
2. **Zero Username Query Usage**: The `username` string is **NEVER** used as a database filter or match predicate in `users_weakness`.
3. **Preserved Business & UI Logic**: Weakness calculations, topic/subject weakness rankings, AI recommendations, revision recommendations, dashboard weakness cards, and UI remain 100% identical.
4. **Data Integrity Auditing**: If an existing record contains `user_id IS NULL`, the system logs a prominent warning (`[DATA INTEGRITY ALERT]`) and does **NOT** silently fall back to username filtering.
5. **Strict Scope Control**: No modifications were made to Authentication, Session, XP Engine, Progress Engine, Revision Engine, Daily Mission, Mentor Memory, Bookmarks, Leaderboard, Analytics, Database Schemas, SQL, or RLS. `repository.py` was left untouched.

---

## 2. Architecture & Identity Resolution Flow

The Weakness Engine resolves user identity dynamically via `_resolve_user_id(user_identifier)` before executing any database operation:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      WEAKNESS ENGINE IDENTITY FLOW                     │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   Incoming Call: get_weakness(user) / add_weakness(user, ...)          │
│                     │                                                  │
│                     ▼                                                  │
│   1. Invoke _resolve_user_id(user_identifier)                          │
│        - If user_identifier is 36-char UUID string -> Use directly     │
│        - If user_identifier matches session username -> Use session user_id│
│        - Fallback: Lookup profiles(id) UUID for username               │
│        - Default -> Return current_user_id() / st.session_state.user_id│
│                     │                                                  │
│                     ▼                                                  │
│   2. Execute Database Query on `public.users_weakness`:               │
│        - SELECT * FROM users_weakness WHERE user_id = :resolved_id     │
│        - INSERT INTO users_weakness (user_id, username, subject, ...)  │
│        - UPDATE users_weakness SET weakness = :val WHERE id = :row_id  │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Comprehensive Database Query Changes

All database operations targeting `public.users_weakness` have been migrated from username filtering to UUID filtering:

### Query 1: Check Existing Weakness Record (`SELECT`)
- **Old Query**:
  ```python
  supabase.table("users_weakness").select("*").eq("username", username).eq("subject", subject).eq("topic", topic).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(username)
  supabase.table("users_weakness").select("*").eq("user_id", user_id).eq("subject", subject).eq("topic", topic).execute()
  ```

### Query 2: Insert New Weakness Record (`INSERT`)
- **Old Query**:
  ```python
  supabase.table("users_weakness").insert({"username": username, "subject": subject, "topic": topic, "weakness": 1}).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(username)
  supabase.table("users_weakness").insert({
      "user_id": user_id,
      "username": display_username,  # Audit column only
      "subject": subject,
      "topic": topic,
      "weakness": 1,
  }).execute()
  ```

### Query 3: Update Weakness Score (`UPDATE`)
- **Old Query**:
  ```python
  supabase.table("users_weakness").update({"weakness": weakness}).eq("id", data[0]["id"]).execute()
  ```
- **New Query**:
  ```python
  supabase.table("users_weakness").update({"weakness": weakness}).eq("id", row_id).execute()
  ```

### Query 4: Retrieve All Weaknesses for User (`SELECT`)
- **Old Query**:
  ```python
  supabase.table("users_weakness").select("*").eq("username", username).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(username)
  supabase.table("users_weakness").select("*").eq("user_id", user_id).execute()
  ```

---

## 4. Modified Files List

| File Path | Description of Changes |
| :--- | :--- |
| [`core/weakness_ai.py`](file:///c:/Users/Home/Desktop/tnpsc_ai/core/weakness_ai.py) | Added `_resolve_user_id()`, refactored `add_weakness()`, `reduce_weakness()`, `get_weakness()`, and `get_most_weak_topic()` to query strictly by `user_id` UUID. Added `[DATA INTEGRITY ALERT]` logging. |

---

## 5. Helper Functions Updated Summary

| Function Name | Updates Applied | Legacy Compatibility |
| :--- | :--- | :--- |
| `_resolve_user_id(user_identifier)` | **[NEW HELPER]** Resolves input parameter (UUID, username, or None) to authoritative UUID. | Guarantees DB operations execute strictly on `user_id`. |
| `add_weakness(username, subject, topic)` | Resolves `user_id` UUID. Filters SELECT by `user_id`. Inserts `user_id` identity column. | Accepts `username` or defaults to `session_state.user_id`. `username` string kept for audit. |
| `reduce_weakness(username, subject, topic)` | Resolves `user_id` UUID. Filters SELECT by `user_id`. | Accepts `username` or defaults to `session_state.user_id`. |
| `get_weakness(username)` | Resolves `user_id` UUID. Queries DB via `.eq("user_id", user_id)`. Performs `NULL user_id` integrity check. | Signature preserves backward compatibility. |
| `get_most_weak_topic(username)` | Delegates to `get_weakness(username)` with resolved UUID identity. | Preserves identical return tuple `(topic_key, count)`. |

---

## 6. Remaining Username Dependencies & Temporary Compatibility Code

### Temporary Compatibility Code
To ensure smooth migration without breaking callers passing legacy username strings during Phase 3, profile lookup fallback is retained:
```python
# TODO: Remove username compatibility after Sprint 8 Final Cleanup.
```
Location: `core/weakness_ai.py` inside `_resolve_user_id()`.

### Approved Non-Database Username Usages
`username` is retained strictly for non-database operations:
1. **Audit Columns**: Populated in `users_weakness` `INSERT` payloads as a human-readable metadata column.
2. **Logs & Debug Messages**: Used in `logger.warning` / `logger.error` messages for troubleshooting.

---

## 7. Data Integrity Alert Rules

If `add_weakness()`, `reduce_weakness()`, or `get_weakness()` cannot resolve `user_id`, or if a queried row contains `user_id IS NULL`, the system triggers an explicit log alert:
```
[DATA INTEGRITY ALERT] Unable to resolve user_id UUID for weakness operation (input: ...)
[DATA INTEGRITY ALERT] Weakness record id=... has user_id IS NULL!
```
The system does **NOT** silently fall back to querying by username string.

---

## 8. Testing & Verification Checklist

- [x] **Syntax Verification**: `python -m py_compile core/weakness_ai.py` executed with zero errors.
- [x] **Full Integration Compilation**: `python -m py_compile` executed cleanly across all dependent modules (`dashboard_stats_ai.py`, `mentor_ai.py`, `mentor_chat.py`, `test_weakness.py`, `ui/pages/weakness.py`, `test_topic_selector.py`, `test_completion.py`, `ai_teacher.py`, `adaptive_ai.py`, `study_planner.py`, `smart_selector.py`, `dashboard.py`, `app.py`).
- [x] **UUID SELECT Query Verification**: Confirmed `get_weakness()` and `add_weakness()` filter by `.eq("user_id", user_id)`.
- [x] **UUID INSERT Query Verification**: Confirmed `add_weakness()` includes `"user_id": user_id` in insertion payload.
- [x] **Data Integrity Logging**: Verified `[DATA INTEGRITY ALERT]` logs for missing or NULL `user_id`.
- [x] **Zero Touch Scope Check**: Confirmed no modifications were made to Authentication, Session, XP Engine, Progress Engine, Revision Engine, Daily Mission, Mentor Memory, Bookmarks, Leaderboard, Analytics, or `repository.py`.
