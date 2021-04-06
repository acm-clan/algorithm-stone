from manim_imports_ext import *

# 547 省份数量

class UnionFind(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = np.array([1, 2, 3, 4])
        self.group = []
        for i in range(self.data.shape[0]):
            self.group.append(i)

    def construct(self):
        self.add_sound("bg2")
        self.start_logo()
        m = self.init_message("线段树")

        leet = Text("LeetCode 547.省份数量", color=GOLD_E).center().scale(0.2).to_edge(UP).shift(UP*0.2)
        self.play(ShowCreation(leet))
        
        self.wait()
