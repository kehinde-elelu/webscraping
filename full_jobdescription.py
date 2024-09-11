import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import nodriver as uc
import csv
import os

base_path = '/Users/kehindeelelu/Documents/ETS/webscraping/data'

# Path to your CSV file
csv_file_path = f'{base_path}/job_listings.csv'



def bf_scrap(html, row):
    job_detail = []
    # Get page source and parse with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with id='jdp-pane'
    job_card = soup.find('div', id='jdp-pane')

    if job_card:
        # Parse salary information
        salary_div = job_card.find('div', class_='data-snapshot', id='cb-salcom-info') if job_card.find('div', class_='data-snapshot', id='cb-salcom-info') else None 
        if salary_div and salary_div.find('i'):
            salary = salary_div.find('i').get_text(strip=True)
        else:
            salary = 'Not specified'

        # Parse recommended skills
        recommended = []
        recommended_skills = job_card.find('ul', class_='pl0 no-marker') if job_card.find('ul', class_='pl0 no-marker') else None 
        if recommended_skills:
            recommended_skills = recommended_skills.find_all('li')
            for li in recommended_skills:
                recommended.append(li.text.strip())
        else:
            recommended = 'Not specified'

        job_description = job_card.find('div', class_='col big col-mobile-full jdp-left-content') if job_card.find('div', class_='col big col-mobile-full jdp-left-content') else None
        job_description = BeautifulSoup(str(job_description), "lxml").text

        # Append job details to the list
        job_detail.append({
            'Title': row['Title'],
            'Company_Name': row['Company'],
            'Location': row['Location'],
            'Type': row['Type'],
            'Job_Description': job_description,
            'website': row['URL'],
            'Salary': salary,
            'Recommended': recommended,
        })

        # print(job_detail)
    return job_detail

async def scrapping_website(index, url, row, browser):
    pages_detail = {}
    if index == 0:
        pages_detail[url] = await browser.get(url)
    else:
        pages_detail[url] = await browser.get(url, new_tab=True)

    html_ = {}
    for page_url, page in pages_detail.items():
        time.sleep(10)
        html_[page_url] = await page.get_content()

    jl_ = []
    for page_url, html in html_.items():
        job_extract = bf_scrap(html, row)
        if job_extract:
            jl_.extend(job_extract)  # Ensure to add to the list
    # if not jl_:
    #     print("Empty Array")
    if jl_:
        return jl_[0]
    return None

def save_dl(job_desp):
    file_path = f'{base_path}/scraped_job_listings.csv'
    
    if os.path.exists(file_path):
        # Append to existing CSV file
        existing_df = pd.read_csv(file_path)
        new_df = pd.DataFrame([job_desp])
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        combined_df.to_csv(file_path, index=False, encoding='utf-8')
        print("Added new rows to existing dataset")
    else:
        # Create a new CSV file and save the data
        job_df = pd.DataFrame([job_desp])
        job_df.to_csv(file_path, index=False, encoding='utf-8')
        print("Created a new dataset and added new rows")

async def main():
    start_csv = 115580
    for i in range(1, 30):
        # Read the header first
        header_df = pd.read_csv(csv_file_path, nrows=0)
        df = pd.read_csv(csv_file_path, skiprows=start_csv, nrows=100, header=None)
        df.columns = header_df.columns
        # print(df)
        time.sleep(5)
        browser = await uc.start()
        # print(len(df))
        for index, row in df.iterrows():
            jl_ = await scrapping_website(index, row['URL'], row, browser)

            # print(jl_)
            if jl_ is not None:
                # Save the DataFrame to a CSV file
                save_dl(jl_)
        time.sleep(2)
        browser.stop()
        start_csv += 100
        print(start_csv)
        

if __name__ == '__main__':
    # since asyncio.run never worked (for me)
    uc.loop().run_until_complete(main())