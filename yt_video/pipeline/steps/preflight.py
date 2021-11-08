from yt_video.pipeline.steps.step import Step
from yt_video.pipeline.steps.step import StepException


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('In Preflight')
        utils.create_dirs()