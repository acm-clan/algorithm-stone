from manimlib import *
import random
from datetime import datetime
from algo_config import *

class AlgoScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        random.seed(datetime.now())

    def create_serif_font(self, msg, color=WHITE):
        return Text(msg, font=Algo_Serif_FontName, color=color)

    def init_message(self, msg):
        self.message = Text(msg, font=Algo_FontName).scale(0.5).to_edge(DOWN).shift(UP)
        self.play(Write(self.message))

    def show_message(self, msg):
        m = Text(msg, font=Algo_FontName).scale(0.5).to_edge(DOWN).shift(UP)
        self.play(Transform(self.message, m))

    def rand_color(self):
        r = lambda: random.randint(100, 255)+100
        return '#%02X%02X%02X' % (r(),r(),r())

    def finish(self):
        self.wait(10)