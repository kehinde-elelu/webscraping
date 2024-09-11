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
from nodriver.cdp.browser import WindowState

base_path = "/Users/kehindeelelu/Documents/ETS/webscraping/data"

stateNames = ['Washington', 'West Virginia']
#   'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
#   'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
#   'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 
#   'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 
#   'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
#   'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Utah', 
#   'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
# ]

start_, end_ = 53, 95

for state in stateNames:
    # os.makedirs(f'{base_path}/html_files/{state}/', exist_ok=True)

    base_url = f"https://www.careerbuilder.com/jobs?location={state}&page_number="
    start_number = 0

    def bf_scrap(html, url):
        job_listings = []
        # Get page source and parse with BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)

        # filename = url.split('=')[-1]
        # # save as a html
        # with open(f'{base_path}/html_files/{state}/{filename}.txt', 'w', encoding='utf-8') as file:
        #     file.write(str(soup))

        # Find all job cards
        job_cards = soup.find_all('li', class_='data-results-content-parent')

        for job_card in job_cards:
            title = job_card.find('div', class_='data-results-title').text.strip() if job_card.find('div', class_='data-results-title') else None 
            company = job_card.find_all('span')[0].text.strip() if job_card.find_all('span')[0] else None 
            location = job_card.find_all('span')[1].text.strip() if job_card.find_all('span')[1] else None 
            job_type = job_card.find('div', class_='data-details').find_all('span')[2].text.strip() if job_card.find('div', class_='data-details') and len(job_card.find('div', class_='data-details').find_all('span')) > 2 else None
            # job_type = job_card.find('div', class_='data-details').find_all('span')[2].text.strip() if job_card.find('div', class_='data-details').find_all('span')[2] else None 
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
        file_path = 'data/job_listings.csv'
    
        if os.path.exists(file_path):
            # Open the CSV file in append mode
            with open(file_path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=job_list[0].keys())
                for job in job_list:
                    writer.writerow(job)
            print("Added new rows")
        else:
            # Convert the job listings to a DataFrame and save to CSV
            job_df = pd.DataFrame(job_list)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            job_df.to_csv(file_path, index=False, encoding='utf-8')
            print("Created a new dataset and added new rows")

    async def scrapping_website(url):
        # try:
        browser = await uc.start()
        for index, url_ in enumerate(url):
            if index == 0:
                pages_detail = await browser.get(url_)
            else:
                pages_detail = await browser.get(url_, new_tab=True)
            time.sleep(5)

            job_content = await pages_detail.get_content()
            soup = BeautifulSoup(job_content, 'html.parser')
            job_cards = soup.find_all('li', class_='data-results-content-parent')

            try: 
                jobs = await pages_detail.find_all('li.data-results-content-parent')
            except Exception as e:
                print(f"Reloading this url {url_}")
                time.sleep(10)
                pages_detail = await browser.get(url_, new_tab=True)
                time.sleep(30)
                jobs = await pages_detail.find_all('li.data-results-content-parent')

            title_arr = []
            for job_card in job_cards:
                title = job_card.find('div', class_='data-results-title').text.strip() if job_card.find('div', class_='data-results-title') else None 
                title_arr.append(title)
            # print(title_arr)

            time.sleep(2)
            counting = 0
            job_listings = []
            for job in title_arr:
                # print(job)
                jobs = await pages_detail.find(f"{job}", best_match=True)
                try:
                    await jobs.mouse_click()
                    # await pages_detail.scroll_down(50)
                    time.sleep(10)
                except Exception as e:
                    print(f"Failed to click on job: {job}")
                    continue 
                    # else:
                    #     print("hidden")
                
                # print(jobs)
                # time.sleep(10)
                job_content_ = await pages_detail.get_content()
                soup_ = BeautifulSoup(job_content_, 'html.parser')
                job_card = soup_.find('div', id='jdp-pane')

                # print(job_card)

                # Parse recommended skills
                recommended = []
                recommended_skills = job_card.find('ul', class_='pl0 no-marker') if job_card.find('ul', class_='pl0 no-marker') else None 
                if recommended_skills:
                    recommended_skills = recommended_skills.find_all('li')
                    for li in recommended_skills:
                        recommended.append(li.text.strip())
                else:
                    recommended = 'Not specified'

                # print(recommended)
                
                salary_div = job_card.find('div', class_='data-snapshot', id='cb-salcom-info') if job_card.find('div', class_='data-snapshot', id='cb-salcom-info') else None 
                if salary_div and salary_div.find('i'):
                    salary = salary_div.find('i').get_text(strip=True)
                else:
                    salary = 'Not specified'
                
                job_description = job_card.find('div', class_='col big col-mobile-full jdp-left-content') if job_card.find('div', class_='col big col-mobile-full jdp-left-content') else None
                job_description = BeautifulSoup(str(job_description), "lxml").text

                # print(job_card)
                small_card = job_card.find('div', class_='data-details').find_all('span') if job_card.find('div', class_='data-details').find_all('span') else None 
                
                company = small_card[0].text.strip() if small_card[0].text.strip() else "No company name" 
                location = small_card[1].text.strip() if small_card[1].text.strip() else "No location" 
                if len(small_card) == 3:
                    job_type = small_card[2].text.strip() if small_card[2].text.strip() else "No Job type" 
                else:
                    job_type = 'NA', 'NA', 'NA'

                job_listings.append({
                    'Title': job,
                    'Company': company,
                    'Location': location,
                    'Type': job_type,
                    "Reference": url_, 
                    "salary": salary,
                    "job_description": job_description,
                    "recommended": recommended
                })
                counting += 1

                if counting == 5:
                    break
            if job_listings:
                save_dl(job_listings)
        # time.sleep(2)
        # browser.stop()
        return 


    # for i in range(1, 2, 1):  
    # time.sleep(30)
    # try: 
    # Scrape the website
    url = [f"{base_url}{start_number + i}" for i in range(start_, end_, 1)]
    # print(url)
    # print(url[0], url[1], url[2])
    jl_ = uc.loop().run_until_complete(scrapping_website(url))
    # print(jl_)
    # for jl in jl_:

    # for i in url:
    #     print(f"Number: {i.split("=")[-1]} added successfully")

    start_number = int(url[-1].split("=")[-1]) + 1
    time.sleep(5)
    # except Exception as e:
    #     print("Error 1:", e)

    print("Job listings have been saved to 'data/job_listings.csv'.")

    time.sleep(10)
    print(state)


