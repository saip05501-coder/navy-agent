import requests
from bs4 import BeautifulSoup
from config import NAVY_URL

def fetch_news():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            NAVY_URL,
            headers=headers,
            timeout=(5, 10)  # (connect timeout, read timeout)
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        news_data = []
        news_items = soup.find_all("li")

        for item in news_items:
            text = item.get_text(" ", strip=True)
            if len(text) > 30:
                news_data.append(text)

        return news_data

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []