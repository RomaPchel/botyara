class MessageSender:

    def __init__(self, name, commands_dict):
        self.__name = name
        self.__start_command = commands_dict["start_command"]
        self.__get_videos_command = commands_dict["get_videos_command"]
        self.__install_command = commands_dict["install_command"]
        self.__help_command = commands_dict["help_command"]

    def send_welcome_message(self):
        return f"Hello! This is {self.__name}. " \
               f"you can use /{self.__get_videos_command} to enter the title of video u want to download;" \
               f"/{self.__install_command} to search video u mentioned and " \
               f"/{self.__help_command} to find out which formats are available"

    def send_response_to_get_videos_command(self):
        return "Enter the title of video you want to find"

    def send_response_to_search_command(self):
        return "Enter the link of the video"

    def send_response_to_invalid_message(self, message):
        return f"Invalid message {message}"

    def send_help_message(self):
        return f"{self.__name} will help you to download videos in 2 formats: MP3 and MP4. Also you can find top 5 videos " \
               f"for the title you " \
               f"send. To start the bot enter /{self.__start_command} command."

    def send_choice_message(self):
        return "Choose format, please"
