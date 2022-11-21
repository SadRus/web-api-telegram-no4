import os
import random
import time

import telegram

from dotenv import load_dotenv
from pathlib import Path

if __name__ == '__main__':
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
    chat_id = os.environ['TG_CHAT_ID']
    delay = int(os.environ['SEND_PHOTO_DELAY'])

    while True:
        photos = []
        for (dirpath, dirnames, filenames) in os.walk('images'):
            photos.append(filenames)
        photo = random.choice(filenames)
        path = Path('images')
        file_path = Path(path / photo)

        with open(file_path, 'rb') as photo_file:
            bot.send_photo(chat_id=chat_id, photo=photo_file)
        time.sleep(delay)
