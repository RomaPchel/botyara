import creator
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/Users/markzavgorodniy/PycharmProjects/bot/botyara/.env')
load_dotenv(dotenv_path=dotenv_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if __name__ == '__main__':
    bot = creator.BotCreator.create(BOT_TOKEN)
    bot.run()
