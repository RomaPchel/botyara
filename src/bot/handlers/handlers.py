from src.DB.utils.Engine import DAO
from src.bot.components.commands.commands import Commands
from src.bot.components.keyboards.buttons.buttons import Buttons
from src.bot.components.keyboards.keyboard import KeyBoard
from src.bot.components.messages.messages import Messages
from src.bot.creator import bot_handler
from src.downloader.utils.AudioDownloader import AudioDownloader
from src.downloader.utils.VideoDownloader import VideoDownloader
from src.parser.parser import YouTubeParser
from sqlalchemy import exc

bot = bot_handler.bot

youtube_parser = YouTubeParser()


@bot.message_handler(commands=[Commands.START_COMMAND])
def start(message):
    bot.send_message(message.chat.id, Messages.WELCOME_MESSAGE)


@bot.message_handler(commands=[Commands.GET_VIDEOS_COMMAND])
def ask_for_title(message):
    title_message = bot.send_message(message.chat.id, Messages.ENTER_THE_TITLE_MESSAGE)
    bot.register_next_step_handler(title_message, ask_for_number)


@bot.message_handler(commands=[Commands.INSTALL_COMMAND])
def install(message):
    user_markup = KeyBoard.generate_keyboard()

    choice_message = bot.send_message(message.chat.id, Messages.CHOICE_MESSAGE,
                                      reply_markup=user_markup)
    bot.register_next_step_handler(choice_message, choose_format)


@bot.message_handler(commands=[Commands.HELP_COMMAND])
def get_help(message):
    bot.send_message(message.chat.id, Messages.HELP_MESSAGE)


@bot.message_handler(commands=[Commands.FORMATS_INFO_COMMAND])
def get_formats(message):
    bot.send_message(message.chat.id, Messages.FORMATS_MESSAGE)


@bot.message_handler(commands=[Commands.CREATE_PLAYLIST])
def ask_for_name_of_playlist(message):
    name_of_playlist = bot.send_message(message.chat.id, Messages.NAME_OF_PLAYLIST_MESSAGE)
    bot.register_next_step_handler(name_of_playlist, create_playlist)


@bot.message_handler(commands=[Commands.ADD_MEDIA])
def choose_playlist(message):
    name_of_playlist = bot.send_message(message.chat.id, Messages.NAME_OF_PLAYLIST_MESSAGE)
    bot.register_next_step_handler(name_of_playlist, ask_link_to_current_playlist)


@bot.message_handler(commands=[Commands.GET_PLAYLISTS])
def get_playlists(message):
    list_of_playlists = DAO.get_playlists(message.chat.id)
    for playlist in list_of_playlists:
        bot.send_message(message.chat.id, playlist.name)


@bot.message_handler(commands=[Commands.GET_MEDIAS])
def choose_playlist_to_show_media(message):
    playlist_name = bot.send_message(message.chat.id, Messages.NAME_OF_PLAYLIST_MESSAGE)
    bot.register_next_step_handler(playlist_name, get_medias_of_current_playlist)


def ask_for_number(message):
    youtube_parser.set_title(message.text)

    number_message = bot.send_message(message.chat.id, Messages.GIVE_NUMBER_OF_VIDEOS_MESSAGE)
    bot.register_next_step_handler(number_message, get_videos)


def get_videos(number_message):
    try:
        number_of_the_videos = int(number_message.text)
        parse_result_dict = youtube_parser.parse(number_of_the_videos)

        for obj in parse_result_dict:
            bot.send_message(number_message.chat.id, f"https://www.youtube.com{obj['url_suffix']}")
    except ValueError:
        bot.send_message(number_message.chat.id, Messages.WRONG_TYPE_OF_NUMBER_MESSAGE)


def choose_format(message):
    if message.text == Buttons.MP3:
        link = bot.send_message(message.chat.id, Messages.GIVE_THE_LINK_MESSAGE)
        bot.register_next_step_handler(link, get_audio)
    elif message.text == Buttons.MP4:
        link = bot.send_message(message.chat.id, Messages.GIVE_THE_LINK_MESSAGE)
        bot.register_next_step_handler(link, get_video)
    else:
        bot.send_message(message.chat.id, Messages.WRONG_FORMAT_ERROR_MESSAGE)


def get_audio(link_message):
    bot.send_message(link_message.chat.id, Messages.DOWNLOADING_MESSAGE)

    try:
        file_info_list = AudioDownloader.download(link_message.text)
        bot.send_audio(link_message.chat.id, audio=open(file_info_list[0], 'rb'),
                       duration=file_info_list[1])

    except ValueError:
        bot.send_message(link_message.chat.id, Messages.WRONG_URL_ERROR_MESSAGE)


def get_video(link_message):
    bot.send_message(link_message.chat.id, Messages.DOWNLOADING_MESSAGE)

    try:
        file_info_list = VideoDownloader.download(link_message.text)

        bot.send_video(link_message.chat.id, video=open(file_info_list[0], 'rb'),
                       duration=file_info_list[1])

    except ValueError:
        bot.send_message(link_message.chat.id, Messages.WRONG_URL_ERROR_MESSAGE)


def create_playlist(name_of_playlist_message):
    DAO.create_playlist(name_of_playlist_message.chat.id, name_of_playlist_message.text)


def ask_link_to_current_playlist(name_of_playlist_message):
    playlist_name = name_of_playlist_message.text
    user_id = name_of_playlist_message.chat.id

    try:
        playlist_id = DAO.get_playlist_by_name_and_chatid(playlist_name, user_id)

        link_to_add = bot.send_message(name_of_playlist_message.chat.id, Messages.LINK_OF_THE_VIDEO)

        bot.register_next_step_handler(link_to_add, add_link_to_current_playlist, playlist_id)
    except exc.SQLAlchemyError:
        bot.send_message(user_id, Messages.PLAYLIST_ERROR)


def add_link_to_current_playlist(link_message, playlist_id):
    DAO.add_media(playlist_id.id, link_message.text)


def get_medias_of_current_playlist(name_of_playlist):
    try:
        playlist_id = DAO.get_playlist_by_name_and_chatid(name_of_playlist.text, name_of_playlist.chat.id)
        media_list = DAO.get_medias_from_playlist(playlist_id.id)

        for media in media_list:
            bot.send_message(name_of_playlist.chat.id, media.link)
    except exc.SQLAlchemyError:
        bot.send_message(name_of_playlist.chat.id, Messages.PLAYLIST_ERROR)
