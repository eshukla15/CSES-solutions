import json
from datetime import datetime

class ProblemSolvingJournal:
    def __init__(self, filename="cf_journey.json"):
        self.filename = filename
        try:
            with open(self.filename, 'r') as f:
                self.logs = json.load(f)
        except FileNotFoundError:
            self.logs = []

    def log_problem(self, platform, title, difficulty, key_insight, struggled_with):
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "platform": platform,
            "title": title,
            "difficulty": difficulty,
            "key_insight": key_insight,  # The "Aha!" moment
            "struggled_with": struggled_with, # What to review later
        }
        self.logs.append(entry)
        self.save_logs()
        print(f"Great job! Focused on the 'Why' for: {title}")

    def save_logs(self):
        with open(self.filename, 'w') as f:
            json.dump(self.logs, f, indent=4)

# Example Usage:
journal = ProblemSolvingJournal()

# Use this after finishing a problem to cement the logic
journal.log_problem(
    platform="Codeforces",
    title="Maximum Subarray Sum",
    difficulty="1200",
    key_insight="If the prefix sum becomes negative, it's better to start a new subarray.",
    struggled_with="Handling the case where all numbers are negative."
)