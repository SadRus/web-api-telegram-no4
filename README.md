# Upload universe photos to Telegram.
### Description

Script upload photo about space in telegram within telegram bot. 
Photo downloaded from "images/" folder, after you get them with python scripts.
Scripts use API SpaceX, NASA APOD and NASA EPIC.

### Objective of project

Script written for educational purposes within online courses for web developers [dvmn.org](https://dvmn.org/).

### Installing

Python3 must be installed. 
Use `pip` (or `pip3`) for install requirements:
```
pip install -r requirements.txt
```

### Enviroment

You needs to create .env file in main folder for enviroment variables.

NASA_TOKEN - for downloading photo.

TG_BOT_TOKEN - you need to create telegram bot via @bot_father and get bot token.

SEND_PHOTO_DELAY - you can custom delay between send photo by change this variable.

### Download photos to folder

For downloading photos in folder you can use:
Download 5 random NASA A Picture Of Day
```
python(or python3) fetch_nasa_apod_images.py
```

Download 11 image of Earth from Earth Polychromatic Imaging Camera
```
python(or python3) fetch_nasa_epic_images.py
```

Download latest SpaceX launch images.
```
python(or python3) fetch_spacex_images.py
```

You can download SpaceX images by launch id. Launch id 5eb87d42ffd86e000604b384 for example.
```
python(or python3) fetch_spacex_images.py --launch_id 5eb87d42ffd86e000604b384
```
### Usage

Upload photo to telegram every 4 hours by default, you can change it in enviroment variables.

From scripts folder:
```
python(or python3) main.py
```