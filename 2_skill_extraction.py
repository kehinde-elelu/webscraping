import pandas as pd
from openai import OpenAI
import json 
import re
from tqdm import tqdm

# Load configuration
with open('config.json', 'r') as f:
    config = json.load(f)

client = OpenAI(api_key=config['OPENAI_API_KEY'])
import json 


# Set your OpenAI API key

# List of skills to match
skill_match = [
    'oral_communication_skills', 'written_communication_skills', 'collaboration', 'problem_solving', 'communication_skills',
    'social_intelligence', 'self_direction', 'critical_thinking', 'time_management', 'negotiation', 'ethics', 'professionalism',
    'creativity', 'work_ethic', 'adaptability', 'service_orientation', 'continual_learning', 'resilience', 'cultural_sensitivity'
]


# Function to check if a skill is in the job description
def check_skill_in_description(skill, description):
    answer = []
    # prompt = f"Does the following job description mention a skill related to '{skill}' or a similar concept? If yes, identify the specific word(s) or phrases that imply this skill and briefly explain why it matches. Respond with 'Yes' or 'No' followed by the word(s) and reason. Job Description: {description}"
    # prompt = f"Does the following job description mention a skill related to '{skill}' or a similar concept? If yes, identify the specific word(s) or phrases that imply this skill. Respond with 'Yes' or 'No' followed by the specific word(s). Job Description: {description}"
    prompt = f"Does the following job description mention a skill related to '{skill}' or a similar concept? If yes, Respond with only 'Yes' or 'No'. Job Description: {description}"

    # Call the OpenAI API to get the model's response
    # response = client.chat.completions.create(
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,  # Adjust based on the desired response length
        temperature=0.7  # Adjust the creativity level)
    )

    # Extract the answer and reason from the response
    answer.append(response.choices[0].message.content.strip())
    match = re.search(r'\byes\b', answer[0][:6], re.IGNORECASE)
    skill_presence = "no"
    if answer and match:
        skill_presence = 'yes'
    
    return skill_presence, answer[0]


df = pd.read_csv('/Users/kehindeelelu/Documents/ETS/webscraping/data/job_listings.csv')
# print(len(df['job_description']))

# Check and add columns if they don't exist
for skill in skill_match:
    if f'{skill}' not in df.columns:
        df[f'{skill}'] = ''
    if f'{skill}_Description' not in df.columns:
        df[f'{skill}_Description'] = ''

start_point = 11
end_point = 50
file_name = 'version2'
df = df[start_point:end_point].copy()
# try:
for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing Rows"):
    # print(index)
    results = []
    for skill in skill_match:
        skill_presence, skill_description = check_skill_in_description(skill, row['job_description'])
        results.append({f'{skill}': skill_presence, f'{skill}_Description': skill_description})

        df.at[index, f'{skill}'] = skill_presence
        df.at[index, f'{skill}_Description'] = skill_description

# Save the updated DataFrame to a new CSV file
df.to_csv(f'/Users/kehindeelelu/Documents/ETS/webscraping/data/skills/updated_job_listings_{file_name}.csv', index=False)

# except Exception as e:
#     print("Error 1:", e)
