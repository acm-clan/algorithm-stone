from manim_imports_ext import *

class TestScene(AlgoScene):
    def construct(self):
        avatar = AlgoAvatar(self)
        avatar.center().scale(0.5)
        self.add(avatar)
        self.wait(2)
