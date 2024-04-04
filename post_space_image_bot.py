import os
import telegram
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    bot.send_message(chat_id=os.environ["CHAT_ID"], text="I'm sorry Dave I'm afraid I can't do that.")
