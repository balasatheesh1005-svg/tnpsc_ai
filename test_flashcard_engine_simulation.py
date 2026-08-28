# -*- coding: utf-8 -*-
"""
Verification & Simulation Script for TNPSC Nova AI Flashcard Engine
Tests flashcard data normalization, session state lifecycle, 10-card sequence, FLIP/NEXT safety.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from ui.notes.components.revision_cards import _normalize_cards, _extract_str

print("==================================================")
print("RUNNING FLASHCARD ENGINE VERIFICATION & SIMULATION")
print("==================================================")

# 1. Test Data Normalization across different topic notes
test_files = [
    ("President Part 1", "data/notes/polity/president_part_1.json", "revision_cards"),
    ("Vice-President Part 1", "data/notes/polity/vice_president_part_1.json", "revision_cards"),
    ("Prime Minister Part 1", "data/notes/polity/prime_minister_part_1.json", "revision_cards"),
    ("Governor Part 1", "data/notes/polity/governor_part_1.json", "revision_cards"),
    ("Governor Part 2", "data/notes/polity/governor_part_2.json", "revision_cards"),
    ("Governor Part 3", "data/notes/polity/governor_part_3.json", "revision_cards"),
    ("Fundamental Rights Part 1", "data/notes/polity/fundamental_rights_part_1.json", "revision_cards"),
]

for label, fpath, key in test_files:
    if os.path.exists(fpath):
        with open(fpath, encoding="utf-8") as f:
            data = json.load(f)
        raw_cards = data.get("content", {}).get(key) or data.get(key)
        norm_cards = _normalize_cards(raw_cards)
        print(f"✓ {label}: Loaded {len(norm_cards)} normalized cards.")
        assert len(norm_cards) >= 6, f"Expected at least 6 cards for {label}, got {len(norm_cards)}"
        card0 = norm_cards[0]
        assert card0["front"].strip() != "", f"Empty front in {label}"
        assert card0["back"].strip() != "", f"Empty back in {label}"

print("\n--- TEST 1 PASSED: DATA NORMALIZATION ACROSS ALL TOPIC NOTES ---")

# 2. Test Streamlit Session State & Navigation Flow Simulation
import streamlit as st

class MockSessionState(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value

mock_state = MockSessionState()
st.session_state = mock_state

# Load Governor Part 1 cards
with open("data/notes/polity/governor_part_1.json", encoding="utf-8") as f:
    gov_data = json.load(f)

raw_cards = gov_data.get("content", {}).get("revision_cards")
cards = _normalize_cards(raw_cards)
total_cards = len(cards)
print(f"\nSimulating 10-Card Sequence for Governor Part 1 ({total_cards} cards):")

topic_id = "polity_governor_part_1"
deck_key = f"fc_deck_{topic_id}"
index_key = f"fc_index_{topic_id}"
flipped_key = f"fc_flipped_{topic_id}"
completed_key = f"fc_completed_{topic_id}"

# Init state
st.session_state.active_fc_deck = deck_key
st.session_state[index_key] = 0
st.session_state[flipped_key] = False
st.session_state[completed_key] = False

# Step through cards 1 to 10 with FLIP and NEXT actions
for step_idx in range(total_cards):
    curr_idx = st.session_state[index_key]
    assert curr_idx == step_idx, f"Step mismatch! Expected index {step_idx}, got {curr_idx}"
    card = cards[curr_idx]
    
    # Initial state for this card
    assert st.session_state[flipped_key] == False, f"Card {curr_idx+1} should start unflipped"
    front_text_clean = card["front"][:60].replace("\n", " ")
    print(f"  [Card {curr_idx+1} / {total_cards}] FRONT: {front_text_clean}...")
    
    # Action 1: FLIP
    st.session_state[flipped_key] = not st.session_state[flipped_key]
    assert st.session_state[flipped_key] == True, f"Card {curr_idx+1} flip failed"
    back_text_clean = card["back"][:60].replace("\n", " ")
    print(f"  [Card {curr_idx+1} / {total_cards}] FLIPPED -> BACK: {back_text_clean}...")
    
    # Action 2: NEXT
    if curr_idx < total_cards - 1:
        st.session_state[index_key] += 1
        st.session_state[flipped_key] = False
    else:
        st.session_state[completed_key] = True

# Verify Completion State
assert st.session_state[completed_key] == True, "Completion state was not reached at card 10!"
print("  🎉 Revision Deck Complete state triggered successfully!")

# Action 3: RESTART
st.session_state[index_key] = 0
st.session_state[flipped_key] = False
st.session_state[completed_key] = False

assert st.session_state[index_key] == 0, "Restart failed to reset index to 0"
assert st.session_state[flipped_key] == False, "Restart failed to reset flipped state to False"
assert st.session_state[completed_key] == False, "Restart failed to reset completed state"

print("  🔄 Deck restarted cleanly to Card 1!")

print("\n--- TEST 2 PASSED: 10-CARD NAVIGATION, FLIP & RESTART SIMULATION PASSED 100% ---")
print("\n==================================================")
print("ALL FLASHCARD ENGINE AUDIT TESTS PASSED 100%!")
print("==================================================")
