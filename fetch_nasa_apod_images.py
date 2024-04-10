import fetch_image_utils as common
import os
import requests
from dotenv import load_dotenv
from pathlib import Path

NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"
IMAGE_COUNT = 30


def main():
    load_dotenv()
    Path(common.IMAGE_FOLDER).mkdir(parents=True, exist_ok=True)
    api_key = os.environ["NASA_API_KEY"]
    payload = {"api_key": api_key, "count": IMAGE_COUNT}
    response = requests.get(NASA_APOD_URL, params=payload)
    response.raise_for_status()
    urls = [apod.get("url") for apod in response.json()]
    for url_number, url in enumerate(urls):
        extension = common.get_file_extension(url)
        common.download_picture(
            url, common.IMAGE_FOLDER, f"nasa_apod_{url_number}{extension}"
        )
        print("APOD images have been downloaded")


if __name__ == "__main__":
    main()
