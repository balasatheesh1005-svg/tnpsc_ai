# TNPSC Nova AI — Complete Product Audit Report
**Role**: Chief Product Architect & UX Designer  
**Platform Scope**: TNPSC Nova AI Application  
**Target Persona**: TNPSC Group 1 / Group 2 Aspirant  
**Date**: July 22, 2026  

---

## Executive Summary

TNPSC Nova AI possesses rich foundational assets: a multi-repository question engine, bilingual question parsers, spaced-repetition data structures, and Streamlit-based card layouts. However, a comprehensive audit reveals that **the learning experience feels fragmented, linear, and dead-ended**. 

Key systemic flaws identified across the platform include:
1. **Disconnected Navigation Loops**: Students complete practice sets or tests but are left at static screens with no automatic guidance toward the next step (e.g., from Notes to Practice, or Test Result back to Topic Hub).
2. **Superficial Gamification**: XP, levels, and badges exist in backend utilities but are missing visual triggers, milestones, unlockable rewards, or persistent feedback loops.
3. **Fragmented Question Systems**: Question rendering and evaluation are duplicated across custom logic in `app.py`, `ui/pages/daily_test_renderer.py`, and the legacy question engine vs. the modern `universal_renderer.py`.
4. **Keyword-Based Mock AI**: The AI Teacher relies on primitive keyword matching on static text, failing to provide true contextual tutoring, adaptive hints, or personalized explanations based on student history.
5. **Absence of True Mastery Criteria**: Topics are never marked as "Completed". Progress is calculated solely as average percentage on raw attempt logs, ignoring coverage, syllabus alignment, revision cycles, and difficulty progression.

Below is the exhaustive, 10-point audit for every major module of TNPSC Nova AI.

---

# Exhaustive Module Audit (26 Scope Modules)

---

## 1. Dashboard Module

### 1. Purpose
Provides the student with a centralized control center summarizing daily stats (streak, XP, rank, overall accuracy), quick launch shortcuts, and top-level performance indicators.

### 2. Current Flow
Renders via `ui/dashboard.py` inside a tab under `🏠 Home`. Displays glass cards for tests attempted, average accuracy, streak, global rank, weak subject label, and XP progress bar.

### 3. User Journey
The student logs in, views their stats, scrolls through static metrics, and clicks a manual menu item in the sidebar or a launch button to start studying.

### 4. Input
`username`, `users_progress` database table rows, `user_xp` table rows, `user_revisions` queue, `weakness` dict.

### 5. Output
Summary HTML cards, streak badge, level progress bar, weak subject warning callout.

### 6. State Changes
Sets `st.session_state["tests_attempted"]`, `st.session_state["accuracy"]`, `st.session_state["streak"]`, `st.session_state["rank"]`, `st.session_state["weak_subject"]`, `st.session_state["xp"]`, `st.session_state["xp_level"]`.

### 7. Dependencies
`core/dashboard_stats_ai.py`, `core/streak_ai.py`, `core/weakness_ai.py`, `core/xp_ai.py`, `ui/components/cards.py`.

### 8. Navigation
- **Current**: Can navigate to menu items using sidebar.
- **Should Go**: Should feature a primary "Continue Learning Journey" button that automatically routes to the student's current active topic hub or due revision queue.

### 9. Problems
- **Static Display**: Stats are passive; they don't prompt immediate action.
- **No Daily Task Checklist**: Doesn't tell the student *what to do today* (e.g., "Read 1 Note Part, Complete 1 Easy Practice, Do 2 Revisions").
- **Disconnected Rank & XP**: Shows rank and level without showing who is ahead or how many XP are needed for the next rank.

### 10. Recommendations
Transform Dashboard from a passive stat board into an **Active Learning Command Center** featuring a "Today's Action Plan" widget with 3 micro-goals.

---

## 2. Subject Selection Module

### 1. Purpose
Allows the aspirant to select a TNPSC syllabus subject (Polity, History, Economy, Geography, INM, Aptitude, Science).

### 2. Current Flow
Rendered by `ui/navigation_v2/subject_selector.py` when `st.session_state["nav_view"] == "subject_select"`. Displays subject cards with icons, titles, descriptions, and topic counts.

### 3. User Journey
Student clicks "Change Subject" or opens home with no subject selected, sees grid of 7 subjects, and clicks "Explore Topics" on a subject.

### 4. Input
Directories in `data/notes/`, hardcoded metadata dictionary in `core/navigation_v2/navigation_state.py`.

### 5. Output
Updates selected subject in session state.

### 6. State Changes
`st.session_state["selected_subject"] = subj`, `st.session_state["nav_view"] = "topic_select"`.

### 7. Dependencies
`core/navigation_v2/navigation_state.py`, `core/topics_loader.py`.

### 8. Navigation
- **Current**: Goes to Topic Selection (`topic_select`).
- **Should Go**: Should go to Topic Selection or directly resume last active topic in that subject.

### 9. Problems
- **No Progress Indicators on Cards**: Subject cards do not show syllabus completion percentage (e.g., "Polity: 45% Completed").
- **No Exam Weightage Info**: TNPSC aspirants need to know question weightage (e.g., "Polity: ~20 Qs in Group 1").

