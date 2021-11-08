from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs, utils):  # 將未來可能在process傳入的參數儲存為inputs字典  data則是傳給下個步驟用的參數
        pass


class StepException(Exception):
    pass
