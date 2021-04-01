from manim_imports_ext import *


class TestScene(AlgoScene):
    def construct(self):
        self.wait(0.2)
        logo = AlgoLogo().scale(0.2)
        self.play(ShowCreation(logo))
        self.wait(2)