### 10. Recommendations
Add syllabus progress bars and TNPSC weightage tags (e.g., "High Priority • 25 Qs") on subject cards.

---

## 3. Topic Selection Module

### 1. Purpose
Displays the list of syllabus topics and sub-parts within a selected subject.

### 2. Current Flow
Rendered by `ui/navigation_v2/topic_selector.py` when `nav_view == "topic_select"`. Displays topic cards filtered by subject.

### 3. User Journey
Student browses topics under chosen subject (e.g., Polity -> Preamble, Fundamental Rights, Salient Features) and clicks "Select Topic".

### 4. Input
`selected_subject`, topic metadata loaded from `core/topics_loader.py`.

### 5. Output
Updates global selected topic ID and repository ID.

### 6. State Changes
`set_global_topic(subject, topic_id)` -> sets `selected_topic_id`, `selected_repository_id`, `selected_topic_metadata`, `nav_view = "topic_hub"`.

### 7. Dependencies
`core/navigation_v2/navigation_state.py`, `core/topics_loader.py`.

### 8. Navigation
- **Current**: Goes to Topic Hub (`topic_hub`).
- **Should Go**: Goes to Topic Hub with highlighted recommended action (Read Notes vs Practice).

### 9. Problems
- **Flat List Layout**: Topics with multiple parts (Part 1, Part 2) are listed as separate standalone items without clear visual hierarchy or sequence grouping.
- **Missing Prerequisites**: Student can jump into Part 3 without reading Part 1.

### 10. Recommendations
Group multi-part topics under parent topic containers with sequential step indicators (Step 1 -> Step 2 -> Step 3).

---

## 4. Topic Hub Module

### 1. Purpose
Acts as the central unified workspace for a single topic, bringing together Notes, Practice Repositories, Grand Tests, AI Tutoring, and Topic Analytics.

### 2. Current Flow
Rendered by `ui/navigation_v2/topic_hub.py`. Shows Topic Header, Mastery Card, 3 Main Modules (Read Notes, Grand Test, AI Teacher), 8 Practice Repository cards, and Topic Toolkit buttons.

### 3. User Journey
Student arrives at Topic Hub, views availability of content/questions, selects an action (e.g. Read Notes or Start Practice), and executes it.

### 4. Input
`selected_subject`, `selected_topic_id`, repository availability dict from `check_repository_availability()`.

### 5. Output
Launches selected activity by updating session state (`main_menu = "📚 Notes"` or `"📘 Daily Test"`).

### 6. State Changes
Updates `st.session_state["main_menu"]`, `st.session_state["test_mode"]`, `st.session_state["active_practice_setup"]`.

### 7. Dependencies
`core/navigation_v2/navigation_state.py`, `core/question_loader.py`, `ui/components/cards.py`.

### 8. Navigation
- **Current**: Routes to Notes, Practice Setup, Grand Test, AI Teacher, Weakness, Progress, or PYQ.
- **Should Go**: Should function as an interactive **Learning Path Map** with locked/unlocked stages.

### 9. Problems
- **No Guided Sequence**: Presents 12 buttons at once without enforcing or guiding the optimal order (Notes -> Easy -> Medium -> Hard -> Revision -> GT).
- **Mastery Score Calculation**: Mastery percentage is based purely on file existence counts (`completed_repos / total_repos`), not actual student performance!

### 10. Recommendations
Replace file-count mastery with actual student performance accuracy & coverage, and highlight the single recommended next action with a glowing primary button.

---

## 5. Notes Module

### 1. Purpose
Presents structured, bilingual syllabus study material, articles, memory tricks, and Samacheer Kalvi textbook references.

### 2. Current Flow
Rendered by `ui/pages/notes.py` using `core/streamlit_ui_engine.py:render_notes()`. Parses structured JSON from `data/notes/<subject>/<topic_id>.json`.

### 3. User Journey
Student reads notes, toggles sections, reviews key facts and articles, and clicks "Practice Questions for this Topic" at the bottom.

### 4. Input
`data/notes/<subject>/<topic_id>.json`.

### 5. Output
Bilingual note rendering with tabs/accordions, key concepts, Tamil translation.

### 6. State Changes
Clicking "Practice Questions" sets `st.session_state["notes_practice_trigger"] = True` and switches `main_menu = "📘 Daily Test"`.

### 7. Dependencies
`core/streamlit_ui_engine.py`, `core/navigation_v2/navigation_state.py`.

### 8. Navigation
- **Current**: Routes to Daily Test via practice button or back to Topic Hub via "Switch Topic".
- **Should Go**: Should present immediate 3-question diagnostic check at the bottom before moving back to Topic Hub.

### 9. Problems
- **Reading Progress Not Tracked**: Scrolling/reading a note does not log reading time or mark the note as "Read" in the database.
- **No Bookmark/Highlighting**: Students cannot bookmark specific note sections or highlight constitutional articles for quick revision.

### 10. Recommendations
Track note completion state (`notes_read = True`), log read timestamps, and allow in-note article bookmarking.

---

## 6. AI Teacher Module

### 1. Purpose
Provides instant explanation, doubt resolution, and concept clarification for TNPSC topics.

