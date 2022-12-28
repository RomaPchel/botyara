#from asd.bot.handlers.handlers import MessageHandler

import telebot


class Bot:
    def __init__(self, token):
        self.__bot = telebot.TeleBot(token)

    @property
    def bot(self):
        return self.__bot

    def run(self):
        self.__bot.polling(none_stop=True)
