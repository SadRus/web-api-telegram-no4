import os
import random
import time

import telegram

from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
    delay = int(os.environ['SEND_PHOTO_DELAY'])

    while True:
        photos = []
        for (dirpath, dirnames, filenames) in os.walk('images/'):
            photos.append(filenames)
        photo = random.choice(filenames)

        bot.send_photo(chat_id=-809390367, photo=open(f'images/{photo}', 'rb'))
        time.sleep(delay)
