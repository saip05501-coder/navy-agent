from scraper import fetch_news
from notifier import send_email
import time

def run():
    print("Fetching Navy News...")

    news = fetch_news()

    if news:
        print("Sending email...")
        send_email(news)
    else:
        print("No news found")

if __name__ == "__main__":
    while True:
        run()
        print("Sleeping for 7 days...")
        time.sleep(7 * 24 * 60 * 60)  # 7 days