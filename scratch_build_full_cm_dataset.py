import json
import os

# Ensure target directories exist
os.makedirs("data/questions/polity", exist_ok=True)

easy_path = "data/questions/polity/chief_minister_state_council_of_ministers_easy.json"
medium_path = "data/questions/polity/chief_minister_state_council_of_ministers_medium.json"
hard_path = "data/questions/polity/chief_minister_state_council_of_ministers_hard.json"

print("Target paths ready.")
