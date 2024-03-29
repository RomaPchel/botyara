import youtube_dl as yt

from src.downloader.models.Downloader import DownloaderInterface


class VideoDownloader(DownloaderInterface):

    @staticmethod
    def download(link):

        try:
            with yt.YoutubeDL({}) as ydl:
                dict_meta = ydl.extract_info(link, download=False)
        except yt.utils.DownloadError:
            return "Invalid URL!", None

        filename = f"{dict_meta['title']}.mp4"
        duration = dict_meta['duration']

        ydl_opts = {
            'format': 'mp4',
            'outtmpl': filename
        }

        try:
            with yt.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except:
            raise ValueError

        return filename, duration
