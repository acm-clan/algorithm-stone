from manimlib import *
from . import *

class AlgoCheckmark(TexText):
    CONFIG = {
        "color": GREEN
    }

    def __init__(self, **kwargs):
        super().__init__("\\ding{51}")


class AlgoExmark(TexText):
    CONFIG = {
        "color": RED
    }

    def __init__(self, **kwargs):
        super().__init__("\\ding{55}")

class AlgoText(Text):
    CONFIG = {
        "color": BLACK,
    }

    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)
        self.scale(0.3)
