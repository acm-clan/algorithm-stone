from manimlib import *
from .algo_config import *

class AlgoNode(VGroup):
    def __init__(self, text, is_circle=False, **kwargs):
        super().__init__(**kwargs)
        color = "#464445"
        self.text_obj = Text(text, color=color, font="Consolas").scale(0.6)
        self.text_sub_obj = Text("", color=color, font="Consolas").scale(0.6)

        if is_circle:
            self.outline_obj = Circle(color=color).scale(0.3)
        else:
            self.outline_obj = Square(color=color).scale(0.3)

        self.text_sub_obj.shift(DR/4).set_color(RED)
        self.add(self.text_obj, self.outline_obj, self.text_sub_obj)

    def set_text(self, text):
        color = "#464445"
        c = self.text_obj.get_center()
        self.remove(self.text_obj)
        self.text_obj = Text(text, font="Consolas").scale(0.6).set_color(color)
        self.text_obj.shift(c)
        self.add(self.text_obj)

    def get_text(self):
        return self.text_obj.text

    def set_sub(self, sub_val):
        self.remove(self.text_sub_obj)
        self.text_sub_obj = Text(sub_val, font="Consolas").scale(0.6)
        self.add(self.text_sub_obj)
        self.text_sub_obj.move_to(self.text_obj)
        self.text_sub_obj.shift(DR/4).set_color(RED)
