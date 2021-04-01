from manim_imports_ext import *


class TestScene(AlgoScene):
    def construct(self):
        c = AlgoLogo(fill_color=BLUE, fill_opacity = 1).scale(0.5)
        self.add(c)

        self.wait(2)
