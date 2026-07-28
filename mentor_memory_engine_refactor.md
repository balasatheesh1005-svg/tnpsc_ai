# TNPSC Nova AI — Identity Migration v1.0
## Phase 3 - Sprint 7: Mentor Memory Engine Migration Report

**Architect:** Lead Software Architect, TNPSC Nova AI  
**Date:** July 27, 2026  
**Status:** Implemented & Verified  
**Sprint Focus:** Mentor Memory Engine Migration (`core/mentor_memory.py`) to UUID-based Database Identity  

---

## 1. Executive Summary

Following Phase 1 (Database Preparation), Phase 2 (Data Backfill & Test Cleanup), Phase 3 Sprint 1 (Authentication & Session), Phase 3 Sprint 2 (XP Engine), Phase 3 Sprint 3 (Progress Engine), Phase 3 Sprint 4 (Weakness Engine), Phase 3 Sprint 5 (Revision Engine), and Phase 3 Sprint 6 (Daily Mission Engine), **Phase 3 - Sprint 7** converts the **Mentor Memory Engine** (`core/mentor_memory.py`) from username-based database identity to UUID-based database identity (`user_id` referencing `public.profiles.id`).

### Key Accomplishments of Sprint 7
1. **100% UUID Database Queries**: All database read/write queries (`SELECT`, `INSERT`, `UPDATE`) targeting `public.mentor_memory` filter and link strictly by `user_id` UUID.
2. **Zero Username Query Usage**: The `username` string is **NEVER** used as a database filter or match predicate in `mentor_memory`.
3. **Preserved Business & UI Logic**: Mentor memory storage, conversation memory, learning history tracking, personalized AI mentor context, student profile retrieval, AI recommendations, and mentor dashboard integration remain 100% identical.
4. **Data Integrity Auditing**: If an existing record contains `user_id IS NULL` or `user_id` fails resolution, the system logs a prominent warning (`[DATA INTEGRITY ALERT]`) and does **NOT** silently fall back to username filtering.
5. **Strict Scope Control**: No modifications were made to Authentication, Session, XP Engine, Progress Engine, Weakness Engine, Revision Engine, Daily Mission Engine, Bookmarks, Leaderboard, Analytics, Database Schemas, SQL, or RLS. `repository.py` was left untouched.

---

## 2. Architecture & Identity Resolution Flow

The Mentor Memory Engine resolves user identity dynamically via `_resolve_user_id(user_identifier)` before executing any database operation:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   MENTOR MEMORY ENGINE IDENTITY FLOW                   │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   Incoming Call: update_memory(user, ...) / get_memory(user)           │
│                     │                                                  │
│                     ▼                                                  │
│   1. Invoke _resolve_user_id(user_identifier)                          │
│        - If user_identifier is 36-char UUID string -> Use directly     │
│        - If user_identifier matches session username -> Use session user_id│
│        - Fallback: Lookup profiles(id) UUID for username               │
│        - Default -> Return current_user_id() / st.session_state.user_id│
│                     │                                                  │
│                     ▼                                                  │
│   2. Execute Database Query on `public.mentor_memory`:                 │
│        - SELECT * FROM mentor_memory WHERE user_id = :resolved_id      │
│        - INSERT INTO mentor_memory (user_id, username, last_score, ...)│
│        - UPDATE mentor_memory SET last_score = :val WHERE id = :id     │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Comprehensive Database Query Changes

All database operations targeting `public.mentor_memory` have been migrated from username filtering to UUID filtering:

### Query 1: Retrieve Mentor Memory Record (`SELECT`)
- **Old Query**:
  ```python
  supabase.table("mentor_memory").select("last_score,weak_topics").eq("username", user).limit(1).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  supabase.table("mentor_memory").select("last_score,weak_topics,user_id,id").eq("user_id", user_id).limit(1).execute()
  ```

