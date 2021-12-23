from .step import Step
from pytube import YouTube
from yt_video.settings import VIDEOS_DIR

class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])  # 將found變成集合 去除同一影片若有多次關鍵字會重複下載的情況
        print('Numbers of download：', len(yt_set))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                print(f'{url} file is existing, skipping')
                continue
            print('Downloading for ', url)
            #  YouTube(url).streams.filter(progressive=True, subtype='mp4').get_by_resolution('480p').download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')  # first() 為預設解析度
            YouTube(url).streams.get_highest_resolution().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')  #

        return data


