# -*- encoding: utf-8 -*-
from manim_imports_ext import *

# 307.区域检索-数组可修改

class SegmentTree(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datas = np.array([1, 2, 3, 4, 5, 6])
        self.group = []
        for i in range(self.datas.shape[0]):
            self.group.append(i)

    def show_diff(self):
        self.show_message("首先，让我们来看看区间问题的常见3个解法")
        
        table = AlgoTable(self, np.array([
            ["",       "区间求和",  "区间最大值",  "区间修改",    "单点修改"],
            ["前缀和", AlgoCheckmark(), AlgoExmark(), AlgoExmark(), AlgoExmark(),],
            ["树状数组", AlgoCheckmark(), AlgoCheckmark(), AlgoExmark(), AlgoCheckmark(),],
            ["线段树", AlgoCheckmark(), AlgoCheckmark(), AlgoCheckmark(), AlgoCheckmark(),],
        ], dtype=object))

        self.play(ShowCreation(table), run_time=4)
        
        rect = SurroundingRectangle(table)
        self.play(ShowCreation(rect))

        self.show_message("前缀和、树状数组、线段树")

        self.show_message("前缀和一般用于固定的数组")
        
        self.show_message("树状数组是一种很高效的数据结构")
        self.show_message("功能能满足大部分需求")

        self.show_message("线段树则是一种非常灵活的数据结构")
        self.show_message("本动画重点讲解线段树")
        self.play(FadeOut(table), FadeOut(rect))

    def what_is_segment_tree(self):
        self.show_message("线段树是一棵树")

        self.show_message("从数组进行构造")

        array = AlgoVector(self, self.datas)
        self.play(ShowCreation(array))
        self.play(array.to_edge, LEFT)

        # 
        tree = AlgoGraph(self)
        self.play(ShowCreation(tree))
        self.play(tree.to_edge, RIGHT)

    def show_problem(self):
        pass

    def construct(self):
        # self.add_sound("bg2")
        # self.start_logo()
        self.init_message("线段树")
        # self.show_sticky_label("LeetCode 307.区域检索-数组可修改")
        self.show_diff()
        # 
        self.what_is_segment_tree()
        # 
        self.show_problem()
        # 
        self.wait(11)
