from yt_video.pipeline.steps.get_video_list import GetVideoList
from yt_video.pipeline.steps.step import StepException
from yt_video.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCd4JzeAkgTsyJDEkWC11PoA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList(),  # 將要處理的步驟功能儲存成清單，再利用for loop呼叫
    ]
    p = Pipeline(steps)
    p.operate(inputs)


if __name__ == '__main__':
    main()
