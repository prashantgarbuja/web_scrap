#Web Scrapping Top Google trends in Australia
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import time

# Set up Chrome options with web browser pop-up disabled
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu') 

# URL to scrape top daily trends in Australia
url = "https://trends.google.com/trends/trendingsearches/daily?geo=AU&hl=en-US"
driver = webdriver.Chrome(options=chrome_options) 

driver.get(url)

time.sleep(5)

page_source = driver.page_source

# Close the Selenium WebDriver
driver.quit()  

soup = BeautifulSoup(page_source, 'html.parser')

trending_topics = soup.find_all('div', class_='details-top')

searches = soup.find_all('div', class_='search-count-title')

file_name = 'Google Trends.csv'

with open(file_name, 'w',
            newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Google Top Trends in Australia'])
    csvwriter.writerow(
            ['Rank',
             'Trending Topic', 
            'Views']
            )
    
    for index, (trending_topic, search) in enumerate(zip(trending_topics, searches), start=1):
            csvwriter.writerow(
                [index, 
                trending_topic.text.strip(), 
                search.text.strip()]
                )
