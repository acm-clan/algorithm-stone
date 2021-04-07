# -*- encoding: utf-8 -*-
from manim_imports_ext import *

# 307.区域检索-数组可修改

class SegmentTree(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.group = []
        for i in range(self.data.shape[0]):
            self.group.append(i)

    def show_diff(self):
        s = AlgoTable(self, np.array([
            ["",       "区间求和",  "区间最大值",  "区间修改",    "单点修改"],
            ["前缀和", AlgoCheckmark(), AlgoExmark(), AlgoExmark(), AlgoExmark(),],
            ["树状数组", AlgoCheckmark(), AlgoCheckmark(), AlgoExmark(), AlgoCheckmark(),],
            ["线段树", AlgoCheckmark(), AlgoCheckmark(), AlgoCheckmark(), AlgoCheckmark(),],
        ], dtype=object))

        self.add(s)

    def construct(self):
        # self.add_sound("bg2")
        # self.start_logo()
        # self.init_message("线段树")
        # self.show_sticky_label("LeetCode 307.区域检索-数组可修改")
        self.show_diff()

        self.wait(11)
