import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import nodriver as uc
import csv
import os
import re


# answer = "yes, the job description mentions the skill 'oral communication skills'. the specific words that indicate this are 'exceptional communication skills, both verbal and written.' this matches because 'verbal' communication refers to spoken language, which is a part of oral communication skills."

# # if answer.lower().startswith('yes'):
# #     answer_split = answer.split(',', 1)  # Split the response into two parts
# #     print(answer_split[0])
# #     skill_presence = 'Yes'
# #     skill_description = answer_split[1].strip() if len(answer_split) > 1 else "No relevant word found"
# # else:
# #     skill_presence = 'No'
# #     skill_description = "No relevant word found"

# print(answer[:5])


# # Use regex to find 'yes'
# match = re.search(r'\byes\b', answer[:6], re.IGNORECASE)
# if match:
#     result = "yes"
# else:
#     result = "no"


df = pd.read_csv('/Users/kehindeelelu/Documents/ETS/webscraping/data/job_listings.csv')
print(len(df))