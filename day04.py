student_profile = {
    "name": "Kunal",
    "role": "Aspiring AI/ML Engineer",
    "streak_days": 4,
    "skills": ["Python", "Git", "Problem Solving"]
}

print("Profile Details")
print(f"Name: {student_profile['name']}")
print(f"Goal: {student_profile['role']}")
print(f"Current Streak: {student_profile['streak_days']} days")
print(f"Skills: {', '.join(student_profile['skills'])}")

student_profile["streak_days"] += 1
student_profile["github_status"] = "Active"

text = "consistency is key to mastering machine learning"
char_frequency = {}

for char in text:
    if char != " ":  # Ignore spaces
        char_frequency[char] = char_frequency.get(char, 0) + 1

print("\n--- Character Frequency Analysis ---")
for character, count in sorted(char_frequency.items()):
    print(f"'{character}': {count}")

most_common = max(char_frequency, key=char_frequency.get)
print(f"\nMost frequent character: '{most_common}' ({char_frequency[most_common]} times)")