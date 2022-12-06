import models.messages as sender
import models.handlers as handler
import telebot


class Bot:
    def __init__(self, name, token):
        self.__name = name
        self.__bot = telebot.TeleBot(token)
        self.__message_sender = sender.MessageSender()
        self.__message_handler = handler.MessageHandler(self.__name, self.__bot, self.__message_sender, "start",
                                                        "get_videos",
                                                        "install", "help")

    def run(self):
        self.__bot.polling(none_stop=True)
