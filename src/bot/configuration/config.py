import dotenv
import telebot
import os

dotenv.load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
