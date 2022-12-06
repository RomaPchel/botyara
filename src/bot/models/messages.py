class MessageSender:

    def send_welcome_message(self, name, get_videos_command, install_command, help_command):
        return f"Hello! This is {name}. " \
               f"you can use /{get_videos_command} to enter the title of video u want to download;" \
               f"/{install_command} to search video u mentioned and " \
               f"/{help_command} to find out which formats are available"

    def send_response_to_get_videos_command(self):
        return "Enter the title of video you want to find"

    def send_response_to_search_command(self):
        return "Enter the link of the video"

    def send_response_to_invalid_message(self, message):
        return f"Invalid message {message}"

    def send_help_message(self, name, start_command):
        return f"{name} will help you to download videos in 2 formats: MP3 and MP4. Also you can find top 5 videos " \
               f"for the title you " \
               f"send. To start the bot enter /{start_command} command."

    def send_choice_message(self):
        return "Choose format, please"
