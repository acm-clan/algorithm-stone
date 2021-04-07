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
