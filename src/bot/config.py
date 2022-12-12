import models.messages as sender
import models.handlers as handler
import telebot


class Bot:
    def __init__(self, name, token):
        self.__name = name
        self.__bot = telebot.TeleBot(token)
        commands_dict = {
            "start_command": "start",
            "get_videos_command": "get_videos",
            "install_command": "install",
            "help_command": "help"
        }
        self.__message_sender = sender.MessageSender(self.__name, commands_dict)
        self.__message_handler = handler.MessageHandler(self.__name, self.__bot, self.__message_sender, commands_dict)

    def run(self):
        self.__bot.polling(none_stop=True)
