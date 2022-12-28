import youtube_dl as yt
from src.downloader.models.Downloader import DownloaderInterface


class AudioDownloader(DownloaderInterface):

    @staticmethod
    def download(link):

        try:
            with yt.YoutubeDL({}) as ydl:
                dict_meta = ydl.extract_info(link, download=False)
        except yt.utils.DownloadError:
            raise ValueError

        filename = f"{dict_meta['title']}.mp3"
        duration = dict_meta['duration']

        ydl_opts = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename
        }

        try:
            with yt.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except:
            raise ValueError

        return filename, duration
