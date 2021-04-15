from manim_imports_ext import *

# 红黑树的噩梦，可以结束了

class RedBlackTreePreface(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        # self.start_logo(subtitle="红黑树")
        self.wait(100)

class RedBlackTreeWhatIs(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        self.wait()

class RedBlackTreeRotate(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        tree = AlgoRBTree(self)
        for i in range(40):
            tree.set(i, i)
        for i in range(40):
            tree.remove(i)
        self.wait()