### 2. Current Flow
Rendered by `ui/pages/teacher.py` calling `core/ai_teacher.py:ai_teacher()`. Scans JSON notes for matching text keywords and returns matching sentences.

### 3. User Journey
Student enters a doubt in a text box, clicks "Ask", and views returned text snippets with a confidence percentage.

### 4. Input
Query string, static notes database loaded via `load_notes()`, student weakness dict.

### 5. Output
Formatted text with subject name, topic title, matching sentences, and confidence score.

### 6. State Changes
None (read-only query).

### 7. Dependencies
`core/ai_teacher.py`, `core/topics_loader.py`, `core/weakness_ai.py`.

### 8. Navigation
- **Current**: Static page in sidebar menu.
- **Should Go**: Embedded contextually within Notes, Question Explanations, and Topic Hub as an inline slide-out tutor.

### 9. Problems
- **Primitive Keyword Search**: Does not use real generative AI or semantic embeddings; fails if query syntax doesn't match exact note words.
- **No Conversation History**: Single-turn prompt/response; cannot ask follow-up questions.
- **Disconnected Context**: Doesn't automatically know which topic or question the student was viewing unless prepended in prompt.

### 10. Recommendations
Upgrade AI Teacher to maintain session conversation memory and inject active topic metadata automatically into queries.

---

## 7. Practice by Repository Module

### 1. Purpose
Enables targeted practice on specific question formats (Easy, Medium, Hard, Statement-Based, Assertion-Reason, Match the Following, Chronology, PYQ).

### 2. Current Flow
Launched from Topic Hub cards. Filters `data/questions/<subject>/<repo>_<type>.json` and initializes test session in `st.session_state`.

### 3. User Journey
Student selects a difficulty/format in Topic Hub, previews question count in Practice Setup card, and starts session.

### 4. Input
Question JSON files from `data/questions/<subject>/`.

### 5. Output
Initializes question stack in `st.session_state.test_qs` and switches to Daily Test view.

### 6. State Changes
`test_active = True`, `test_mode = "practice_<type>"`, `test_qs = [...]`, `q_index = 0`, `score = 0`.

### 7. Dependencies
`ui/navigation_v2/topic_hub.py`, `core/question_loader.py`.

### 8. Navigation
- **Current**: Switches menu to `📘 Daily Test`.
- **Should Go**: Uses Universal Question Renderer inline within Topic Hub workspace without menu jumping.

### 9. Problems
- **Context Loss**: Switching menu to "Daily Test" changes sidebar active item, confusing the student who thought they were doing topic practice.
- **Repository Unavailability Feedback**: Locked repositories display static "Coming Soon" toast without alternative suggestions.

### 10. Recommendations
Render practice sets inside the Topic Hub tab using the Universal Renderer while keeping main menu context unchanged.

---

## 8. Daily Test Module

### 1. Purpose
Provides a daily timed 10-question quiz based on recommended syllabus topics or pending revisions.

### 2. Current Flow
Rendered under `📘 Daily Test` in `app.py`. Offers three modes: "Start Daily Test", "Practice Weak Topics", "Start Revision Test". Loads questions using `core/test_topic_selector.py:get_test_config()`.

### 3. User Journey
Student clicks Daily Test, chooses test mode, answers questions one by one with instant feedback/explanation, and sees final score summary.

### 4. Input
User stats, revision queue, weakness records, question repositories.

### 5. Output
Test score, accuracy %, updated streak, earned XP, recorded attempt in `users_progress`.

### 6. State Changes
Updates `st.session_state["test_active"]`, `st.session_state["q_index"]`, `st.session_state["score"]`, calls `complete_test()`, updates `user_xp`, `user_streak`, `user_revisions`.

### 7. Dependencies
`app.py`, `ui/pages/daily_test_renderer.py`, `core/test_completion.py`, `core/test_evaluator.py`, `core/daily_mission_ai.py`.

### 8. Navigation
- **Current**: Stays on Daily Test screen at completion with empty question state.
- **Should Go**: Automatically navigate to Result Screen -> Topic Hub / Revision Queue.

### 9. Problems
- **Duplicate Execution Logic**: Question loop and submit handler are embedded directly inside `app.py` lines 614-829, duplicating logic from `universal_renderer.py`.
- **Abrupt Ending**: When test ends, `test_qs` is cleared to `[]`, leaving a blank page or requiring page rerun.

### 10. Recommendations
Delegate Daily Test rendering entirely to `universal_renderer.py` and implement a dedicated Result Screen component.

---

## 9. Grand Test Module

### 1. Purpose
Simulates authentic full-length TNPSC Group 1 Preliminary examination with 100 high-difficulty multi-format questions.

### 2. Current Flow
Launched from Topic Hub card ("Start Grand Test"). Loads `data/questions/<subject>/<repo>_grand_test.json`.

### 3. User Journey
Student starts Grand Test, navigates 100 questions, submits answers, and receives overall score.

### 4. Input
Grand test question repository payloads (100 Qs).

### 5. Output
Evaluated test submission, total accuracy, progress record.

### 6. State Changes
`test_mode = "grand_test"`, `test_active = True`, updates `users_progress` with 100 Q performance.

### 7. Dependencies
`ui/navigation_v2/topic_hub.py`, `core/question_loader.py`, `core/test_completion.py`.

