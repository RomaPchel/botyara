from src.bot.components.commands.commands import Commands
from src.bot.components.keyboards.buttons.buttons import Buttons


class Messages:
    DURATION_ERROR = "Video is too long to download(>6min)"
    MEDIA_ADDITION_SUCCESS = "Link has been added to '%s'!"

    WELCOME_MESSAGE = f"Hello! This is Bot for getting and downloading content from Youtube. " \
                      f"you can use /{Commands.GET_VIDEOS_COMMAND} to enter the title of video u want to download;" \
                      f"/{Commands.INSTALL_COMMAND} to search video u mentioned and " \
                      f"/{Commands.FORMATS_INFO_COMMAND} to get info about formats of content "\
                      f"/{Commands.HELP_COMMAND} to find out which formats are available " \
                      f"/{Commands.CREATE_PLAYLIST} to create playlist " \
                      f"/{Commands.ADD_MEDIA} to add link for current playlist " \
                      f"/{Commands.GET_PLAYLISTS} to show playlists you have " \
                      f"/{Commands.GET_MEDIAS} to show links of current playlists " \
                      f"Lucky you!"

    ENTER_THE_TITLE_MESSAGE = "Enter the title of video you want to find"

    GIVE_THE_LINK_MESSAGE = "Give me the link, please: "

    WRONG_FORMAT_ERROR_MESSAGE = f"Invalid format, to get more info about formats call /{Commands.FORMATS_INFO_COMMAND} "

    WRONG_URL_ERROR_MESSAGE = "Invalid URL or can't find a content"

    WRONG_TYPE_OF_NUMBER_MESSAGE = "Number must be integer"

    HELP_MESSAGE = f"{Commands.HELP_COMMAND} will help you to download videos in 2 formats: MP3 and MP4." \
                   f" Also you can " \
                   f"find top 5 videos " \
                   f"for the title you " \
                   f"send. To start the bot enter /{Commands.START_COMMAND} command."

    CHOICE_MESSAGE = "Choose format, please: "

    FORMATS_MESSAGE = f"You can download content in {Buttons.MP3} or {Buttons.MP4}"

    GIVE_NUMBER_OF_VIDEOS_MESSAGE = "Enter the number of videos you want to get, please: "

    NAME_OF_PLAYLIST_MESSAGE = "Write name of playlist: "

    LINK_OF_THE_VIDEO = "Write link of the video you want to add: "

    PLAYLIST_CREATION_SUCCESS = "Playlist '%s' has been created!"

    PLAYLIST_ERROR = "No playlist was found"

    PLAYLIST_EMPTY_ERROR = "Playlist %s is empty"

    DOWNLOADING_MESSAGE = "Downloading..."
