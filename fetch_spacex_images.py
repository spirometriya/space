import argparse
import fetch_image_utils as common
import requests
from pathlib import Path

SPACEX_API_URL = "https://api.spacexdata.com/v5/launches/"


def main(launch_id):
    response = requests.get(f"{SPACEX_API_URL}{launch_id}")
    response.raise_for_status()
    urls = response.json().get("links").get("flickr").get("original")
    for url_number, url in enumerate(urls):
        extension = common.get_file_extension(url)
        common.download_picture(
            url, common.IMAGE_FOLDER, f"spacex_{url_number}{extension}"
        )


if __name__ == "__main__":
    Path(common.IMAGE_FOLDER).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description="Downloads images of SpaceX launches to user's computer"
    )
    parser.add_argument(
        "-id",
        help="Specify the launch id to download images of this launch only (optional, default=latest)",
        default="latest",
    )
    args = parser.parse_args()
    launch_id = args.id
    main(launch_id)
    print("SpaceX images have been downloaded")
