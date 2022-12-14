#from src.bot.handlers.handlers import MessageHandler

import telebot


class Bot:
    def __init__(self, token):
        self.__bot = telebot.TeleBot(token)
        #self.__message_handler = MessageHandler(self.__bot)

    @property
    def bot(self):
        return self.__bot

    def run(self):
        self.__bot.polling(none_stop=True)
