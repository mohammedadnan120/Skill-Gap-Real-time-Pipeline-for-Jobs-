import pandas as pd
import random

#1.List of companies and job titles in Saudi Arabia and Jordan :
companies = ["STC", "Aramco", "Tahakom", "Thiqah", "Tamara", "Salla", "Amazon Riyadh", "Zain Jordan", "Orange Jordan", "Expedia Amman"]
job_titles = ["Data Engineer", "Junior Python Developer", "Data Analyst", "Backend Engineer", "Big Data Specialist"]

# 2. List of skills (which the code will later search for :
skills_pool = [
    "Python, SQL, AWS, Docker",
    "Pandas, NumPy, SQL, Tableau",
    "Spark, Hadoop, Python, ETL",
    "SQL, Python, Google Cloud, Airflow",
    "Python, Flask, Docker, SQL",
    "Data Pipelines, Python, AWS, Spark",
    "SQL, Excel, Python, Power BI"
]

# 3.Create 50 random job descriptions (Mock Data) :
data = []
for i in range(50):
    row = {
        "Job_Title": random.choice(job_titles),
        "Company": random.choice(companies),
        "Required_Skills": random.choice(skills_pool)
    }
    data.append(row)

# 4.Convert it to DataFrame :
df = pd.DataFrame(data)

# 5.View the first 5 rows to confirm :
print("--- Data for 50 jobs was successfully created ---")
print(df.head())

#-Save it to a CSV file to begin the next stage
df.to_csv("job_market_data.csv", index=False)


