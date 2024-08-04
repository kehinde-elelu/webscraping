'''
Reference: 
https://www.scrapingbee.com/blog/undetected-chromedriver-python-tutorial-avoiding-bot-detection/
https://github.com/ultrafunkamsterdam/nodriver
https://ultrafunkamsterdam.github.io/nodriver/nodriver/quickstart.html#usage-example
'''


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import csv
import os
import asyncio
import nodriver as uc

base_path = "/Users/kehindeelelu/Documents/ETS/webscraping/data"

stateNames = ['Arkansas']
#   'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
#   'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
#   'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 
#   'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 
#   'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
#   'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Utah', 
#   'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
# ]

for state in stateNames:
    os.makedirs(f'{base_path}/html_files/{state}/', exist_ok=True)

    base_url = f"https://www.careerbuilder.com/jobs?location={state}&page_number="
    start_number = 0

    def bf_scrap(html, url):
        job_listings = []
        # Get page source and parse with BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)

        filename = url.split('=')[-1]
        # save as a html
        with open(f'{base_path}/html_files/{state}/{filename}.txt', 'w', encoding='utf-8') as file:
            file.write(str(soup))

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
        return job_listings

    def save_dl(job_list):
        if os.path.exists('data/job_listings.csv'):
            # Open the CSV file in append mode and add new rows
            with open('data/job_listings.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for job in job_list:
                    writer.writerow(job.values())
            print("Added new rows")
        else:
            # Convert the job listings to a DataFrame and save to CSV
            job_df = pd.DataFrame(job_list)
            job_df.to_csv('data/job_listings.csv', index=False, encoding='utf-8')
            print("Created a new dataset and added new rows")

    async def scrapping_website(url):
        try:
            pages_detail = {}
            browser = await uc.start()
            for index, url_ in enumerate(url):
                time.sleep(2)
                if index == 0:
                    pages_detail[url_] = await browser.get(url_)
                else:
                    pages_detail[url_] = await browser.get(url_, new_tab=True)
        
            time.sleep(240)
            
            html_ = {}
            # await page.save_screenshot()
            for page_url, page in pages_detail.items():
                html_[page_url] = await page.get_content()

            # print(html_)

            jl_ = []
            for page_url, html in html_.items():
                jl_.append(bf_scrap(html, page_url))
            print(len(jl_))

        except Exception as e:
            print("Error 2:", e)
        
        return jl_


    # for i in range(1, 2, 1):  
    # time.sleep(30)
    try: 
        # Scrape the website
        url = [f"{base_url}{start_number + i}" for i in range(98)]
        # print(url)
        # print(url[0], url[1], url[2])
        jl_ = uc.loop().run_until_complete(scrapping_website(url))

        for jl in jl_:
            save_dl(jl)

        for i in url:
            print(f"Number: {i.split("=")[-1]} added successfully")

        start_number = int(url[-1].split("=")[-1]) + 1
        time.sleep(5)
    except Exception as e:
        print("Error 1:", e)

    print("Job listings have been saved to 'data/job_listings.csv'.")

    time.sleep(240)


