import datetime
import fetch_image_utils as common
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

NASA_EPIC_URL = "https://api.nasa.gov/EPIC/api/natural"


def parse_string_date(date):
    parsed_date = datetime.datetime.fromisoformat(date).strftime("%Y,%m,%d")
    return parsed_date.split(",")


def fetch_nasa_epics(api_key):
    template_img_url = "https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png"
    payload = {"api_key": api_key}
    response = requests.get(NASA_EPIC_URL, params=payload)
    response.raise_for_status()
    urls = []
    for r in response.json():
        urls.append(
            template_img_url.format(*parse_string_date(r.get("date")), r.get("image"))
        )
    for url_number, url in enumerate(urls):
        extension = common.get_file_extension(url)
        common.download_picture(
            url, common.image_folder, f"nasa_epic_{url_number}{extension}", api_key
        )


if __name__ == "__main__":
    load_dotenv()
    Path(common.image_folder).mkdir(parents=True, exist_ok=True)
    nasa_apy_key = os.environ["NASA_API_KEY"]
    try:
        fetch_nasa_epics(nasa_apy_key)
        print("EPIC images have been downloaded")
    except requests.HTTPError:
        print("Failed to download EPIC images")
