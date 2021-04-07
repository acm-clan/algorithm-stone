from manimlib import *
import random
from datetime import datetime
from .algo_config import *
from .algo_logo import *

class AlgoScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        random.seed(datetime.now())

    def show_sticky_label(text):
        leet = Text(text, color=GOLD_E).center().scale(0.2).to_edge(UP).shift(UP*0.2)
        self.play(ShowCreation(leet))

    def start_logo(self):
        text = VGroup(
            Text("ACM", font=AlgoFontName, color="#1fa0cf").scale(0.5),
            Text("算法日常", font=AlgoFontName, color="#93582e").scale(0.5)
        ).arrange(buff=0.1)

        self.play(Write(text))
        logo = AlgoLogo().scale(0.15).next_to(text, direction=LEFT)
        self.play(ShowCreation(logo))

        group = VGroup(logo, text)
        self.play(group.arrange, run_time=1)
        self.wait()

        self.play(group.scale, 0.3, run_time=1.5, rate_func=smooth)
        self.wait(0.3)
        self.play(group.to_edge, DL, run_time=1, rate_func=smooth)

    def create_serif_font(self, msg, color=WHITE):
        return Text(msg, font=AlgoSerifFontName, color=color)

    def init_message(self, msg):
        self.subtitle_message = Text(msg, font=AlgoFontName, stroke_width=0, stroke_opacity=0.5, stroke_color=None).scale(0.4).to_edge(DOWN).shift(UP)
        self.play(Write(self.subtitle_message))
        return self.subtitle_message

    def show_message(self, msg, delay=3):
        self.remove(self.subtitle_message)
        m = Text(msg, font=AlgoFontName, stroke_width=0, stroke_opacity=0.5, stroke_color=None).scale(0.4).to_edge(DOWN).shift(UP)
        self.subtitle_message = m
        self.play(ShowIncreasingSubsets(m), run_time=len(msg)*0.2)
        self.wait(delay)

    def rand_color(self):
        r = lambda: random.randint(100, 255)+100
        return '#%02X%02X%02X' % (r(),r(),r())

    def finish(self):
        self.wait(10)