from src.bot.models.handlers import MessageHandler

import telebot


class Bot:
    def __init__(self, token):
        self.__bot = telebot.TeleBot(token)
        self.__message_handler = MessageHandler(self.__bot)

    def run(self):
        self.__bot.polling(none_stop=True)