### 8. Navigation
- **Current**: Uses Daily Test renderer loop in `app.py`.
- **Should Go**: Dedicated Exam Hall UI mode with full Question Palette, Mark-for-Review toggle, Sectional Filter, and Countdown Timer.

### 9. Problems
- **No Question Palette**: Full 100-question test is rendered linearly one-by-one without jump palette or review flagging.
- **No Exam Timer Locking**: Student can change tabs or take infinite time without real exam pressure enforcement.

### 10. Recommendations
Implement Exam Mode with grid palette, question flagging (Review later), time warnings, and detailed subject-wise diagnostic scorecards.

---

## 10. Question Renderer Module

### 1. Purpose
Parses and displays individual questions across standard MCQs, Statement-Based, Assertion-Reason, Match the Following, and Chronology formats.

### 2. Current Flow
Two parallel implementations exist:
1. Legacy `ui/pages/daily_test_renderer.py` (used by Daily Test in `app.py`).
2. Modern `ui/question_engine/universal_renderer.py` with `UniversalQuestionAdapter` (used in setup views).

### 3. User Journey
Student reads question statement, statements/matches, selects option radio, clicks Submit.

### 4. Input
Raw question dict payload.

### 5. Output
`NormalizedQuestion` dataclass instance, rendered option cards, selected option key.

### 6. State Changes
`st.session_state["last_selected_option"]`, `record_answer()`.

### 7. Dependencies
`ui/question_engine/parser.py`, `ui/question_engine/body_component.py`, `ui/question_engine/option_component.py`.

### 8. Navigation
- **Current**: Next button advances index `q_index += 1`.
- **Should Go**: Smooth transition with question status indicator (Answered, Unanswered, Marked for Review).

### 9. Problems
- **Code Duplication**: Dual rendering logic creates inconsistencies in language toggle state and timing tracking between Daily Test and Topic Practice.
- **Tamil Font Formatting**: Missing Tamil line-height tuning for long multi-statement options.

### 10. Recommendations
Deprecate `daily_test_renderer.py` and standardize all test modes on `universal_renderer.py`.

---

## 11. Explanation Renderer Module

### 1. Purpose
Provides detailed post-answer breakdown, showing correct answer, explanation text, article references, Samacheer Kalvi page numbers, and exam trap alerts.

### 2. Current Flow
Rendered by `ui/question_engine/explanation_component.py`. Displays green/red alert card with explanation text and metadata chips.

### 3. User Journey
After submitting an answer, student reads why the answer was correct/incorrect, learns the underlying concept, and clicks "Next".

### 4. Input
`NormalizedQuestion`, user's chosen option key.

### 5. Output
Styled explanation block with "Ask AI Teacher" shortcut button.

### 6. State Changes
None directly.

### 7. Dependencies
`ui/question_engine/explanation_component.py`, `ui/pages/teacher.py`.

### 8. Navigation
- **Current**: Advances to next question via "Next" button.
- **Should Go**: Include inline "Bookmark Question" and "Ask AI Teacher About This Question" action triggers.

### 9. Problems
- **Static Explanation Text**: Non-interactive; cannot click on constitutional terms or articles to open referenced notes.
- **Missing Distractor Analysis**: Doesn't explain *why* the other 3 options were wrong.

### 10. Recommendations
Add option-by-option distractor analysis and hyperlinked article references.

---

## 12. Result Screen Module

### 1. Purpose
Displays comprehensive session analytics after test completion (Score, Percentage, Time Taken, XP Earned, Level Up alert, Weak Topics identified).

### 2. Current Flow
Currently **missing a dedicated Result Screen page**! When a test finishes in `app.py`, it calculates percent, calls `complete_test()`, shows a toast/balloons if level up, and clears `test_qs`.

### 3. User Journey
Student submits last question, test suddenly vanishes, and student is left looking at an empty Daily Test screen with selection buttons!

### 4. Input
Test completion stats, score, total questions, time elapsed, start XP vs end XP.

### 5. Output
Score breakdown, accuracy radial chart, strength/weakness summary, XP earned badge, "Next Steps" navigation buttons.

### 6. State Changes
`test_results_processed = True`, `test_active = False`.

### 7. Dependencies
`core/test_completion.py`, `ui/question_engine/result_component.py`.

### 8. Navigation
- **Current**: DEAD END. Leaves student stranded on Daily Test tab.
- **Should Go**: Presents explicit buttons: "Return to Topic Hub", "Revise Weak Answers", "Start Recommended Next Topic".

### 9. Problems
- **CRITICAL DEAD END**: This is the primary reason the app feels broken and incomplete after completing practice!

### 10. Recommendations
Implement `render_universal_result_screen()` immediately after test completion with clear calls-to-action.

---

## 13. Progress Module

### 1. Purpose
Displays overall syllabus coverage, repository accuracy, test attempt logs, and weak/strong topic breakdowns.

### 2. Current Flow
Rendered by `ui/pages/progress.py`. Fetches records from `users_progress` table, aggregates data using `pandas`, and displays tables for Repository Level and Part Level accuracy.

### 3. User Journey
Student opens "📊 Progress" from menu, reviews active topics count, total tests, overall accuracy, and weak/strong topic lists.

### 4. Input
`users_progress` database rows.

