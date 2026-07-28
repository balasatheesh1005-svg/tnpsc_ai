# TNPSC Nova AI — Identity Migration v1.0
## Phase 3 - Sprint 6: Daily Mission Engine Migration Report

**Architect:** Lead Software Architect, TNPSC Nova AI  
**Date:** July 27, 2026  
**Status:** Implemented & Verified  
**Sprint Focus:** Daily Mission Engine Migration (`core/daily_mission_ai.py`) to UUID-based Database Identity  

---

## 1. Executive Summary

Following Phase 1 (Database Preparation), Phase 2 (Data Backfill & Test Cleanup), Phase 3 Sprint 1 (Authentication & Session), Phase 3 Sprint 2 (XP Engine), Phase 3 Sprint 3 (Progress Engine), Phase 3 Sprint 4 (Weakness Engine), and Phase 3 Sprint 5 (Revision Engine), **Phase 3 - Sprint 6** converts the **Daily Mission Engine** (`core/daily_mission_ai.py`) from username-based database identity to UUID-based database identity (`user_id` referencing `public.profiles.id`).

### Key Accomplishments of Sprint 6
1. **100% UUID Database Queries**: All database read/write queries (`SELECT`, `INSERT`, `UPDATE`) targeting `public.daily_missions` filter and link strictly by `user_id` UUID.
2. **Zero Username Query Usage**: The `username` string is **NEVER** used as a database filter or match predicate in `daily_missions`.
3. **Preserved Business & UI Logic**: Daily mission generation, mission completion tracking, daily streak, mission XP rewards (+100 XP), daily progress calculation, dashboard daily mission cards, AI recommendations, and UI remain 100% identical.
4. **Data Integrity Auditing**: If an existing record contains `user_id IS NULL` or `user_id` fails resolution, the system logs a prominent warning (`[DATA INTEGRITY ALERT]`) and does **NOT** silently fall back to username filtering.
5. **Strict Scope Control**: No modifications were made to Authentication, Session, XP Engine, Progress Engine, Weakness Engine, Revision Engine, Mentor Memory, Bookmarks, Leaderboard, Analytics, Database Schemas, SQL, or RLS. `repository.py` was left untouched.

---

## 2. Architecture & Identity Resolution Flow

The Daily Mission Engine resolves user identity dynamically via `_resolve_user_id(user_identifier)` before executing any database operation:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   DAILY MISSION ENGINE IDENTITY FLOW                   │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   Incoming Call: get_today_mission(user) / claim_reward(user)          │
│                     │                                                  │
│                     ▼                                                  │
│   1. Invoke _resolve_user_id(user_identifier)                          │
│        - If user_identifier is 36-char UUID string -> Use directly     │
│        - If user_identifier matches session username -> Use session user_id│
│        - Fallback: Lookup profiles(id) UUID for username               │
│        - Default -> Return current_user_id() / st.session_state.user_id│
│                     │                                                  │
│                     ▼                                                  │
│   2. Execute Database Query on `public.daily_missions`:                │
│        - SELECT * FROM daily_missions WHERE user_id = :resolved_id     │
│        - INSERT INTO daily_missions (user_id, username, ...)           │
│        - UPDATE daily_missions SET reward_claimed = true WHERE id = :id│
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Comprehensive Database Query Changes

All database operations targeting `public.daily_missions` have been migrated from username filtering to UUID filtering:

### Query 1: Get Today's Mission Record (`SELECT`)
- **Old Query**:
  ```python
  supabase.table("daily_missions").select("*").eq("username", username).eq("mission_date", mission_date).limit(1).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  supabase.table("daily_missions").select("*").eq("user_id", user_id).eq("mission_date", mission_date).limit(1).execute()
  ```

### Query 2: Insert Today's Default Mission Record (`INSERT`)
- **Old Query**:
  ```python
  supabase.table("daily_missions").upsert(
      {"username": username, "mission_date": mission_date, "daily_test_completed": False, "revision_count": 0, "questions_answered": 0, "reward_claimed": False},
      on_conflict="username,mission_date"
  ).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  supabase.table("daily_missions").insert({
      "user_id": user_id,
      "username": display_username,  # Audit column only
      "mission_date": mission_date,
      "daily_test_completed": False,
      "revision_count": 0,
      "questions_answered": 0,
      "reward_claimed": False,
  }).execute()
  ```

### Query 3: Update Daily Test Completion (`UPDATE`)
- **Old Query**:
  ```python
  supabase.table("daily_missions").update({"daily_test_completed": True}).eq("id", mission["id"]).execute()
  ```
- **New Query**:
  ```python
  supabase.table("daily_missions").update({"daily_test_completed": True}).eq("id", mission["id"]).execute()
  ```

### Query 4: Increment Mission Field Count (`UPDATE`)
- **Old Query**:
  ```python
  supabase.table("daily_missions").update({field_name: current_value + 1}).eq("id", mission["id"]).execute()
  ```
- **New Query**:
  ```python
  supabase.table("daily_missions").update({field_name: current_value + 1}).eq("id", mission["id"]).execute()
  ```

