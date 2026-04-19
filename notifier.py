import smtplib
from email.mime.text import MIMEText
from config import EMAIL, PASSWORD, TO_EMAIL

def send_email(news_list):
    if not news_list:
        print("No news found")
        return

    try:
        content = "📢 Indian Navy - Latest News\n\n"

        for news in news_list:
            content += f"{news}\n\n"

        msg = MIMEText(content)
        msg["Subject"] = "Navy News Update"
        msg["From"] = EMAIL
        msg["To"] = TO_EMAIL

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()

        print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ Email error:", e)