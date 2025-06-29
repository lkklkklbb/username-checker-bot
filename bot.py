import requests
import time
from telegram import Bot
import os

# أخذ التوكن والآي دي من متغيرات البيئة
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def send_telegram_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

def check_username_availability(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    return response.status_code == 404

def generate_usernames():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c1 in chars:
        for c2 in chars:
            for c3 in chars:
                for c4 in chars:
                    yield c1 + c2 + c3 + c4

def main():
    for username in generate_usernames():
        if check_username_availability(username):
            msg = f"✅ يوزر متاح: {username}"
            print(msg)
            send_telegram_message(msg)
            time.sleep(3600)  # انتظار بعد العثور على يوزر
        else:
            print(f"مفحوص: {username}")
        time.sleep(1)

if __name__ == "__main__":
    main()
