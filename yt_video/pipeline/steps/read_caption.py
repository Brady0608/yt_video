from yt_video.pipeline.steps.step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue

            captions = {}
            with open(yt.get_caption_filepath, 'r') as f:
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
            yt.captions = captions

        return data



