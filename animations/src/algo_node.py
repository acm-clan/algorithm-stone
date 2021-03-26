from manimlib import *


class AlgoNode(VGroup):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text_obj = Text(text, font_size=20)
        self.text_sub_obj = Text("", font_size=12)
        self.rect_obj = Square().scale(0.3)
        self.text_sub_obj.shift(DR/4).set_color(RED)
        self.add(self.text_obj, self.rect_obj, self.text_sub_obj)

    def set_text(self, text):
        self.remove(self.text_obj)
        self.text_obj = Text(text, font_size=20)
        self.add(self.text_obj)

    def get_text(self):
        return self.text_obj.text

    def set_sub(self, sub_val):
        self.remove(self.text_sub_obj)
        self.text_sub_obj = Text(sub_val, font_size=12)
        self.add(self.text_sub_obj)
        self.text_sub_obj.move_to(self.text_obj)
        self.text_sub_obj.shift(DR/4).set_color(RED)