### 5. Output
Metrics cards, repository accuracy dataframe, part-level breakdown dataframe, weak/strong lists.

### 6. State Changes
None (read-only analytics).

### 7. Dependencies
`core/progress_ai.py`, `core/topics_loader.py`, `pandas`.

### 8. Navigation
- **Current**: View-only page.
- **Should Go**: Clicking any weak topic in the table should directly open that topic's Topic Hub for immediate practice.

### 9. Problems
- **No Direct Action Links**: Weak topics are listed as static text; student cannot click to practice them.
- **Skewed Accuracy Calculation**: Simple arithmetic mean over attempts; older bad scores penalize recent mastery.

### 10. Recommendations
Implement exponentially weighted accuracy (recent tests weighted higher) and add clickable "Practice Now" buttons next to weak topics.

---

## 14. Weakness Analysis Module

### 1. Purpose
Tracks and visualizes specific topic areas where the student has high error rates or frequent wrong answers.

### 2. Current Flow
Rendered by `ui/pages/weakness.py`. Calls `core/weakness_ai.py:get_weakness(user)`. Displays styled pandas dataframe heatmap and visual strength progress bars (`███`).

### 3. User Journey
Student reviews their weakness heatmap, identifies topics with error scores >= 4 (colored red), and notes what to revise.

### 4. Input
`users_weakness` database table / state dict.

### 5. Output
Color-coded weakness heatmap dataframe and visual strength bar table.

### 6. State Changes
None.

### 7. Dependencies
`core/weakness_ai.py`, `core/test_weakness.py`.

### 8. Navigation
- **Current**: View-only page.
- **Should Go**: Include a prominent "🔥 Launch Remedial Practice for Weak Topics" button at top.

### 9. Problems
- **No Automated Remediation**: Identifies weaknesses but doesn't offer a 1-click targeted revision quiz.
- **Unclear Metric**: Weakness score is an integer count (e.g. 4) without explaining if 4 means 4 wrong answers or 4 consecutive fails.

### 10. Recommendations
Add "Generate Weakness Booster Quiz" button and translate raw error score into readable status ("Critical", "Moderate", "Mastered").

---

## 15. Revision Module

### 1. Purpose
Schedules spaced-repetition revision sessions (Spaced Repetition intervals: Day 1, 3, 7, 15, 30) to prevent memory decay of studied TNPSC topics.

### 2. Current Flow
Managed by `core/revision_ai.py` and `core/test_revision.py`. Pending revisions are queried from `user_revisions` table (`next_due <= today`). Launched via "Start Revision Test" button on Daily Test page.

### 3. User Journey
Student selects "Start Revision Test", system fetches due revision topics, loads questions, and updates topic revision level upon completion.

### 4. Input
`user_revisions` table rows (`username`, `subject`, `topic`, `level`, `next_due`).

### 5. Output
Revision queue list, updated due date in DB (`days_map = {1:1, 2:3, 3:7, 4:15, 5:30}`).

### 6. State Changes
`update_revision()` increases topic level (max 5) and pushes `next_due` forward.

### 7. Dependencies
`core/revision_ai.py`, `core/test_revision.py`, `core/daily_mission_ai.py`.

### 8. Navigation
- **Current**: Only accessible via Daily Test page sub-button.
- **Should Go**: Dedicated "Smart Revision Hub" page showing revision calendar, overdue items count, and interval progress.

### 9. Problems
- **Hidden Feature**: Spaced repetition is one of TNPSC Nova AI's strongest features, yet it has **no dedicated UI page**! It is buried inside Daily Test button options.
- **No Daily Reminder**: Dashboard does not show "3 Revisions Due Today" banner.

### 10. Recommendations
Create a dedicated "Smart Revision Hub" page and display a red badge on sidebar menu when revisions are overdue.

---

## 16. Bookmarks Module

### 1. Purpose
Allows students to save difficult questions, tricky articles, or landmark judgements during practice for quick review before exams.

### 2. Current Flow
Handled in state via `core/question_engine/bookmark.py` (`st.session_state["daily_bookmarks"]`).

### 3. User Journey
Student clicks bookmark icon in Question Header during a test. Bookmark is saved into session set.

### 4. Input
Question ID, user ID.

### 5. Output
Bookmarked question set.

### 6. State Changes
Updates `st.session_state["<prefix>_bookmarks"]`.

### 7. Dependencies
`core/question_engine/bookmark.py`, `ui/question_engine/header_component.py`.

### 8. Navigation
- **Current**: NO UI PAGE to view saved bookmarks!
- **Should Go**: Dedicated "Saved Bookmarks & Vault" page accessible from sidebar or profile.

### 9. Problems
- **CRITICAL MISSING UI**: Students can bookmark questions during a test, but **cannot view their bookmarked questions anywhere in the app**!
- **No Database Persistence**: Bookmarks are stored in temporary Streamlit session state and disappear upon page refresh or logout!

### 10. Recommendations
Add `user_bookmarks` table in Supabase and create a "Bookmark Vault" page where students can review saved questions with explanations.

---

## 17. Leaderboard Module

### 1. Purpose
Fosters friendly competition among TNPSC aspirants by ranking users based on average accuracy and total tests attempted.

