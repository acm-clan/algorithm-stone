from manim_imports_ext import *

class TestScene(AlgoScene):
    def construct(self):
        graph = AlgoGraph(self, [1,2,3,4], [(1,2), (2,3), (1, 4)])
        self.add(graph)
        self.wait(2)
