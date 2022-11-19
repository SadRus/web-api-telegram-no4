import os
import requests

from dotenv import load_dotenv
from funcs import save_image
from pathlib import Path


def fetch_nasa_epic():
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {
        'api_key': os.environ['NASA_TOKEN']
        }
    response = requests.get(url, params=params)
    response.raise_for_status()
    response = response.json()

    for number, image_info in enumerate(response, start=1):
        image = image_info['image']
        date = image_info['date'].split()[0]
        date = date.replace('-', '/')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={params["api_key"]}'
        image_name = f'nasa_epic{number}.png'
        file_path = path + image_name
        save_image(file_path, image_url)

if __name__ == '__main__':
    load_dotenv()
    path = './images/'
    Path(path).mkdir(parents=False, exist_ok=True)
    
    try:
        fetch_nasa_epic()
    except requests.exceptions.HTTPError as error:
        exit(f"Can't get data from server: {error}")
