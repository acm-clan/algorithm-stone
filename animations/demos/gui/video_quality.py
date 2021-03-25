from enum import Enum


# Value tied to index in radio_buttons
class VideoQuality(Enum):

    def __new__(cls, *args, **kwargs):
        del args    # unused
        del kwargs  # unused

        value = len(cls.__members__)
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, index):
        self.index = index

    low = 0
    med = 1
    high = 2

    @staticmethod
    def retrieve_by_index(index):
        for quality in VideoQuality:
            if quality.index == index:
                return quality
        return None
