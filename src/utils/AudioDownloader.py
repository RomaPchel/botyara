import youtube_dl as yt
from src.models.Downloader import ParserInterface

class AudioDownloader(ParserInterface):
    @staticmethod
    def download_audio(link, chat_id, msg_id):

        try:
            with yt.YoutubeDL({}) as ydl:
                dict_meta = ydl.extract_info(link, download=False)
        except yt.utils.DownloadError:
            return "Invalid URL!", None

        filename = f"{dict_meta['title']}.mp3"
        ydl_opts = {
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename
        }

        try:
            with yt.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except:
            raise ValueError

        if 'watch?v=' in link:
            downloaded_file_name = link.split('watch?v=')[-1]
        else:
            downloaded_file_name = link.split('/')[-1]
        return 'ok', downloaded_file_name


