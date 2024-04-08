import fetch_image_utils as common
import os
import requests
from dotenv import load_dotenv
from pathlib import Path

NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"


def fetch_nasa_apods(api_key):
    payload = {"api_key": api_key, "count": "30"}
    response = requests.get(NASA_APOD_URL, params=payload)
    response.raise_for_status()
    urls = [apod.get("url") for apod in response.json()]
    for url_number, url in enumerate(urls):
        extension = common.get_file_extension(url)
        common.download_picture(
            url, common.image_folder, f"nasa_apod_{url_number}{extension}"
        )


if __name__ == "__main__":
    load_dotenv()
    Path(common.image_folder).mkdir(parents=True, exist_ok=True)
    nasa_apy_key = os.environ["NASA_API_KEY"]
    try:
        fetch_nasa_apods(nasa_apy_key)
        print("APOD images have been downloaded")
    except requests.HTTPError:
        print("Failed to download APOD images")
