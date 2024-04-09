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
    parser = argparse.ArgumentParser()
    parser.add_argument("-step", help="Script launch step (hours)", default=4)
    args = parser.parse_args()
    step = args.step
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    posted_images = set()
    while True:
        images = common.get_list_of_images()
        if set(images) == posted_images:
            random.shuffle(images)
            posted_images = set()
        for image in images:
            try:
                bot.send_document(
                    chat_id=os.environ["CHAT_ID"],
                    document=open(f"{common.IMAGE_FOLDER}{image}", "rb"),
                )
                print("The image has been successfully posted to telegram")
                posted_images.add(image)
            except requests.HTTPError:
                print("Post image error - check the validity of token and chat-id")
        time.sleep(float(step) * 3600)
