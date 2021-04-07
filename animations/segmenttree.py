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
        kw = {
            "tex_to_color_map": {
                
            }
        }

        s = VGroup(
            Tex("前缀和：数组不变，区间求和", **kw),
            Tex("树状数组：用于区间求和，单点修改", **kw),
            Tex("线段树：用于区间求和，区间最大值，区间修改，单点修改等", **kw),
        )

        s.arrange(DOWN, buff=LARGE_BUFF)
        self.add(s)

    def construct(self):
        # self.add_sound("bg2")
        # self.start_logo()
        # self.init_message("线段树")
        # self.show_sticky_label("LeetCode 307.区域检索-数组可修改")
        self.show_diff()

        self.wait()
