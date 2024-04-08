# Download and post images of space
The script allows you to download photos of space from several web service APIs and post them to the telegram group. 

# How to start

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

### Environment variables.

- NASA_API_KEY
- TELEGRAM_TOKEN
- CHAT_ID

.env example:

```
NASA_API_KEY = "d9a2CFUHACuPIoqp53OISBXID9dQL0JPtZixbVTd"
TELEGRAM_TOKEN = "6417806071:5pAcwh9SoNqJAHsIUOsU7JbJ6MEXcKf1uUB"
CHAT_ID = "@dvmn_space_images"
```
### How to get

1. Sign up [api.nasa.gov](https://api.nasa.gov/). The API key will be sent to the email you specified.
2. Register a new bot using a special bot [@BotFather](https://telegram.me/BotFather):
   - to create a new bot, send the command: /newbot
   - BotFather will prompt you to enter the name of the new bot and the username for the bot account
   - the name is displayed in the dialog box with the bot, and the username is used to link to it
   - the response message contains a token that is needed to control the bot via the API
3. Create a public group in telegram and a link to this group. A new bot must be added to this group with administrator rights.

### Run

Launch on Linux or Windows as simple

```bash
$ python fetch_spacex_images.py

# Photos from latest SpaceX launch will be downloaded to the "Images" directory of the project
# You will see

$ python fetch_spacex_images.py
SpaceX images have been downloaded

# if you want to upload photos of a particular launch, you must specify its ID using a key, for example:
$ python fetch_spacex_images.py -id 5eb87d42ffd86e000604b384
```

```bash
$ python fetch_nasa_apod_images.py  

# 30 Astronomy Picture of the Day will be downloaded to the "Images" directory of the project
# You will see

$ python fetch_nasa_apod_images.py
APOD images have been downloaded
```

```bash
$ python fetch_nasa_epic_images.py  

# Some photos from Earth Polychromatic Imaging Camera will be downloaded to the "images" directory of the project
# You will see

$ python fetch_nasa_epic_images.py
EPIC images have been downloaded
```

```bash
$ python post_image_to_tg_chat.py -filename hubble.jpeg

# Posts one image file to your telegram group. 
# You will see

$ python post_image_to_tg_chat.py -filename hubble.jpeg
The image has been successfully posted in telegram

# If you do not specify a "filename", a random file from your project folder "images" will be selected.
# If the file size exceeds 20MB, the post request will not be executed!
```

```bash
$ python post_all_images_to_tg_chat.py -step 8

# Posts all image files from "images" directory of the project to your telegram group every 8 hours.
# You will see

$ python post_all_images_to_tg_chat.py -step 8
The image has been successfully posted in telegram
The image has been successfully posted in telegram
The image has been successfully posted in telegram

# If the "step" parameter is omitted, the script will run every 4 hours by default.
# If all the photos from the directory have already been published, the script starts posting them again, shuffling the photos in random order.
# If the file size exceeds 20 MB, the post request for this image will not be executed!
```

# Project Goals

This code was written for educational purposes as part of an online course for web developers at dvmn.org.