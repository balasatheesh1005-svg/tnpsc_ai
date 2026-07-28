# TNPSC Nova AI — Navigation Architecture & State Audit

---

## 1. Executive Summary

Navigation in TNPSC Nova AI is currently split across **two independent routing controllers** that frequently desynchronize:
1. **Sidebar Navigation**: Controls `st.session_state["main_menu"]` via `streamlit_option_menu` in `app.py`.
2. **Topic Hub V2 Navigation**: Controls `st.session_state["nav_view"]` (`subject_select`, `topic_select`, `topic_hub`) via `core/navigation_v2/navigation_state.py`.

Because these two systems do not share a single source of truth, switching sidebar items destroys active topic context, forces page reruns, and leaves students stranded at dead ends after completing tests.

---

## 2. Navigation Audit & State Corruption Matrix

| Interaction | Current Routing Mechanism | State Mutation | Identified Bug / UX Flaw |
|---|---|---|---|
| **Select Sidebar Menu Item** | `option_menu` callback in `app.py` line 513 | `st.session_state["main_menu"] = selected` | Wipes active sub-view state without preserving current question or note scroll position. |
| **Topic Hub -> Read Notes** | Button key `hub_launch_notes` in `topic_hub.py` line 201 | `st.session_state["main_menu"] = "📚 Notes"` | Navigates to Notes page, but sidebar menu highlight doesn't sync until next rerun. |
| **Topic Hub -> Start Practice** | Button key `hub_start_prac_<key>` in `topic_hub.py` line 303 | `test_active = True`, `main_menu = "📘 Daily Test"` | Forcibly changes top menu to Daily Test, losing Topic Hub context. |
| **Notes -> Practice Questions** | Button in `ui/pages/notes.py` line 86 | `notes_practice_trigger = True`, `main_menu = "📘 Daily Test"` | Relies on temporary trigger flag `notes_practice_trigger` which clears on rerun. |
| **Submit Last Test Question** | `app.py` line 785 | `test_active = False`, `test_qs = []` | **DEAD END**: Clears question stack and leaves student looking at setup buttons. |
| **Click "Change Subject"** | Button in `topic_hub.py` line 144 | `clear_selected_subject()`, `nav_view = "subject_select"` | Works correctly within Topic Hub view tree. |

---

## 3. Detailed Breakdown of Navigation Risks

### Risk 1: Navigation Loops & Context Loss
When a student selects a subject and topic (e.g. *Polity → Preamble*), `navigation_state.py` sets:
```python
st.session_state["selected_subject"] = "polity"
st.session_state["selected_topic_id"] = "polity_preamble_part1"
```
However, if the student clicks "📘 Daily Test" in the sidebar, `app.py` checks `st.session_state.daily_test_config`. If `daily_test_config` exists, it ignores `selected_topic_id` and loads whatever topic the daily mission engine recommends! The student is now taking a test on *Fundamental Rights* while believing they are practicing *Preamble*!

### Risk 2: Back Button Behavior in Streamlit
Streamlit lacks native browser back-button history management (`window.history.back()`). If a student clicks the browser's back button:
- Streamlit re-executes `app.py` from top to bottom with the current session state.
- Because `st.session_state` retains the last written key values, the page does not go "back" to the previous view; instead, it reloads the current view or resets to Home!

### Risk 3: Fragile Trigger Flags
State flags like `st.session_state["notes_practice_trigger"]` are used to pass commands between pages. If the user clicks any widget (e.g. language radio toggle) before the trigger completes, Streamlit reruns `app.py`, popping or clearing the trigger flag before execution!

---

## 4. Recommended Unified Navigation Router Architecture

To resolve all state corruption and routing flaws, TNPSC Nova AI should implement a single **Unified Page Router**:

```
                              ┌────────────────────────┐
                              │  UNIFIED PAGE ROUTER   │
                              │ (core/router.py)       │
                              └───────────┬────────────┘
                                          │
                  ┌───────────────────────┼───────────────────────┐
                  ▼                       ▼                       ▼
          [ VIEW STATE ]          [ TOPIC CONTEXT ]       [ SESSION STACK ]
          • active_page           • subject_id            • test_active
          • sub_view              • topic_id              • result_mode
          • modal_state           • repository_id         • return_page
```

### Router Rules:
1. **Persistent Topic Context**: `selected_subject` and `selected_topic_id` MUST remain pinned across all main sidebar tabs (Notes, Practice, AI Teacher, Progress).
2. **Tab Breadcrumbs**: Display top breadcrumb bar: `Home / Polity / Preamble / Easy Practice`.
3. **Explicit Return Target**: When starting a test from Notes or Topic Hub, set `st.session_state["return_page"] = "topic_hub"`. Upon test completion, automatically return to `return_page` with the Result Screen overlay!
