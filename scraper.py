import requests
from bs4 import BeautifulSoup
from config import NAVY_URL
import time

def fetch_news():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for attempt in range(3):  # retry 3 times
        try:
            response = requests.get(NAVY_URL, headers=headers, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            news_data = []

            # Find all list items
            news_items = soup.find_all("li")

            for item in news_items:
                text = item.get_text(" ", strip=True)

                # Filter meaningful news
                if len(text) > 30:
                    news_data.append(text)

            return news_data

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1} failed:", e)
            time.sleep(5)  # wait before retry

    print("Failed to fetch data after retries")
    return []