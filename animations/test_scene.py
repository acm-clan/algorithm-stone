from manim_imports_ext import *

class TestScene(AlgoScene):
    def construct(self):
        avatar = AlgoAvatar(self)
        avatar.center()
        self.add(avatar)
        self.wait(2)
