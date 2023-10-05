# Web scraping the top IMDB movie list. Note: Please be aware that web scraping may not be the correct tool for gathering information, you might wanna use API in some case. 
import requests
from bs4 import BeautifulSoup
import csv

#Some website doesn't allow access, so creating request as a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url = "https://www.imdb.com/chart/top"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    page_source = response.content
    soup = BeautifulSoup(
        page_source, 'html.parser')
    movie_titles = soup.find_all(
        'a', 
        class_='ipc-title-link-wrapper')
    ratings = soup.find_all(
        'span', 
        class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')

    file_name = 'IMDB Top 250 movies.csv'

    with open(file_name, 'w',
            newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(
            ['Top Movie', 
            'Rating']
            )
        
        for movie_title, rating in zip(movie_titles, ratings):
            csvwriter.writerow(
                [movie_title.text.strip(), 
                rating.text.strip()]
                )

else:
    print(f"Error: Unable to retrieve data. Status code {response.status_code}")
