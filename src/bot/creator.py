from bot import Bot
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/Users/markzavgorodniy/PycharmProjects/bot/.env')
load_dotenv(dotenv_path=dotenv_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot_handler = Bot(BOT_TOKEN)
