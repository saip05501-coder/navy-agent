import requests
from bs4 import BeautifulSoup
from config import NAVY_URL

def fetch_news():
    response = requests.get(NAVY_URL, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    news_data = []

    # 🔥 Find NEWS section (based on <li>)
    news_items = soup.find_all("li")

    for item in news_items:
        text = item.get_text(" ", strip=True)

        # Filter only meaningful news lines
        if len(text) > 30:   # avoids small menu items
            news_data.append(text)

    return news_data