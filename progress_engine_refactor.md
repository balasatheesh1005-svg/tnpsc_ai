# TNPSC Nova AI — Identity Migration v1.0
## Phase 3 - Sprint 3: Progress Engine Migration Report

**Architect:** Lead Software Architect, TNPSC Nova AI  
**Date:** July 27, 2026  
**Status:** Implemented & Verified  
**Sprint Focus:** Progress Engine Migration (`core/progress_ai.py` & `core/dashboard_stats_ai.py`) to UUID-based Database Identity  

---

## 1. Executive Summary

Following Phase 1 (Database Preparation), Phase 2 (Data Backfill & Test Cleanup), Phase 3 Sprint 1 (Authentication & Session), and Phase 3 Sprint 2 (XP Engine), **Phase 3 - Sprint 3** converts the **Progress Engine** from username-based identity to UUID-based identity (`user_id` referencing `public.profiles.id`).

### Key Accomplishments of Sprint 3
1. **100% UUID Database Queries**: All database read/write queries (`SELECT`, `INSERT`) targeting `public.users_progress` filter and link strictly by `user_id` UUID.
2. **Zero Username Query Usage**: The `username` string is **NEVER** used as a database filter or match predicate in `users_progress`.
3. **Preserved Business & UI Logic**: Progress calculation, subject/topic accuracy percentages, dashboard trend charts, progress breakdown tables, and metrics remain 100% identical.
4. **Data Integrity Auditing**: If an existing record contains `user_id IS NULL`, the system logs a prominent warning (`[DATA INTEGRITY ALERT]`) and does **NOT** silently fall back to username filtering.
5. **Strict Scope Control**: No modifications were made to Authentication, Session, XP Engine, Weakness Engine, Revision Engine, Daily Mission, Mentor Memory, Bookmarks, Leaderboard, Analytics, Database Schemas, SQL, or RLS. `core/question_engine/repository.py` was left untouched as it handles local JSON/file storage.

---

## 2. Architecture & Identity Resolution Flow

The Progress Engine resolves user identity dynamically via `_resolve_user_id(user_identifier)` before executing any database operation:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      PROGRESS ENGINE IDENTITY FLOW                     │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   Incoming Call: get_progress(user=None) / save_progress(user=None,...)│
│                     │                                                  │
│                     ▼                                                  │
│   1. Invoke _resolve_user_id(user_identifier)                          │
│        - If user_identifier is 36-char UUID string -> Use directly     │
│        - If user_identifier matches session username -> Use session user_id│
│        - Fallback: Lookup profiles(id) UUID for username               │
│        - Default -> Return current_user_id() / st.session_state.user_id│
│                     │                                                  │
│                     ▼                                                  │
│   2. Execute Database Query on `public.users_progress`:               │
│        - SELECT * FROM users_progress WHERE user_id = :resolved_id     │
│        - INSERT INTO users_progress (user_id, username, subject, ...) │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Comprehensive Database Query Changes

All database operations targeting `public.users_progress` have been migrated from username filtering to UUID filtering:

### Query 1: Retrieve User Progress (SELECT)
- **Old Query**:
  ```python
  supabase.table("users_progress").select("*").eq("username", user).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  supabase.table("users_progress").select("*").eq("user_id", user_id).execute()
  ```

### Query 2: Save User Progress (INSERT)
- **Old Query**:
  ```python
  data = {
      "username": user,
      "subject": subj,
      "topic": r_id,
      "accuracy": accuracy,
  }
  supabase.table("users_progress").insert(data).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  data = {
      "user_id": user_id,
      "username": display_username,  # Audit column only
      "subject": subj,
      "topic": r_id,
      "accuracy": accuracy,
  }
  supabase.table("users_progress").insert(data).execute()
  ```

### Query 3: Dashboard User Progress Aggregation (SELECT)
- **Old Query**:
  ```python
  progress_response = supabase.table("users_progress").select("username, accuracy").execute()
  all_progress = progress_response.data or []
  user_progress = [row for row in all_progress if row.get("username") == user]
  ```
