from manimlib import *
import random
from datetime import datetime

class AlgoScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DefaultFontName = "Microsoft YaHei"
        self.DefaultFontName = "Source Han Sans CN"
        self.DefaultSerifFontName = ""
        self.DefaultSansSerifFontName = ""
        self.DefaultMonoFontName = "Consolas"
        self.DefaultFontSize = 24
        random.seed(datetime.now())

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