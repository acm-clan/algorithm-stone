from manimlib import *
import random
from datetime import datetime

class AlgoScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DefaultFontName = "Microsoft YaHei"
        self.DefaultFontName = "Source Han Sans CN, Segoe UI"
        self.DefaultFontName = "Source Han Serif CN"
        self.DefaultSerifFontName = "Source Han Serif CN"
        self.DefaultSansSerifFontName = "Source Han Sans CN"
        self.DefaultMonoFontName = "Consolas"
        self.DefaultFontSize = 24
        random.seed(datetime.now())

    def create_serif_font(self, msg, color=WHITE, font_size=24):
        return Text(msg, font=self.DefaultSerifFontName,
            font_size=font_size, color=color)

    def init_message(self, msg):
        self.message = Text(msg, font_size=self.DefaultFontSize, font=self.DefaultFontName).to_edge(DOWN).shift(UP)
        self.play(Write(self.message))

    def show_message(self, msg):
        m = Text(msg, font_size=self.DefaultFontSize, font=self.DefaultFontName).to_edge(DOWN).shift(UP)
        self.play(Transform(self.message, m))

    def rand_color(self):
        r = lambda: random.randint(100, 255)+100
        return '#%02X%02X%02X' % (r(),r(),r())

    def finish(self):
        self.wait(10)