from manimlib import *
from .algo_vgroup import *
from .algo_node import *

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


class AlgoPropertyPanel(AlgoVGroup):
    def __init__(self, text_list, **kwargs):
        super().__init__(**kwargs)

        arr = [AlgoText(x, color=DARK_BROWN) for x in text_list]

        text_group = VGroup()
        text_group.add(*arr)
        text_group.arrange(direction=DOWN, aligned_edge=LEFT, buff=SMALL_BUFF)
        self.add(text_group)
        self.text_group = text_group

        rect = SurroundingRectangle(text_group)
        self.rect = rect
        self.add(rect)

    def light(self, index, color=BLACK):
        self.text_group.submobjects[index].set_color(color)

class AlgoStdioFilter():
    def __init__(self, c, cb):
        self.cb = cb
        self.c = c
        import io

        real_stdout = sys.stdout
        fake_stdout = io.StringIO()
        sys.stdout = fake_stdout
        self.c()
        output_string = fake_stdout.getvalue()
        fake_stdout.close()
        sys.stdout = real_stdout
        self.cb(output_string)