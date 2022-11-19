import os

import telegram

from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TG_BOT_TOKEN'])
    # bot.send_message(text='hi', chat_id=440084749)
    bot.send_photo(chat_id=-809390367, photo=open('images/nasa_apod1.jpg', 'rb'))