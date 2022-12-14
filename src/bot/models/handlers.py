from src.downloader.utils.AudioDownloader import AudioDownloader
from src.downloader.utils.VideoDownloader import VideoDownloader
from src.bot.components.messages.messages import Messages
from src.bot.components.commands.commands import Commands
from src.bot.components.keyboards.buttons.buttons import Buttons
from src.parser.parser import YouTubeParser
from src.bot.components.keyboards.keyboard import KeyBoard


class MessageHandler:
    def __init__(self, bot):
        self.__bot = bot
        youtube_parser = YouTubeParser()

        @self.__bot.message_handler(commands=[Commands.START_COMMAND])
        def start(message):
            self.__bot.send_message(message.chat.id, Messages.WELCOME_MESSAGE)

        @self.__bot.message_handler(commands=[Commands.GET_VIDEOS_COMMAND])
        def ask_for_title(message):
            title_message = self.__bot.send_message(message.chat.id, Messages.ENTER_THE_TITLE_MESSAGE)
            self.__bot.register_next_step_handler(title_message, ask_for_number)

        @self.__bot.message_handler(commands=[Commands.INSTALL_COMMAND])
        def install(message):
            user_markup = KeyBoard.generate_keyboard()

            choice_message = self.__bot.send_message(message.chat.id, Messages.CHOICE_MESSAGE,
                                                     reply_markup=user_markup)
            self.__bot.register_next_step_handler(choice_message, choose_format)

        @self.__bot.message_handler(commands=[Commands.HELP_COMMAND])
        def get_help(message):
            self.__bot.send_message(message.chat.id, Messages.HELP_MESSAGE)

        @self.__bot.message_handler(commands=[Commands.FORMATS_INFO_COMMAND])
        def get_formats(message):
            self.__bot.send_message(message.chat.id, Messages.FORMATS_MESSAGE)

        def ask_for_number(message):
            youtube_parser.set_title(message.text)

            number_message = self.__bot.send_message(message.chat.id, Messages.GIVE_NUMBER_OF_VIDEOS_MESSAGE)
            self.__bot.register_next_step_handler(number_message, get_videos)

        def get_videos(number_message):
            try:
                number_of_the_videos = int(number_message.text)
                parse_result_dict = youtube_parser.parse(number_of_the_videos)

                for obj in parse_result_dict:
                    self.__bot.send_message(number_message.chat.id, f"https://www.youtube.com{obj['url_suffix']}")
            except ValueError:
                self.__bot.send_message(number_message.chat.id, Messages.WRONG_TYPE_OF_NUMBER_MESSAGE)

        def choose_format(message):
            if message.text == Buttons.MP3:
                link = self.__bot.send_message(message.chat.id, Messages.GIVE_THE_LINK_MESSAGE)
                self.__bot.register_next_step_handler(link, get_audio)
            elif message.text == Buttons.MP4:
                link = self.__bot.send_message(message.chat.id, Messages.GIVE_THE_LINK_MESSAGE)
                self.__bot.register_next_step_handler(link, get_video)
            else:
                self.__bot.send_message(message.chat.id, Messages.WRONG_FORMAT_ERROR_MESSAGE)

        def get_audio(link_message):
            self.__bot.send_message(link_message.chat.id, "Downloading...")

            try:
                file_info_list = AudioDownloader.download(link_message.text)
                self.__bot.send_audio(link_message.chat.id, audio=open(file_info_list[0], 'rb'),
                                      duration=file_info_list[1])

            except ValueError:
                self.__bot.send_message(link_message.chat.id, Messages.WRONG_URL_ERROR_MESSAGE)

        def get_video(link_message):

            try:
                file_info_list = VideoDownloader.download(link_message.text)

                self.__bot.send_video(link_message.chat.id, video=open(file_info_list[0], 'rb'),
                                      duration=file_info_list[1])

            except ValueError:
                self.__bot.send_message(link_message.chat.id, Messages.WRONG_URL_ERROR_MESSAGE)
