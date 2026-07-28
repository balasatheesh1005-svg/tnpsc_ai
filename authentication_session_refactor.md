# TNPSC Nova AI — Identity Migration v1.0
## Phase 3 - Sprint 1: Authentication & Session Refactor Report

**Architect:** Lead Software Architect, TNPSC Nova AI  
**Date:** July 25, 2026  
**Status:** Implemented & Verified  
**Sprint Focus:** Authentication Module & Streamlit Session State Architecture  

---

## 1. Executive Summary

Phase 1 (Database Schema Preparation) and Phase 2 (Data Backfill & Test Data Cleanup) established the dual-identity database foundation.

This report establishes **Phase 3 - Sprint 1: Authentication & Session Refactor**. In this sprint, the authentication and session state engine has been updated to maintain dual-identity state in Streamlit `session_state` upon successful login, signup, or auto-session restoration.

### Key Accomplishments of Sprint 1
1. **Dual Identity in Session State**: Every authenticated user session now populates both `st.session_state.user_id` (UUID from `public.profiles.id`) and `st.session_state.username` (legacy identifier).
2. **Profile Lookup Alignment**: Profile retrieval during authentication primary-keys on `profiles.id` (`UUID`), fallback-matching on `email` or `username`.
3. **Zero UI or Business Logic Disruption**: Display components, profile management, and login screens remain 100% unchanged.
4. **Zero Domain Module Touch**: `progress_ai`, `xp_ai`, `revision_ai`, `weakness_ai`, `daily_mission_ai`, `mentor_memory`, `bookmarks`, and `user_analytics` were **not modified**.
5. **Zero Database DDL/SQL Alteration**: No database schema changes, SQL edits, or RLS modifications performed.

---

## 2. Session State Dual-Identity Matrix

After successful authentication (`login`, `sign_up`, or `restore_auth_session`), Streamlit `session_state` holds the following identity attributes:

| Session Key | Data Type | Primary Source | Usage Purpose |
| :--- | :--- | :--- | :--- |
| `st.session_state.user_id` | `UUID` (string) | `public.profiles.id` (ref `auth.users.id`) | Future Phase 3b UUID database queries |
| `st.session_state.username` | `TEXT` (string) | `public.profiles.username` | Current application display & legacy queries |
| `st.session_state.email` | `TEXT` (string) | `public.profiles.email` | User communications & auth lookups |
| `st.session_state.full_name` | `TEXT` (string) | `public.profiles.full_name` | User UI display header |
| `st.session_state.auth_session` | `Session` (object) | Supabase Auth Client | Token refresh & API session state |
| `st.session_state.auth_user` | `User` (object) | Supabase Auth Client | User identity metadata |
| `st.session_state.auth_profile` | `dict` | `public.profiles` row | Complete user profile memory dictionary |

---

## 3. Authentication Module Inspection & Flow Analysis

The authentication module comprised of `core/auth.py` and `core/session.py` was inspected and refactored:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AUTHENTICATION FLOW                              │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   [User Login / Auto-Restore / Signup]                                 │
│                     │                                                  │
│                     ▼                                                  │
│   1. Supabase Auth Authentication (Email / Password / Token)          │
│                     │                                                  │
│                     ▼                                                  │
│   2. Retrieve Profile by UUID (get_profile_by_user_id(user.id))       │
│                     │                                                  │
│                     ▼                                                  │
│   3. Execute save_auth_session(session, user, profile)                │
│                     │                                                  │
│                     ▼                                                  │
│   4. Populate Streamlit Session State:                                │
│        - st.session_state.user_id   = profile["id"] (UUID)             │
│        - st.session_state.username  = profile["username"]              │
│        - st.session_state.email     = profile["email"]                 │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### Module Functions Audit Summary
- **`login(identifier, password)`**: Resolves identifier (username or email), authenticates via Supabase Auth, fetches profile by `profiles.id` UUID, and populates `st.session_state.user_id`, `st.session_state.username`, and `st.session_state.email`.
- **`sign_up(full_name, username, email, password, confirm_password)`**: Validates credentials, creates `auth.users` record, creates `public.profiles` row with matching `id` (UUID), and saves dual-identity session state.
- **`restore_auth_session()`**: Auto-login helper retrieving persisted tokens (`tnpsc_at`, `tnpsc_rt`), validating with Supabase Auth, resolving profile by `profiles.id` UUID, and restoring session state seamlessly.
- **`logout()`**: Signs out of Supabase Auth and invokes `clear_auth_session()` to clear all authentication keys from `st.session_state`.

---

## 4. Code Changes Summary

### 4.1 Changes in `core/session.py`
Updated `save_auth_session()` to ensure `user_id` (UUID from `profiles.id`), `username`, and `email` are explicitly populated in `st.session_state`. Added `current_user_email()` and `get_session_identity()` helper functions:

```python
def save_auth_session(session, user, profile):
    st.session_state["auth_session"] = session
    st.session_state["auth_user"] = user
    st.session_state["auth_profile"] = profile or {}
    persist_auth_session(session)

    profile_dict = profile or {}

    # Extract user_id UUID from profiles.id first, falling back to auth user object
    user_id = profile_dict.get("id") or getattr(user, "id", None)
    if isinstance(user, dict) and not user_id:
        user_id = user.get("id")

    email = profile_dict.get("email") or getattr(user, "email", None)
    if isinstance(user, dict) and not email:
        email = user.get("email")

    username = profile_dict.get("username") or email or ""

    st.session_state["user_id"] = str(user_id) if user_id else None
    st.session_state["username"] = username
    st.session_state["email"] = email
    st.session_state["full_name"] = profile_dict.get("full_name") or ""
```

### 4.2 Changes in `core/auth.py`
Ensured `get_profile_by_user_id(user_id)` is invoked with the Supabase Auth UUID to retrieve authoritative profile details from `public.profiles`, passing the full profile dictionary into `save_auth_session`.

---

## 5. Migration Notes for Future Sprints

1. **Sprint 2 (Dual-Write Engine)**:
   - When Python domain modules (`core/progress_ai.py`, `core/xp_ai.py`, etc.) are updated in future sprints, they can access `st.session_state.user_id` or `current_user_id()` directly without extra profile DB lookups.
2. **Backwards Compatibility**:
   - `st.session_state.username` remains completely intact and active.
   - All current UI components (`ui/dashboard.py`, `ui/pages/*.py`) continue accessing `current_username()` without disruption.
3. **No Schema Changes**:
   - Database tables remain on the Phase 1 & 2 dual-identity schema.

---

## 6. Testing & Verification Checklist

- [x] **Email Login Test**: Login using email address $\rightarrow$ verify `st.session_state.user_id` contains UUID and `st.session_state.username` contains username.
- [x] **Username Login Test**: Login using username $\rightarrow$ verify `st.session_state.user_id` contains UUID and `st.session_state.username` contains username.
- [x] **Signup Test**: Create new user $\rightarrow$ verify profile inserted into `public.profiles` with matching UUID `id` and session populated correctly.
- [x] **Auto-Login / Session Restore Test**: Refresh browser page $\rightarrow$ verify `restore_auth_session()` restores `st.session_state.user_id` UUID, `username`, and `email` without requiring re-login.
- [x] **Logout Test**: Click logout $\rightarrow$ verify `st.session_state.user_id`, `username`, and `email` are cleared completely.
- [x] **UI Continuity Verification**: Verify application dashboard, leaderboards, daily missions, and AI mentor load and display identically to pre-refactor state.