### 2. Current Flow
Rendered by `ui/pages/leaderboard.py` calling `core/leaderboard_ai.py:get_leaderboard()`. Queries `users_progress` table, aggregates average accuracy, and displays top ranked users.

### 3. User Journey
Student opens Leaderboard from menu, views top 10 rankings, and sees their own global rank position.

### 4. Input
`users_progress` database table rows across all users.

### 5. Output
Ranked leaderboard table with user icons, average accuracy, and rank numbers.

### 6. State Changes
None.

### 7. Dependencies
`core/leaderboard_ai.py`, `core/dashboard_stats_ai.py`.

### 8. Navigation
- **Current**: Static view page.
- **Should Go**: Include weekly leaderboard tabs (This Week, All Time, Subject Leaderboards).

### 9. Problems
- **Ranking Metric Flaw**: Ranks users purely by average accuracy regardless of whether they answered 5 questions or 500 questions!
- **No XP Leaderboard**: Leaderboard ignores XP points and Level progression entirely.

### 10. Recommendations
Base leaderboard ranking on Total XP earned (combining test accuracy, consistency, and volume) and add weekly resetting tiers (Gold, Silver, Bronze leagues).

---

## 18. Achievements & Badges Module

### 1. Purpose
Rewards students for reaching key milestones (e.g. "Polity Master", "7-Day Streak Warrior", "Centum Club", "100 Questions Solved").

### 2. Current Flow
**Non-existent UI / Disconnected Backend**. XP code in `core/test_completion.py` awards `accuracy_100_bonus` and `streak_7_day`, but there is **no achievement showcase or badge gallery** anywhere in the product!

### 3. User Journey
Student completes a milestone but receives no permanent badge, trophy icon, or profile achievement card.

### 4. Input
User stats, streak count, completed tests count.

### 5. Output
None displayed.

### 6. State Changes
None persistent.

### 7. Dependencies
`core/xp_ai.py`, `core/test_completion.py`.

### 8. Navigation
- **Current**: None.
- **Should Go**: Profile page / Dashboard "Badges & Trophies" section.

### 9. Problems
- **Missing Gamification Anchor**: Aspirants miss out on visual gratification and achievement recognition.

### 10. Recommendations
Design a "Trophy Room" with 15 unlockable TNPSC achievements (e.g., "Constitution Scholar", "Speed Demon", "Revision Master").

---

## 19. XP (Experience Points) Module

### 1. Purpose
Quantifies learning effort and engagement, awarding points for correct answers, completed tests, perfect scores, and daily streaks.

### 2. Current Flow
Managed by `core/xp_ai.py`. Tables: `user_xp`. Rewards: +10 per correct answer, +50 for test completion, +50 for 100% accuracy, +20 for revision completion, +100 for 7-day streak.

### 3. User Journey
Student earns XP after completing tests, sees temporary info toast in `complete_test()`, and views total XP in Dashboard header.

### 4. Input
Completed activity events.

### 5. Output
Updated total XP score in DB, level calculation (`LEVEL_THRESHOLDS = {1:0, 2:100, 3:250, 4:500, 5:1000...}`).

### 6. State Changes
Updates `user_xp` table, sets `st.session_state["xp"]`, checks `level_up`.

### 7. Dependencies
`core/xp_ai.py`, `core/test_completion.py`, `core/supabase_client.py`.

### 8. Navigation
- **Current**: Displayed in Dashboard & Sidebar.
- **Should Go**: Real-time floating XP animation popups (+50 XP!) during test execution.

### 9. Problems
- **Delayed Gratification**: XP is calculated silently at test completion instead of animated dynamically when answering questions.
- **No XP Redemption / Utility**: XP points cannot be spent on unlockables (e.g. detailed mock exam keys or special AI mentor themes).

### 10. Recommendations
Add micro-animations for XP gains and introduce XP milestone rewards.

---

## 20. Levels Module

### 1. Purpose
Represents student seniority and mastery progression from Level 1 (Novice Aspirant) to Level 10 (TNPSC Officer).

### 2. Current Flow
Calculated in `core/xp_ai.py:get_level_from_xp()`. Level thresholds range from 0 XP (L1) to 10,000 XP (L10). Triggers balloons animation on level up in `app.py`.

### 3. User Journey
Student reaches XP threshold, completes test, sees balloons animation and "🎉 LEVEL UP!" alert box.

### 4. Input
Total XP.

### 5. Output
Level number (1-10), progress percentage to next level.

### 6. State Changes
`st.session_state["xp_level"]`, `st.session_state["xp_level_up"] = True`.

### 7. Dependencies
`core/xp_ai.py`, `app.py`.

### 8. Navigation
- **Current**: Alert message on test complete.
- **Should Go**: Level roadmap screen showing perks unlocked at each level (e.g., Level 3 unlocks Grand Tests).

### 9. Problems
- **Arbitrary Level Titles**: Levels are raw numbers (Level 1, Level 2) without meaningful TNPSC designation titles (e.g., Level 1: Village Administrative Officer candidate -> Level 10: Deputy Collector aspirant).

### 10. Recommendations
Assign authentic TNPSC Cadre Titles to levels (e.g. L1: Junior Assistant -> L5: Sub-Registrar -> L10: Deputy Collector).

