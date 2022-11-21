import os
import requests

from urllib.parse import urlparse


def save_image(path, image_url, headers={}, params={}):
    response = requests.get(image_url, headers=headers, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def get_extension(url):
    address = urlparse(url).path
    return os.path.splitext(address)[1]
