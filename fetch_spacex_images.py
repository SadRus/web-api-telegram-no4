import argparse
import requests

from funcs import save_image
from pathlib import Path


def fetch_spacex_by_launch_id(path, launch_id='latest'):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    response_json = response.json()
    images_url = response_json['links']['flickr']['original']
    for number, image_url in enumerate(images_url, start=1):
        image_name = f'spacex{number}.jpg'
        file_path = path / image_name
        save_image(file_path, image_url)

if __name__ == '__main__':
    path = Path('images')
    Path(path).mkdir(parents=False, exist_ok=True)
    
    parser = argparse.ArgumentParser(
        description='Download SpaceX launch image by id or latest'
        )
    parser.add_argument('--launch_id', default='latest')
    args = parser.parse_args()
    
    try:
        fetch_spacex_by_launch_id(path, args.launch_id)
    except requests.exceptions.HTTPError as error:
        exit(f"Can't get data from server: {error}")
