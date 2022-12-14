from abc import ABC, abstractmethod


class DownloaderInterface(ABC):

    @staticmethod
    @abstractmethod
    def download(link):
        """Attempts to download a video"""
        pass
