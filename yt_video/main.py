from yt_video.pipeline.steps.get_video_list import GetVideoList
from yt_video.pipeline.steps.initialize_yt import InitializeYT
from yt_video.pipeline.steps.download_caption import DownloadCaptions
from yt_video.pipeline.steps.step import StepException
from yt_video.pipeline.pipeline import Pipeline
from yt_video.utils import UTILS
from yt_video.pipeline.steps.preflight import Preflight
from yt_video.pipeline.steps.postflight import Postflight
from yt_video.pipeline.steps.read_caption import ReadCaption
from yt_video.pipeline.steps.search import Search
from yt_video.pipeline.steps.download_video import DownloadVideos


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
    }

    steps = [
        Preflight(),
        GetVideoList(),  # 將要處理的步驟功能儲存成清單，再利用for loop呼叫
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        Postflight(),
    ]
    utils = UTILS()
    p = Pipeline(steps)
    p.operate(inputs, utils)


if __name__ == '__main__':
    main()