- **New Query**:
  ```python
  user_progress = get_progress(user)  # Queries users_progress by user_id UUID
  ```

---

## 4. Modified Files List

| File Path | Description of Changes |
| :--- | :--- |
| [`core/progress_ai.py`](file:///c:/Users/Home/Desktop/tnpsc_ai/core/progress_ai.py) | Added `_resolve_user_id()`, refactored `save_progress()` and `get_progress()` to query strictly by `user_id` UUID, and added `[DATA INTEGRITY ALERT]` logging. |
| [`core/dashboard_stats_ai.py`](file:///c:/Users/Home/Desktop/tnpsc_ai/core/dashboard_stats_ai.py) | Refactored `get_dashboard_stats()` to use `get_progress(user)` for UUID-based progress fetching instead of filtering by username string. |

---

## 5. Helper Functions Updated Summary

| Function Name | Updates Applied | Legacy Compatibility |
| :--- | :--- | :--- |
| `_resolve_user_id(user_identifier)` | **[NEW HELPER]** Resolves input parameter (UUID, username, or None) to authoritative UUID. | Guarantees DB operations execute strictly on `user_id`. |
| `save_progress(user, subject, topic, accuracy, topic_id, repository_id)` | Resolves `user_id` UUID. Populates `user_id` identity column. | Accepts `user` or defaults to `session_state.user_id`. `username` retained for audit. |
| `get_progress(user)` | Resolves `user_id` UUID. Queries DB via `.eq("user_id", user_id)`. Performs `NULL user_id` integrity check. | Signature preserves backward compatibility. |
| `get_dashboard_stats(user)` | Calls `get_progress(user)` to retrieve user progress records via `user_id` UUID. | Returns identical metrics structure for dashboard cards. |

---

## 6. Remaining Username Dependencies & Temporary Compatibility Code

### Temporary Compatibility Code
To ensure smooth migration without breaking existing sessions or callers passing legacy username strings during Phase 3, profile lookup fallback is retained:
```python
# TODO: Remove username compatibility after Sprint 8 Final Cleanup.
```
Location: `core/progress_ai.py` in `_resolve_user_id()` function.

### Approved Non-Database Username Usages
`username` is retained strictly for non-database operations:
1. **Display**: Greeting banners and dashboard headers.
2. **Audit Columns**: Preserved as a metadata column in `users_progress` `INSERT` payloads for database inspection.
3. **Logs & Debug Messages**: Used in `logger.warning` / `logger.error` messages for troubleshooting.

---

## 7. Data Integrity Alert Rules

If `save_progress()` or `get_progress()` cannot resolve `user_id`, or if a queried row contains `user_id IS NULL`, the system triggers an explicit log alert:
```
[DATA INTEGRITY ALERT] Unable to resolve user_id UUID for progress operation (input: ...)
[DATA INTEGRITY ALERT] Progress record id=... has user_id IS NULL!
```
The system does **NOT** silently fall back to querying by username string.

---

## 8. Testing & Verification Checklist

- [x] **Syntax Verification**: `python -m py_compile core/progress_ai.py` executed with zero errors.
- [x] **Dependent Module Verification**: Compiled all dependent modules (`dashboard_stats_ai.py`, `practice_session.py`, `test_completion.py`, `progress.py`, `dashboard.py`, `mentor_ai.py`, `mentor_chat.py`, `app.py`) with zero syntax/import errors.
- [x] **UUID SELECT Query**: Verified `get_progress()` filters by `.eq("user_id", user_id)`.
- [x] **UUID INSERT Query**: Verified `save_progress()` includes `"user_id": user_id` in insertion payload.
- [x] **Data Integrity Logging**: Verified `[DATA INTEGRITY ALERT]` logs for missing `user_id`.
- [x] **Zero Touch Scope Check**: Confirmed no modifications were made to Authentication, Session, XP Engine, Weakness Engine, Revision Engine, Daily Mission, Mentor Memory, Bookmarks, Leaderboard, Analytics, or `repository.py`.