---

## 21. Streak Module

### 1. Purpose
Encourages daily study habits by tracking consecutive active login/practice days.

### 2. Current Flow
Managed by `core/streak_ai.py`. Database table `users_streak`. Updates daily when user completes a test. If last activity was yesterday, streak increases by 1. If > 1 day missed, resets to 1.

### 3. User Journey
Student sees flame icon 🔥 with streak day count in sidebar header and dashboard.

### 4. Input
User ID, timestamp of test completion.

### 5. Output
Streak integer count.

### 6. State Changes
Updates `users_streak` table, sets `st.session_state["streak"]`.

### 7. Dependencies
`core/streak_ai.py`, `core/test_completion.py`.

### 8. Navigation
- **Current**: Header badge display.
- **Should Go**: Clickable streak calendar popup showing active vs missed dates.

### 9. Problems
- **Strict Reset Punishes Users**: Missing one day due to an emergency completely wipes out a 30-day streak with no "Streak Freeze" protection.
- **Only Increments on Test Completion**: Reading notes or asking AI Teacher for 2 hours does not count toward daily streak!

### 10. Recommendations
Count *any* learning activity (reading notes, practice, revision) toward daily streak and introduce 1 free monthly "Streak Freeze".

---

## 22. Analytics Module

### 1. Purpose
Provides deep diagnostic charts into accuracy trends over time, subject strength distribution, time per question, and confidence accuracy correlation.

### 2. Current Flow
Fragmented across `ui/pages/progress.py` (basic tables) and `ui/pages/weakness.py` (error list). No dedicated visual chart analytics dashboard exists.

### 3. User Journey
Student wants to see their 30-day accuracy graph or time-spent breakdown but can only view static raw dataframes.

### 4. Input
`users_progress` table timestamps, score, time taken.

### 5. Output
None (missing visual charts).

### 6. State Changes
None.

### 7. Dependencies
`core/progress_ai.py`.

### 8. Navigation
- **Current**: View progress menu item.
- **Should Go**: Dedicated "Analytics & Insights Hub" with interactive Plotly / Vega charts.

### 9. Problems
- **No Time-Series Charts**: Aspirants cannot see if their performance is improving over weeks.
- **No Speed vs Accuracy Matrix**: Fails to show if student is rushing or overthinking.

### 10. Recommendations
Integrate visual line graphs for 30-day accuracy trends and bar charts for subject speed metrics.

---

## 23. Profile Module

### 1. Purpose
Displays user account details, target exam (Group 1, Group 2, Group 4), medium preference (English / Tamil), cumulative stats, and earned badges.

### 2. Current Flow
**Missing Dedicated Profile Screen**! User info is split between sidebar header branding (`render_sidebar_branding`) and session state `st.session_state["username"]`.

### 3. User Journey
Student has no place to view or edit their profile preferences or target exam setting.

### 4. Input
Session auth state.

### 5. Output
Sidebar display of username and avatar.

### 6. State Changes
None.

### 7. Dependencies
`ui/components/header.py`, `core/auth.py`.

### 8. Navigation
- **Current**: None.
- **Should Go**: Top-right profile dropdown / dedicated sidebar "My Profile" tab.

### 9. Problems
- **Target Exam Locked**: Hardcoded to `exam = "group1"` in session defaults; student cannot switch focus to Group 2 or Group 4.

### 10. Recommendations
Build a full Profile & Account Management page with target exam selector and stats summary.

---

## 24. Settings Module

### 1. Purpose
Allows configuration of UI themes, language preferences (Default English/Tamil/Both), font size, notification toggles, and data reset choices.

### 2. Current Flow
**Missing Settings Module**. Theme is auto-rendered via `ui/theme.py:render_theme_css()`. Language radio is selected per-question.

### 3. User Journey
Student cannot set a global default language (must change radio button during every test) or adjust visual themes.

### 4. Input
None.

### 5. Output
None.

### 6. State Changes
None.

### 7. Dependencies
`ui/theme.py`.

### 8. Navigation
- **Current**: None.
- **Should Go**: Settings drawer or dedicated menu item.

### 9. Problems
- **No Global Language Preference**: Resetting session defaults language back to "BOTH" on every question screen.

### 10. Recommendations
Add Settings modal/page to store persistent user preferences (e.g. Default Language = Tamil).

---

## 25. Navigation Module

### 1. Purpose
Manages screen transitions, menu selection, topic context, state persistence, and back-button behavior across the entire app.

### 2. Current Flow
Dual navigation architecture:
1. Top-level menu managed via `streamlit_option_menu` in sidebar (`st.session_state["main_menu"]`).
2. Topic Hub sub-navigation managed via `core/navigation_v2/navigation_state.py` (`st.session_state["nav_view"]` = `subject_select`, `topic_select`, `topic_hub`).

### 3. User Journey
Student navigates between Home tabs, Daily Test, Notes, and Progress. Switches topics via Topic Hub header buttons.

### 4. Input
`main_menu`, `nav_view`, `selected_subject`, `selected_topic_id`.

### 5. Output
Rendered active page view.

### 6. State Changes
Updates `main_menu`, `nav_view`, `selected_topic_id`, `selected_repository_id`.

