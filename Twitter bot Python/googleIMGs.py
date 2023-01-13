import requests
from bs4 import BeautifulSoup
import tweepy

# Search for an image on the web
query = "a sith lord returns in cover art from the new marvel anthology series star wars"
image_url = None

# Make a request to Google Images
url = "https://www.google.com/search?q=" + query + "&tbm=isch"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

r = requests.get(url, headers=headers)

if r.status_code == 200:
    # Parse the HTML
    soup = BeautifulSoup(r.text, "html.parser")

    # Find the first image on the page
    image_tag = soup.find("img")

    if image_tag:
        image_url = image_tag["src"]
