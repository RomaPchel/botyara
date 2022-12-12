import telebot


class MessageHandler:
    def __init__(self, name, bot, message_sender, commands_dict):
        self.__name = name
        self.__bot = bot
        self.__message_sender = message_sender
        self.__start_command = commands_dict["start_command"]
        self.__get_videos_command = commands_dict["get_videos_command"]
        self.__install_command = commands_dict["install_command"]
        self.__help_command = commands_dict["help_command"]

        @self.__bot.message_handler(commands=[self.__start_command])
        def start(message):
            self.__bot.send_message(message.chat.id,
                                    self.__message_sender.send_welcome_message())

        @self.__bot.message_handler(commands=[self.__get_videos_command])
        def get_videos(message):
            msg = self.__bot.send_message(message.chat.id, self.__message_sender.send_response_to_get_videos_command())
            self.__bot.register_next_step_handler(msg, find_video)

        def find_video(message):
            if message.text[0] == '/':
                self.__bot.send_message(message.chat.id,
                                        self.__message_sender.send_response_to_invalid_message(message.text))
            else:
                self.__bot.send_message(message.chat.id, message.text)

        @self.__bot.message_handler(commands=[self.__install_command])
        def install(message):

            msg = self.__bot.send_message(message.chat.id, self.__message_sender.send_response_to_search_command())
            self.__bot.register_next_step_handler(msg, self.__get_markup)

        @self.__bot.message_handler(commands=[self.__help_command])
        def get_help(message):
            self.__bot.send_message(message.chat.id,
                                    self.__message_sender.send_help_message())

    def __get_markup(self, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        user_markup.row("MP3")
        user_markup.row("MP4")

        msg = self.__bot.send_message(message.chat.id, self.__message_sender.send_choice_message(),
                                      reply_markup=user_markup)
        self.__bot.register_next_step_handler(msg, self.__get_file)

    def __get_file(self, message):
        if message.text == "MP3":
            self.__bot.send_message(message.chat.id, "mp3 chosen")
        elif message.text == "MP4":
            self.__bot.send_message(message.chat.id, "mp4 chosen")
