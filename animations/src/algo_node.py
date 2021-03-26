from manimlib import *

class AlgoNode(VGroup):
    def __init__(self, text, **kwargs):
        self.text = Text(text, font_size=20)
        self.rect = Square().scale(0.3)
        super().__init__(**kwargs)
        self.add(self.text, self.rect)
        
