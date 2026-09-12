import json
import os

os.makedirs("data/questions/polity", exist_ok=True)

easy_file = "data/questions/polity/chief_minister_state_council_of_ministers_easy.json"
medium_file = "data/questions/polity/chief_minister_state_council_of_ministers_medium.json"
hard_file = "data/questions/polity/chief_minister_state_council_of_ministers_hard.json"

print("Paths ready for 150 questions generation.")
