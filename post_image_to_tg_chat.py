import argparse
import os
import requests
import telegram
import fetch_image_utils as common
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Post image to telegram from user's computer"
    )
    parser.add_argument(
        "-filename",
        help="Specify name of file with extension (optional, a random picture will be selected by default)",
        default=common.get_random_image(),
    )
    args = parser.parse_args()
    filename = args.filename
    if common.check_file_size(filename):
        bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
        try:
            bot.send_document(
                chat_id=os.environ["TELEGRAM_CHAT_ID"],
                document=open(f"{common.IMAGE_FOLDER}{filename}", "rb"),
            )
            print("The image has been successfully posted in telegram")
        except requests.HTTPError:
            print("Post image error - check the validity of token and chat-id")
