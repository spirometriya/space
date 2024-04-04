import requests
import os
from urllib.parse import urlparse, unquote

image_folder = f"{os.getcwd()}\\images"


def get_file_extension(url):
    filename = unquote(urlparse(url).path)
    extension = os.path.splitext(filename)[1]
    return extension


def download_picture(url, path, file_name, api_key=None):
    payload = {"api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(f"{path}\\{file_name}", mode="wb") as file:
        file.write(response.content)
