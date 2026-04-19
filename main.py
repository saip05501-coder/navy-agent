import signal
from scraper import fetch_news
from notifier import send_email

# 🔥 Force stop after 25 seconds
def timeout_handler(signum, frame):
    raise Exception("Execution timed out")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(25)

def run():
    print("Fetching Navy News...")
    news = fetch_news()

    if news:
        send_email("\n".join(news))
        print("Email sent")
    else:
        print("No news or failed to fetch")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print("Stopped:", e)