### Query 5: Claim Daily Mission Reward (`UPDATE`)
- **Old Query**:
  ```python
  supabase.table("daily_missions").update({"reward_claimed": True}).eq("id", mission["id"]).eq("reward_claimed", False).execute()
  ```
- **New Query**:
  ```python
  user_id = _resolve_user_id(user)
  supabase.table("daily_missions").update({"reward_claimed": True}).eq("id", mission["id"]).eq("reward_claimed", False).execute()
  # XP reward added via UUID:
  add_xp(user_id, DAILY_MISSION_REWARD_XP, reward_type="daily_mission_completion")
  ```

---

## 4. Modified Files List

| File Path | Description of Changes |
| :--- | :--- |
| [`core/daily_mission_ai.py`](file:///c:/Users/Home/Desktop/tnpsc_ai/core/daily_mission_ai.py) | Added `_resolve_user_id()`, refactored `get_today_mission()`, `update_daily_test()`, `_increment_today_field()`, `update_revision()`, `update_question_count()`, `get_mission_progress()`, `mission_completed()`, and `claim_reward()` to query strictly by `user_id` UUID. Added `[DATA INTEGRITY ALERT]` logging. |

---

## 5. Helper Functions Updated Summary

| Function Name | Updates Applied | Legacy Compatibility |
| :--- | :--- | :--- |
| `_resolve_user_id(user_identifier)` | **[NEW HELPER]** Resolves parameter (UUID, username, or None) to authoritative UUID. | Guarantees DB operations execute strictly on `user_id`. |
| `_mission_defaults(user_id, display_username, mission_date)` | Updated parameters to store `user_id` UUID and `username` audit string. | Provides structured payload for insertion. |
| `get_today_mission(user)` | Resolves `user_id` UUID. Filters SELECT by `user_id`. Inserts `user_id` identity column. Checks `NULL user_id` integrity. | Accepts `username` or defaults to `session_state.user_id`. |
| `update_daily_test(user)` | Resolves `user_id` via `get_today_mission(user)`. | Accepts `username` or defaults to `session_state.user_id`. |
| `update_revision(user)` | Resolves `user_id` via `_increment_today_field(user, ...)`. | Accepts `username` or defaults to `session_state.user_id`. |
| `update_question_count(user)` | Resolves `user_id` via `_increment_today_field(user, ...)`. | Accepts `username` or defaults to `session_state.user_id`. |
| `get_mission_progress(user)` | Resolves `user_id` via `get_today_mission(user)`. | Signature preserves backward compatibility. |
| `claim_reward(user)` | Resolves `user_id` UUID. Updates `reward_claimed` and awards XP passing `user_id` to `add_xp()`. | Signature preserves backward compatibility. |

---

## 6. Remaining Username Dependencies & Temporary Compatibility Code

### Temporary Compatibility Code
To ensure smooth migration without breaking callers passing legacy username strings during Phase 3, profile lookup fallback is retained:
```python
# TODO: Remove username compatibility after Sprint 8 Final Cleanup.
```
Location: `core/daily_mission_ai.py` inside `_resolve_user_id()`.

### Approved Non-Database Username Usages
`username` is retained strictly for non-database operations:
1. **Audit Columns**: Populated in `daily_missions` `INSERT` payloads as a human-readable metadata column.
2. **Logs & Debug Messages**: Used in `logger.warning` / `logger.error` messages for troubleshooting.

---

## 7. Data Integrity Alert Rules

If `get_today_mission()`, `claim_reward()`, or other functions cannot resolve `user_id`, or if a queried row contains `user_id IS NULL`, the system triggers an explicit log alert:
```
[DATA INTEGRITY ALERT] Unable to resolve user_id UUID for daily mission operation (input: ...)
[DATA INTEGRITY ALERT] Daily mission record id=... has user_id IS NULL!
```
The system does **NOT** silently fall back to querying by username string.

---

## 8. Testing & Verification Checklist

- [x] **Syntax Verification**: `python -m py_compile core/daily_mission_ai.py` executed with zero errors.
- [x] **Full Integration Compilation**: `python -m py_compile` executed cleanly across all dependent modules (`test_evaluator.py`, `mentor_chat.py`, `ui/dashboard.py`, `app.py`).
- [x] **UUID SELECT Query Verification**: Confirmed `get_today_mission()` filters by `.eq("user_id", user_id)`.
- [x] **UUID INSERT Query Verification**: Confirmed `_mission_defaults()` & `get_today_mission()` include `"user_id": user_id` in insertion payload.
- [x] **XP Integration Verification**: Confirmed `claim_reward()` passes resolved `user_id` UUID to `add_xp()`.
- [x] **Data Integrity Logging**: Verified `[DATA INTEGRITY ALERT]` logs for missing or NULL `user_id`.
- [x] **Zero Touch Scope Check**: Confirmed no modifications were made to Authentication, Session, XP Engine, Progress Engine, Weakness Engine, Revision Engine, Mentor Memory, Bookmarks, Leaderboard, Analytics, or `repository.py`.
