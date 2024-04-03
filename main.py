import datetime
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse, unquote

HUBBLE_URL = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
SPACEX_API_URL = "https://api.spacexdata.com/v5/launches/latest"
NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"
NASA_EPIC_URL = "https://api.nasa.gov/EPIC/api/natural"

image_folder = f"{os.getcwd()}\\images"
hubble_file_name = "hubble.jpeg"


def get_file_extension(url):
    filename = unquote(urlparse(url).path)
    extension = os.path.splitext(filename)[1]
    return extension


def parse_string_date(date):
    parsed_date = datetime.datetime.fromisoformat(date).strftime("%Y,%m,%d")
    return parsed_date.split(",")


def download_picture(url, path, file_name, api_key=None):
    payload = {"api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(f"{path}\\{file_name}", mode="wb") as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    response = requests.get(SPACEX_API_URL)
    response.raise_for_status()
    urls = response.json().get("links").get("flickr").get("original")
    for url_number, url in enumerate(urls):
        extension = get_file_extension(url)
        download_picture(url, image_folder, f"spacex_{url_number}{extension}")


def fetch_nasa_apods(api_key):
    payload = {"api_key": api_key, "count": "30"}
    response = requests.get(NASA_APOD_URL, params=payload)
    response.raise_for_status()
    urls = [apod.get("url") for apod in response.json()]
    for url_number, url in enumerate(urls):
        extension = get_file_extension(url)
        download_picture(url, image_folder, f"nasa_apod_{url_number}{extension}")


def fetch_nasa_epics(api_key):
    template_img_url = "https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png"
    payload = {"api_key": api_key}
    response = requests.get(NASA_EPIC_URL, params=payload)
    response.raise_for_status()
    urls = []
    for r in response.json():
        urls.append(template_img_url.format(*parse_string_date(r.get("date")), r.get("image")))
    for url_number, url in enumerate(urls):
        extension = get_file_extension(url)
        download_picture(url, image_folder, f"nasa_epic_{url_number}{extension}", api_key)


if __name__ == '__main__':
    load_dotenv()
    Path(image_folder).mkdir(parents=True, exist_ok=True)
    nasa_apy_key = os.environ["NASA_API_KEY"]
    download_picture(HUBBLE_URL, image_folder, hubble_file_name)
    fetch_spacex_last_launch()
    fetch_nasa_apods(nasa_apy_key)
    fetch_nasa_epics(nasa_apy_key)
