import pandas as pd
import csv

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/kehindeelelu/Documents/ETS/webscraping/data/skills/updated_job_listings.csv')

# List of skills to check
skills = [
    'oral_communication_skills', 'written_communication_skills', 'collaboration', 'problem_solving', 'communication_skills',
    'social_intelligence', 'self_direction', 'critical_thinking', 'time_management', 'negotiation', 'ethics', 'professionalism',
    'creativity', 'work_ethic', 'adaptability', 'service_orientation', 'continual_learning', 'resilience', 'cultural_sensitivity'
]

# Initialize a dictionary to store the count of 'yes' for each skill
yes_count = {}

# Loop through each skill and count the occurrences of 'yes'
for skill in skills:
    yes_count[skill] = df[skill].str.lower().eq('yes').sum()

print(yes_count)

# Specify the file name
filename = "/Users/kehindeelelu/Documents/ETS/webscraping/data/count_log.csv"

# Writing to the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Writing the headers
    writer.writerow(["Skill", "Count"])
    
    # Writing the data
    for skill, count in yes_count.items():
        writer.writerow([skill, count])

print(f"Data saved to {filename}")