import os
import requests

from dotenv import load_dotenv
from funcs import save_image
from pathlib import Path


def fetch_nasa_apod():
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'count': 5,
        'api_key': os.environ['NASA_TOKEN']
        }
    response = requests.get(url, params=params)
    response.raise_for_status()
    response = response.json()

    for number, apod in enumerate(response, start=1):
        image_name = f'nasa_apod{number}.jpg'
        image_url = apod['url']
        file_path = path + image_name
        save_image(file_path, image_url)


if __name__ == '__main__':
    load_dotenv()
    path = './images/'
    Path(path).mkdir(parents=False, exist_ok=True)
    
    try:
        fetch_nasa_apod()
    except requests.exceptions.HTTPError as error:
        exit(f"Can't get data from server: {error}")