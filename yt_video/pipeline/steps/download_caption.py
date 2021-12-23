import time

from pytube import YouTube
from yt_video.pipeline.steps.step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        NumExistingCaptions = 1
        NumNoCaptionVideo = 0
        start = time.time()
        for yt in data:
            print('downloading for ', yt.id)
            if utils.caption_file_exists(yt):
                print('found existing caption NO', NumExistingCaptions, yt.url)
                NumExistingCaptions += 1
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())

            except (KeyError, AttributeError) as e:
                print('Found an Error: ', e, 'while downloading the caption for', yt.url)
                NumNoCaptionVideo += 1
                continue

            # print(en_caption_convert_to_srt)
            # save the caption to a file named Output.txt

            text_file = open(utils.get_caption_filepath(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 'seconds')
        print('Total: ', NumNoCaptionVideo, 'no caption')

        return data