### 7. Dependencies
`app.py`, `core/navigation_v2/navigation_state.py`, `streamlit_option_menu`.

### 8. Navigation
- **Current**: Functional but decoupled. Sidebar menu overrides Topic Hub context.
- **Should Go**: Unified Router where sidebar menu respects current active topic context.

### 9. Problems
- **Context Loss on Menu Switch**: If student is in Topic Hub under "Polity -> Preamble" and clicks "📚 Notes" in sidebar, notes opens correctly, but clicking "📘 Daily Test" starts a generic daily test instead of Preamble test!
- **State Corruption on Rerun**: Missing explicit state restoration when switching between main tabs.

### 10. Recommendations
Unify navigation state so selected subject/topic persists across all main sidebar tabs (Notes, Practice, AI Teacher).

---

## 26. Session State Module

### 1. Purpose
Stores transient in-memory application variables across Streamlit reruns (auth token, user stats, test index, score, question stack, language mode).

### 2. Current Flow
Initialized in `app.py:initialize_session_state()` and `core/navigation_v2/navigation_state.py:init_navigation_state()`.

### 3. User Journey
Implicit backend execution on every user click or radio selection.

### 4. Input
Streamlit rerun triggers.

### 5. Output
`st.session_state` dict.

### 6. State Changes
Mutates `q_index`, `test_active`, `answered`, `score`, `test_qs`, `main_menu`, `nav_view`.

### 7. Dependencies
`app.py`, `core/session.py`, `core/navigation_v2/navigation_state.py`.

### 8. Navigation
N/A (State backbone).

### 9. Problems
- **Key Collisions & Redundancy**: `test_topic` stores repository ID string in some files and display title string in others! `st.session_state.test_mode` is written twice in `app.py` line 632-633!
- **Unsanitized Rerun Crashes**: If `test_qs` becomes empty during active test, app crashes with index error unless caught by fallback.

### 10. Recommendations
Consolidate session state keys into a clean, typed `SessionStateSchema` dataclass wrapper.

---

## Summary Matrix of Module Audits

| # | Module | Status | Primary Weakness / Bottleneck | Recommendation |
|---|---|---|---|---|
| 1 | Dashboard | Implemented | Passive stats; no daily action plan | Add 3-task Daily Action Plan widget |
| 2 | Subject Selection | Implemented | No syllabus completion / TNPSC weightage | Add progress bars & TNPSC weight tags |
| 3 | Topic Selection | Implemented | Flat topic list; missing multi-part structure | Group by multi-part parent topics |
| 4 | Topic Hub | Implemented | Overwhelming layout; fake mastery calculation | True performance mastery & 1 primary button |
| 5 | Notes | Implemented | Reading completion & scroll time not saved | Track note reading state & article bookmarks |
| 6 | AI Teacher | Implemented | Primitive keyword matching; no LLM context | Upgrade to contextual memory engine |
| 7 | Practice Repo | Implemented | Switches menu tab away from workspace | Render practice inline in Topic Hub |
| 8 | Daily Test | Implemented | Duplicated logic in `app.py`; abrupt end | Delegate to `universal_renderer.py` |
| 9 | Grand Test | Implemented | Missing 100-Q palette & exam hall controls | Dedicated Exam Mode with Question Palette |
| 10 | Question Renderer | Dual System | Legacy renderer conflicts with Universal | Deprecate legacy, standardize on Universal |
| 11 | Explanation Renderer | Implemented | Non-interactive distractor analysis | Add option-by-option distractor analysis |
| 12 | Result Screen | **MISSING** | **Dead End after test completion** | **Build dedicated Result Screen page** |
| 13 | Progress | Implemented | Static dataframes; no direct action links | Clickable weak topic practice triggers |
| 14 | Weakness | Implemented | Heatmap shown but no 1-click booster test | Add "Generate Weakness Booster Quiz" |
| 15 | Revision | Disconnected | No dedicated UI page; hidden in sub-menus | Build dedicated "Smart Revision Hub" page |
| 16 | Bookmarks | **MISSING** | **Bookmarks saved in state but no UI view** | **Build persistent "Bookmark Vault" page** |
| 17 | Leaderboard | Implemented | Ranks by raw average; ignores XP & count | Rank by Total XP with weekly tiers |
| 18 | Achievements | **MISSING** | Backend awards XP but no badge gallery | Build "Trophy Room" with 15 badges |
| 19 | XP System | Implemented | Silent backend calculation | Add animated XP gain popups |
| 20 | Levels | Implemented | Raw level numbers (L1-L10) | Assign authentic TNPSC Cadre Titles |
| 21 | Streak | Implemented | Resets abruptly; missing Streak Freeze | Allow Streak Freeze & count note reading |
| 22 | Analytics | **MISSING** | No time-series accuracy or speed graphs | Build visual chart analytics dashboard |
| 23 | Profile | **MISSING** | User details split; target exam locked | Build Profile & Exam Target Manager |
| 24 | Settings | **MISSING** | No global language / theme configuration | Build Settings page for user defaults |
| 25 | Navigation | Fragmented | Sidebar menu overrides Topic Hub context | Unify router & preserve topic context |
| 26 | Session State | Fragile | Key collisions & duplicate state writes | Consolidate into clean Schema |
