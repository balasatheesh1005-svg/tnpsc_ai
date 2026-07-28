# TNPSC Nova AI — Identity Migration v1.0
## Phase 3 - Sprint 2: XP Engine Migration Report

**Architect:** Lead Software Architect, TNPSC Nova AI  
**Date:** July 26, 2026  
**Status:** Implemented & Verified  
**Sprint Focus:** XP Engine Migration (`core/xp_ai.py`) to UUID-based Database Identity  

---

## 1. Executive Summary

Phase 1 (Database Preparation), Phase 2 (Data Backfill & Test Cleanup), and Phase 3 Sprint 1 (Authentication & Session Refactor) established the dual-identity foundation.

In **Phase 3 - Sprint 2**, the **XP Engine** (`core/xp_ai.py`) has been fully migrated from legacy username-based database identity to UUID-based database identity (`user_id` referencing `public.profiles.id`).

### Key Accomplishments of Sprint 2
1. **100% UUID Database Queries**: Every database read/write operation (`SELECT`, `INSERT`, `UPDATE`) in `user_xp` now queries strictly by `user_id`.
2. **Zero Username Query Usage**: `username` string is **NEVER** used as a database filter or match predicate in `user_xp`.
3. **Preserved Business & Display Logic**: XP calculations (`get_level_from_xp`), level progression thresholds (`LEVEL_THRESHOLDS`), XP reward allocations (`XP_REWARDS`), and achievement rules remain 100% unchanged.
4. **Data Integrity Auditing**: If an old record contains `user_id IS NULL`, the system logs a prominent warning (`[DATA INTEGRITY ALERT]`) and does **NOT** silently fall back to username filtering.
5. **Zero Module Drift**: No alterations were made to Authentication, Session, Progress, Weakness, Revision, Daily Mission, Mentor Memory, Dashboard, Leaderboard, Analytics, or Database SQL schemas.

---

## 2. Architecture & Identity Resolution Flow

The XP Engine resolves user identity dynamically via `_resolve_user_id(user_identifier)` before any database interaction:

```
┌────────────────────────────────────────────────────────────────────────┐
┌                         XP ENGINE IDENTITY FLOW                        │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   Incoming Call: get_user_xp(user_id=None) / add_xp(user_id=None, ...) │
│                     │                                                  │
│                     ▼                                                  │
│   1. Invoke _resolve_user_id(user_identifier)                          │
│        - If user_identifier is 36-char UUID string -> Use directly     │
│        - If user_identifier matches session username -> Use session user_id │
│        - If user_identifier is username -> Lookup profiles(id) UUID    │
│        - Default -> Return current_user_id() / st.session_state.user_id│
│                     │                                                  │
│                     ▼                                                  │
│   2. Execute Database Query on `public.user_xp`:                        │
│        - SELECT ... WHERE user_id = :resolved_id                       │
│        - INSERT ... (user_id, username, xp, level)                     │
│        - UPDATE ... WHERE user_id = :resolved_id                       │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Comprehensive Database Query Changes

All database operations in `core/xp_ai.py` have been refactored:

### Query 1: Ensure User XP Record (SELECT)
- **Old Query**:
  ```python
  supabase.table("user_xp").select("*").eq("username", username).execute()
  ```
- **New Query**:
  ```python
  supabase.table("user_xp").select("id, user_id, username, xp, level").eq("user_id", user_id).execute()
  ```

### Query 2: Ensure User XP Record (INSERT)
- **Old Query**:
  ```python
  supabase.table("user_xp").insert({"username": username, "xp": 0, "level": 1}).execute()
  ```
- **New Query**:
  ```python
  supabase.table("user_xp").insert({
      "user_id": user_id,
      "username": username or current_username() or "",
      "xp": 0,
      "level": 1
  }).execute()
  ```

### Query 3: Retrieve User XP (SELECT)
- **Old Query**:
  ```python
  supabase.table("user_xp").select("xp, level").eq("username", username).limit(1).execute()
  ```
- **New Query**:
  ```python
  supabase.table("user_xp").select("xp, level, user_id").eq("user_id", resolved_id).limit(1).execute()
  ```

### Query 4: Award User XP (UPDATE)
- **Old Query**:
  ```python
  supabase.table("user_xp").update({"xp": new_xp, "level": new_level}).eq("username", username).execute()
  ```
- **New Query**:
  ```python
  supabase.table("user_xp").update({"xp": new_xp, "level": new_level}).eq("user_id", resolved_id).execute()
  ```

---

## 4. Helper Functions Update Summary

| Function Name | Updates Applied | Legacy Compatibility |
| :--- | :--- | :--- |
| `_resolve_user_id(user_identifier)` | **[NEW HELPER]** Resolves user parameter (UUID, username, or None) to authoritative UUID. | Guarantees DB operations run strictly on `user_id`. |
| `_ensure_user_xp_record(user_id, username=None)` | Changed filter parameter from `username` to `user_id`. Includes data integrity check for `NULL user_id`. | Inserts both `user_id` and display `username`. |
| `get_user_xp(user_id=None)` | Refactored parameter to default to `None` (session `user_id`). Queries DB strictly by `user_id`. | Signature preserves backward compatible calls. |
| `add_xp(user_id=None, amount=0, reward_type=None)` | Refactored DB read/write queries to use `user_id` UUID. | Returns identical result dictionary for callers. |
| `get_level(user_id=None)` | Delegates to `get_user_xp(user_id)`. | Accepts `user_id` or session default. |
| `get_next_level_target(user_id=None)` | Delegates to `get_user_xp(user_id)`. | Accepts `user_id` or session default. |
| `get_level_progress(user_id=None)` | Delegates to `get_user_xp(user_id)`. | Accepts `user_id` or session default. |
| `is_achievement_unlocked(user_id=None, achievement_type=None)` | Delegates to `get_level(user_id)`. | Accepts `user_id` or session default. |

---

## 5. Backward Compatibility & Data Integrity Rules

1. **No Silent Fallbacks**: If a query encounters a row in `public.user_xp` with `user_id IS NULL`, it triggers a system log warning (`[DATA INTEGRITY ALERT]`). It does **NOT** fall back to querying by `username`.
2. **Display Username Retention**: `username` is preserved in INSERT payloads to maintain human-readable audit columns in Supabase, but is never used for querying or filtering.
3. **Session Integration**: Callers from UI and other modules can call XP functions without arguments (e.g. `get_user_xp()`) and automatically query using `st.session_state.user_id`.

---

## 6. Testing & Verification Checklist

- [x] **Syntax & Module Compilation**: Verified `core/xp_ai.py` syntax and imports cleanly.
- [x] **UUID SELECT Query Verification**: Confirmed `get_user_xp` executes `.eq("user_id", resolved_id)`.
- [x] **UUID INSERT Query Verification**: Confirmed `_ensure_user_xp_record` populates `user_id` column.
- [x] **UUID UPDATE Query Verification**: Confirmed `add_xp` executes `.eq("user_id", resolved_id)`.
- [x] **XP Calculation Integrity**: Verified `LEVEL_THRESHOLDS` and `get_level_from_xp` remain untouched.
- [x] **Zero Touch Scope Check**: Verified no files outside `core/xp_ai.py` were modified.
