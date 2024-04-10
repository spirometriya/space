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


def main(api_key):
    image_url_template = "https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png"
    payload = {"api_key": api_key}
    response = requests.get(NASA_EPIC_URL, params=payload)
    response.raise_for_status()
    urls = []
    for epic_image in response.json():
        urls.append(
            image_url_template.format(
                *parse_string_date(epic_image.get("date")), epic_image.get("image")
            )
        )
    for url_number, url in enumerate(urls):
        extension = common.get_file_extension(url)
        common.download_picture(
            url, common.IMAGE_FOLDER, f"nasa_epic_{url_number}{extension}", api_key
        )


if __name__ == "__main__":
    load_dotenv()
    Path(common.IMAGE_FOLDER).mkdir(parents=True, exist_ok=True)
    nasa_apy_key = os.environ["NASA_API_KEY"]
    main(nasa_apy_key)
    print("EPIC images have been downloaded")
