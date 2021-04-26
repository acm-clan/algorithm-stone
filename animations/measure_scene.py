import sys
from manim_imports_ext import *

class MeasureScene(AlgoScene):
    def construct(self):
        shape = self.camera.frame.get_shape()

        
        horizon = Line(start=LEFT*shape[0]/2, end=RIGHT*shape[0]/2, color=RED)
        verticle = Line(start=UP*shape[1]/2, end=DOWN*shape[1]/2, color=BLUE)
        self.play(ShowCreation(horizon), ShowCreation(verticle))

        # t = AlgoText("1 width %.2f height %.2f delta 0.00"%(shape[0], shape[1]), color=GREEN).shift(LEFT*3)
        # self.add(t)
        # t.next_to(horizon, direction=UP, buff=0)
        # self.play(ShowCreation(t))

        count = 2
        delta = 0.0
        # lastcentery = t.get_center()[1]
        # print("center:", t.get_center())

        v = VGroup()
        for i in range(12):
            nt = Text("%d width %.2f height %.2f delta %.2f"%(count, shape[0], shape[1], delta), 
                color=GREEN).shift(LEFT*3)
            v.add(nt)
        v.arrange(direction=UP, aligned_edge=LEFT, buff=0.0)
        self.add(v)
            # self.add(nt)
            # nt.next_to(t, direction=UP, buff=0)
            # self.play(ShowCreation(nt))

            # p = nt.get_center()
            # print("center:", p)
            # delta = p[1] - lastcentery
            # t = nt
            # lastcentery = p[1]
            # count += 1

        self.camera.frame.shift(OUT*10)
        
        self.snapshot()
        self.wait()
