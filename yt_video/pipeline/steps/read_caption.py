import os
from pprint import pprint
from yt_video.pipeline.steps.step import Step
from yt_video.settings import CAPTIONS_DIR

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}  # data為字典 key為檔名.txt value為字幕
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                time_line = False  # 用來判斷該行是否為時間
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:  # 等同 == True
                        caption = line
                        captions[caption] = time  # 將字幕寫入字典
                        time_line = False
            data[caption_file] = captions
        pprint(data)
        return data



