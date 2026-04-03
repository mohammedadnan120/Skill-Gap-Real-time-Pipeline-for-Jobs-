import pandas as pd
import sqlite3

# 1. Extract: Load the data created previously
df = pd.read_csv("job_market_data.csv")

# 2. Transform: Analyze skills and calculate frequency
my_skills_to_check = ['Python', 'SQL', 'AWS', 'Pandas', 'Spark', 'Docker', 'ETL']
skill_counts = {}

for skill in my_skills_to_check:
    count = df['Required_Skills'].str.contains(skill, case=False).sum()
    skill_counts[skill] = count

# Create the DataFrame (rank_df is defined here)
rank_df = pd.DataFrame(list(skill_counts.items()), columns=['Skill', 'Frequency'])
rank_df = rank_df.sort_values(by='Frequency', ascending=False)

# 3. Load: Save results into a SQL database
conn = sqlite3.connect('Skill_Market.db')

# Now rank_df is defined and no error will occur
rank_df.to_sql('Skill_Demand_Analysis', conn, if_exists='replace', index=False)

print("--- ✅ Analysis and Storage in SQL Completed Successfully ---")
print(rank_df)

# Close the connection
conn.close()
