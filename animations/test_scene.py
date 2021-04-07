from manim_imports_ext import *

class TestScene(AlgoScene):
    def construct(self):
        avatar = AlgoAvatar(self)
        avatar.center().scale(0.5)
        self.add(avatar)
        self.wait(2)

class TestTexScene(AlgoScene):
    def construct(self):
        avatar = AlgoAvatar(self)
        avatar.center().scale(0.5)
        self.add(avatar)
        self.wait(2)

    def show_diff(self):
        kw = {
            "tex_to_color_map": {
                "x_0": BLUE_D,
                "y_0": BLUE_B,
                "{t}": GREY_B,
                "O(2)": BLUE_D
            }
        }

        s = VGroup(
            TexText("1 前缀和：数组不变，区间求和 $O(1)$", **kw),
            Tex("\\text {1 前缀和：数组不变，区间求和} O(2)", **kw),
            TexText("2 树状数组：用于区间求和，单点修改 $O(logn)$", **kw),
            TexText("3 线段树：用于区间求和，区间最大值，区间修改，单点修改 $O(logn)$", **kw),
            Tex("x({t}) = \\cos(t) x_0 - \\sin(t) y_0", **kw),
        )

        s.arrange(DOWN, buff=LARGE_BUFF)

        s = AlgoTable(self, [
            ["", "区间求和", "区间最大值", "区间修改", "单点修改"],
            [],
        ])

        self.add(s)