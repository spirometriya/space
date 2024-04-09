import random
import requests
import os
from urllib.parse import urlparse, unquote

IMAGE_FOLDER = f"{os.getcwd()}\\images\\"
MAX_FILE_SIZE = 20000000


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


def get_images():
    all_images = list(os.walk(IMAGE_FOLDER))[0][2]
    return [image for image in all_images if check_file_size(image)]


def get_random_image():
    files = list(os.walk(IMAGE_FOLDER))[0][2]
    return random.choice(files)


def check_file_size(filename):
    file_size = os.path.getsize(f"{IMAGE_FOLDER}{filename}")
    if file_size < MAX_FILE_SIZE:
        return True
