import argparse
import os
import random
import requests
import telegram
import time
import fetch_image_utils as common
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Post all images to telegram from user's computer"
    )
    parser.add_argument(
        "-step",
        type=float,
        help="Specify the number of hours after which the script will be restarted (optional, default=4)",
        default=4,
    )
    args = parser.parse_args()
    step = args.step
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    while True:
        images = common.get_valid_images()
        random.shuffle(images)
        for image in images:
            try:
                with open(f"{common.IMAGE_FOLDER}{image}", "rb") as file:
                    bot.send_document(chat_id=chat_id, document=file)
                print("The image has been successfully posted to telegram")
            except requests.HTTPError:
                print("Post image error - check the validity of token and chat-id")
        time.sleep(step * 3600)
