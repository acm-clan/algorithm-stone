from manimlib import *

class AlgoNode(VGroup):
    def __init__(self, text, **kwargs):
        self.text_obj = Text(text, font_size=20)
        self.rect_obj = Square().scale(0.3)
        super().__init__(**kwargs)
        self.add(self.text_obj, self.rect_obj)

    def set_text(self, text):
        self.remove(self.text_obj)
        self.text_obj = Text(text, font_size=20)
        self.add(self.text_obj)

    def get_text(self):
        return self.text_obj.text

        
        
