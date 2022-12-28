from abc import ABC, abstractmethod
import youtube_dl as yt


class DownloaderInterface(ABC):

    @staticmethod
    def check_for_duration(link):
        try:
            with yt.YoutubeDL({}) as ydl:
                dict_meta = ydl.extract_info(link, download=False)
        except yt.utils.DownloadError:
            raise ValueError

        duration = dict_meta['duration']
        print(duration / 60)
        if duration / 60 > 6:
            return False
        return True

    @staticmethod
    @abstractmethod
    def download(link):
        """Attempts to download a video"""
        pass
