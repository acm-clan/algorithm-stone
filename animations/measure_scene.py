import sys
from manim_imports_ext import *

class MeasureScene(AlgoScene):
    def construct(self):
        shape = self.camera.frame.get_shape()

        t = Text("1 width %.2f height %.2f delta 0.00"%(shape[0], shape[1]), color=GREEN, font_size=20).shift(LEFT*3).scale(1)
        self.add(t)
        horizon = Line(start=LEFT*shape[0]/2, end=RIGHT*shape[0]/2, color=RED)
        verticle = Line(start=UP*shape[1]/2, end=DOWN*shape[1]/2, color=BLUE)

        t.next_to(horizon, direction=UP, buff=0)

        count = 2
        delta = 0.0
        while True:
            nt = Text("%d width %.2f height %.2f delta %.2f"%(count, shape[0], shape[1], delta), 
                color=GREEN, font_size=20).shift(LEFT*3).scale(1)
            nt.next_to(t, direction=UP, buff=0)
            p = nt.get_center()
            delta = p[1] - t.get_center()[1]
            t = nt
            if p[1] > shape[1]/2:
                break
            count += 1
            self.add(nt)

        # self.camera.frame.shift(OUT*0.2)
        self.play(ShowCreation(horizon), ShowCreation(verticle))
        self.snapshot()
        self.wait()
