from yt_video.pipeline.steps.get_video_list import GetVideoList
from yt_video.pipeline.steps.download_caption import DownloadCaptions
from yt_video.pipeline.steps.step import StepException
from yt_video.pipeline.pipeline import Pipeline
from yt_video.utils import UTILS
from yt_video.pipeline.steps.preflight import Preflight
from yt_video.pipeline.steps.postflight import Postflight


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Preflight(),
        GetVideoList(),  # 將要處理的步驟功能儲存成清單，再利用for loop呼叫
        DownloadCaptions(),
        Postflight(),
    ]
    utils = UTILS()
    p = Pipeline(steps)
    p.operate(inputs, utils)


if __name__ == '__main__':
    main()
