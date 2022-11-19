import youtube_dl as yt

from src.models.Downloader import ParserInterface


class VideoDownloader(ParserInterface):

    @staticmethod
    def download_video(link, chat_id, msg_id):

        try:
            with yt.YoutubeDL({}) as ydl:
                dict_meta = ydl.extract_info(link, download=False)
        except yt.utils.DownloadError:
            return "Invalid URL!", None

        available_formats = [format for format in dict_meta['formats']]

        ydl_opts = {
            'format_id': available_formats[-1]['format_id'],
            'outtmpl': './%(id)s.%(ext)s'
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
