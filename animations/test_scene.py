from manim_imports_ext import *

class TestScene(AlgoScene):
    def construct(self):
        self.camera.background_rgba = [1, 1, 1, 0.5]
        self.start_logo()
        self.wait(2)
