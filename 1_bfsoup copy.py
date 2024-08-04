import undetected_chromedriver as uc
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import csv
import os

# Set up undetected_chromedriver with Selenium
options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"')
options.add_argument("https:www.google.com")
driver = uc.Chrome(options=options)

job_listings = []

def scrapping_website(url):
    try:
        driver.get(url)
        
        # Add a random delay to mimic human behavior
        time.sleep(random.uniform(1, 3))
        
        # Ensure the page has fully loaded
        time.sleep(5)  # Increase if the site loads slowly
        
        # Get page source and parse with BeautifulSoup
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find all job cards
        job_cards = soup.find_all('li', class_='data-results-content-parent')

        for job_card in job_cards:
            title = job_card.find('div', class_='data-results-title').text.strip() if job_card.find('div', class_='data-results-title') else None 
            company = job_card.find_all('span')[0].text.strip() if job_card.find_all('span')[0] else None 
            location = job_card.find_all('span')[1].text.strip() if job_card.find_all('span')[1] else None 
            job_type = job_card.find('div', class_='data-details').find_all('span')[2].text.strip() if job_card.find('div', class_='data-details').find_all('span')[2] else None 
            job_url = job_card.find('a')['href'].strip() if job_card.find('a') else None 

            job_listings.append({
                'Title': title,
                'Company': company,
                'Location': location,
                'Type': job_type,
                'URL': f"https://www.careerbuilder.com{job_url}",
                "Reference": url
            })
    except Exception as e:
        print("Error 2:", e)
    
    return job_listings


for i in range(7, 9, 1):  
    time.sleep(30)
    try: 
        # Scrape the website
        url = f"https://www.careerbuilder.com/jobs?posted=30&page_number={i}"
        job_listings = scrapping_website(url)
        # print(job_listings)

        if os.path.exists('data/job_listings.csv'):
            # Open the CSV file in append mode and add new rows
            with open('data/job_listings.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for job in job_listings:
                    writer.writerow(job.values())
            print("Added new rows")
        else:
            # Convert the job listings to a DataFrame and save to CSV
            job_df = pd.DataFrame(job_listings)
            job_df.to_csv('data/job_listings.csv', index=False, encoding='utf-8')
            print("Created a new dataset and added new rows")

        print(f"Website number {i} added successfully - {url}")

        time.sleep(30)
    except Exception as e:
        print("Error 1:", e)

print("Job listings have been saved to 'data/job_listings.csv'.")

# Close the WebDriver
driver.quit()
