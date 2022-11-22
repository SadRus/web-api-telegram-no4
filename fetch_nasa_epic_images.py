import os
import requests

from dotenv import load_dotenv
from funcs import save_image
from pathlib import Path


def fetch_nasa_epic(nasa_token, path):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {
        'api_key': nasa_token
        }
    response = requests.get(url, params=params)
    response.raise_for_status()
    json_content = response.json()

    for number, content in enumerate(json_content, start=1):
        image = content['image']
        date = content['date'].split()[0]
        date = date.replace('-', '/')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png'
        image_name = f'nasa_epic{number}.png'
        file_path = path / image_name
        save_image(file_path, image_url, params=params)

if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    path = Path('images')
    Path(path).mkdir(parents=False, exist_ok=True)
    
    try:
        fetch_nasa_epic(nasa_token, path)
    except requests.exceptions.HTTPError as error:
        exit(f"Can't get data from server: {error}")
