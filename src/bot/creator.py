from src.bot.bot import Bot
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot_handler = Bot("5864587562:AAEcIRUlerYT9x5RpA1Xy5vQl7GJvtQU2Ss")
