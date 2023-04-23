import requests
from bs4 import BeautifulSoup
from googlesearch import search
import time

# define search query
query = "bollywood actress"

# set number of search results to return
num_results = 100

# perform Google search
search_results = search(query, num_results=num_results)

# retrieve image URLs
image_urls = []
for url in search_results:
    # add delay to avoid rate limiting
    time.sleep(0.1)


    # retrieve HTML content of URL
    response = requests.get(url)

    # parse HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # find all image tags and extract image URLs
    images = soup.find_all("img")
    for image in images:
        image_url = image.get("src")
        if image_url and image_url.startswith("http"):
            image_urls.append(image_url)

print(image_urls)