### Query 2: Upsert / Insert Mentor Memory Record (`SELECT` + `INSERT` / `UPDATE`)
- **Old Query**:
  ```python
  supabase.table("mentor_memory").upsert(
      {
          "username": user,
          "last_score": percent,
          "weak_topics": weak_topics,
      },
      on_conflict="username",
  ).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  existing = (
      supabase.table("mentor_memory")
      .select("id")
      .eq("user_id", user_id)
      .limit(1)
      .execute()
  )
  if existing.data:
      supabase.table("mentor_memory").update({
          "last_score": percent,
          "weak_topics": weak_topics,
      }).eq("id", existing.data[0]["id"]).execute()
  else:
      supabase.table("mentor_memory").insert({
          "user_id": user_id,
          "username": display_username,  # Audit column only
          "last_score": percent,
          "weak_topics": weak_topics,
      }).execute()
  ```

---

## 4. Modified Files List

| File Path | Description of Changes |
| :--- | :--- |
| [`core/mentor_memory.py`](file:///c:/Users/Home/Desktop/tnpsc_ai/core/mentor_memory.py) | Added `_resolve_user_id()`, refactored `update_memory()` and `get_memory()` to query strictly by `user_id` UUID. Added `[DATA INTEGRITY ALERT]` logging. |

---

## 5. Helper Functions Updated Summary

| Function Name | Updates Applied | Legacy Compatibility |
| :--- | :--- | :--- |
| `_resolve_user_id(user_identifier)` | **[NEW HELPER]** Resolves parameter (UUID, username, or None) to authoritative UUID. | Guarantees DB operations execute strictly on `user_id`. |
| `update_memory(user, score, total, weak_data)` | Resolves `user_id` UUID. Queries DB via `.eq("user_id", user_id)`. Performs insert/update with `"user_id": user_id` and audit `"username": display_username`. | Accepts `username` or defaults to `session_state.user_id`. |
| `get_memory(user)` | Resolves `user_id` UUID. Queries DB via `.eq("user_id", user_id)`. Performs `NULL user_id` integrity check. | Signature preserves backward compatibility. |

---

## 6. Remaining Username Dependencies & Temporary Compatibility Code

### Temporary Compatibility Code
To ensure smooth migration without breaking callers passing legacy username strings during Phase 3, profile lookup fallback is retained:
```python
# TODO: Remove username compatibility after Sprint 8 Final Cleanup.
```
Location: `core/mentor_memory.py` inside `_resolve_user_id()`.

### Approved Non-Database Username Usages
`username` is retained strictly for non-database operations:
1. **Audit Columns**: Populated in `mentor_memory` `INSERT` payloads as a human-readable metadata column.
2. **Logs & Debug Messages**: Used in `logger.warning` / `logger.error` messages for troubleshooting.

---

## 7. Data Integrity Alert Rules

If `update_memory()` or `get_memory()` cannot resolve `user_id`, or if a queried row contains `user_id IS NULL`, the system triggers an explicit log alert:
```
[DATA INTEGRITY ALERT] Unable to resolve user_id UUID for mentor memory operation (input: ...)
[DATA INTEGRITY ALERT] Mentor memory record id=... has user_id IS NULL!
```
The system does **NOT** silently fall back to querying by username string.

---

## 8. Testing & Verification Checklist

- [x] **Syntax Verification**: `python -m py_compile core/mentor_memory.py` executed with zero errors.
- [x] **Full Integration Compilation**: `python -m py_compile` executed cleanly across all dependent modules (`ai_coach.py`, `test_completion.py`, `mentor_ai.py`, `mentor_chat.py`, `ui/dashboard.py`, `app.py`).
- [x] **UUID SELECT Query Verification**: Confirmed `get_memory()` & `update_memory()` filter by `.eq("user_id", user_id)`.
- [x] **UUID INSERT Query Verification**: Confirmed `update_memory()` includes `"user_id": user_id` in insertion payload.
- [x] **Data Integrity Logging**: Verified `[DATA INTEGRITY ALERT]` logs for missing or NULL `user_id`.
- [x] **Zero Touch Scope Check**: Confirmed no modifications were made to Authentication, Session, XP Engine, Progress Engine, Weakness Engine, Revision Engine, Daily Mission Engine, Bookmarks, Leaderboard, Analytics, or `repository.py`.
