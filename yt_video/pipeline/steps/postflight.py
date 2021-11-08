from yt_video.pipeline.steps.step import Step
from yt_video.pipeline.steps.step import StepException


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('In Postflight')
