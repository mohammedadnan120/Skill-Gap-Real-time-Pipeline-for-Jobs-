import pandas as pd

# 1. Load the data created in the first stage
df = pd.read_csv("job_market_data.csv")

# 2. List of skills to track
my_skills_to_check = ['Python', 'SQL', 'AWS', 'Pandas', 'Spark', 'Docker', 'ETL']

# 3. Skill Extraction & Ranking
# Create a dictionary to store the results
skill_counts = {}

for skill in my_skills_to_check:
    # Search for the skill within the 'Required_Skills' column and count occurrences
    count = df['Required_Skills'].str.contains(skill, case=False).sum()
    skill_counts[skill] = count

# Convert results into a DataFrame for better readability
rank_df = pd.DataFrame(list(skill_counts.items()), columns=['Skill', 'Frequency'])
rank_df = rank_df.sort_values(by='Frequency', ascending=False)

print("--- Ranking of Most In-Demand Skills in the Market ---")
print(rank_df)

# 4. Gap Analysis
# Assuming these are your current skills (e.g., from courses)
my_current_skills = ['Python', 'SQL', 'Pandas']

print("\n--- Skill Gap Analysis ---")
for skill in my_skills_to_check:
    if skill not in my_current_skills:
        demand = skill_counts[skill]
        print(f" Missing Skill: {skill} (Required in {demand} jobs)")
