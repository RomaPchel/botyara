from abc import ABC, abstractmethod


class ParserInterface(ABC):

    @staticmethod
    @abstractmethod
    def download(link):
        """Attempts to download a video"""
        pass
