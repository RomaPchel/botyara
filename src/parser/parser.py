from youtube_search import YoutubeSearch


class YouTubeParser:
    def __init__(self):
        self.__title_of_the_video = ""

    def set_title(self, title):
        self.__title_of_the_video = title

    def parse(self, number_of_videos):
        res = YoutubeSearch(self.__title_of_the_video, max_results=number_of_videos).to_dict()

        return res

