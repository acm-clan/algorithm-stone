from manimlib import *



class AlgoScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DefaultFontName = "Microsoft YaHei"
        self.DefaultFontSize = 24

    def init_message(self, msg):
        self.message = Text(msg, font_size=self.DefaultFontSize, font=self.DefaultFontName).shift(DOWN*1.5)
        self.play(Write(self.message))

    def show_message(self, msg):
        m = Text(msg, font_size=self.DefaultFontSize, font=self.DefaultFontName).shift(DOWN*1.5)
        self.play(Transform(self.message, m))