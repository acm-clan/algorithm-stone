from manimlib import *

class MonotonicStack(Scene):
    def construct(self):
        # create list
        arr = [73, 74, 75, 71, 69, 72, 76, 73]
        group = VGroup()

        n = 1
        for v in arr:
            rect = Rectangle(width=1, height=1)
            group.add(rect)
            rect.shift(UP*n)
            n += 1

        self.play(
            ShowCreation(group)
        )

