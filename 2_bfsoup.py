import pandas as pd
import undetected_chromedriver as uc
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random

# Set up undetected_chromedriver with Selenium
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)

job_detail = []

def scrapping_website(row, skill=None, place=None):
    try:
        driver.get(row['URL'])
        
        # Add a random delay to mimic human behavior
        time.sleep(random.uniform(1, 3))
        
        # Ensure the page has fully loaded
        time.sleep(5)  # Increase if the site loads slowly
        
        # Get page source and parse with BeautifulSoup
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Find the div with id='jdp-pane'
        job_card = soup.find('div', id='jdp-pane')

        if job_card:
            # Parse salary information
            salary_div = job_card.find('div', class_='data-snapshot', id='cb-salcom-info')
            if salary_div and salary_div.find('i'):
                salary = salary_div.find('i').get_text(strip=True)
            else:
                salary = 'Not specified'

            # Parse recommended skills
            recommended = []
            recommended_skills = job_card.find('ul', class_='pl0 no-marker')
            if recommended_skills:
                recommended_skills = recommended_skills.find_all('li')
                for li in recommended_skills:
                    recommended.append(li.text.strip())
            else:
                recommended = 'Not specified'

            job_description = job_card.find('div', class_='col big col-mobile-full jdp-left-content')
            job_description = BeautifulSoup(str(job_description), "lxml").text

            # Append job details to the list
            job_detail.append({
                'Title': row['Title'],
                'Company_Name': row['Company'],
                'Location': row['Location'],
                'Type': row['Type'],
                'Job Description': job_description,
                'website': row['URL'],
                'Salary': salary,
                'Recommended': recommended,
            })
        else:
            print("No job card found with id='jdp-pane'")

    except Exception as e:
        print("Error is:", e)

    return job_detail


# Path to your CSV file
csv_file_path = '/Users/kehindeelelu/Documents/ETS/webscraping_v1/data/job_listings.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Iterating using iterrows()
for index, row in df.head(1).iterrows():
    # Scrape the website
    job_detail_ = scrapping_website(row)
    time.sleep(5)

# Convert the job listings to a DataFrame and display
job_df = pd.DataFrame(job_detail_)
print(job_df)


# Save the DataFrame to a CSV file
output_csv_file_path = '/Users/kehindeelelu/Documents/ETS/webscraping_v1/data/scraped_job_listings.csv'
job_df.to_csv(output_csv_file_path, index=False)

# Close the WebDriver
driver.quit()
