from manim_imports_ext import *

class MeasureScene(AlgoScene):
    def construct(self):
        shape = self.camera.frame.get_shape()

        font_size = 30

        t = Text("1 width %.2f height %.2f delta 0.00"%(shape[0], shape[1]), color=GREEN, font_size=font_size).shift(LEFT*3)
        self.add(t)

        hw = shape[0]/2
        hh = shape[1]/2

        left = Line(start=LEFT*hw+UP*hh, end=LEFT*hw+DOWN*hh, color=BLUE)
        right = Line(start=RIGHT*hw+UP*hh, end=RIGHT*hw+DOWN*hh, color=BLUE_A)
        top = Line(start=LEFT*hw+UP*hh, end=RIGHT*hw+UP*hh, color=BLUE_B)
        bottom = Line(start=LEFT*hw+DOWN*hh, end=RIGHT*hw+DOWN*hh, color=BLUE_C)

        horizon = Line(start=LEFT*shape[0]/2, end=RIGHT*shape[0]/2, color=RED)
        verticle = Line(start=UP*shape[1]/2, end=DOWN*shape[1]/2, color=YELLOW)
        self.play(ShowCreation(horizon), ShowCreation(verticle), ShowCreation(left), 
            ShowCreation(right), ShowCreation(top), ShowCreation(bottom))

        t.next_to(horizon, direction=UP, buff=0)

        count = 2
        delta = 0.0
        lastcentery = t.get_center()[1]
        print("center:", t.get_center())
        while True:
            nt = Text("%d width %.2f height %.2f delta %.2f"%(count, shape[0], shape[1], delta), 
                color=GREEN, font_size=font_size).shift(LEFT*3)
            nt.next_to(t, direction=UP, buff=0)
            p = nt.get_center()
            print("center:", p)
            delta = p[1] - lastcentery
            t = nt
            lastcentery = p[1]
            if p[1] > shape[1]/2:
                break
            count += 1
            self.play(ShowCreation(nt))

        self.camera.frame.shift(OUT*10)
        self.snapshot()
        self.wait()


class MeasureScene2(AlgoScene):
    def construct(self):
        shape = self.camera.frame.get_shape()
        horizon = Line(start=LEFT*shape[0]/2, end=RIGHT*shape[0]/2, color=RED)
        verticle = Line(start=UP*shape[1]/2, end=DOWN*shape[1]/2, color=BLUE)
        self.play(ShowCreation(horizon), ShowCreation(verticle))

        delta = 0.0

        v = VGroup()
        for i in range(12):
            nt = Text("%d width %.2f height %.2f delta %.2f"%(i, shape[0], shape[1], delta), 
                color=GREEN).shift(LEFT*3)
            v.add(nt)
        v.arrange(direction=UP, aligned_edge=LEFT, buff=0.0)
        self.add(v)

        self.camera.frame.shift(OUT*10)
        
        self.snapshot()
        self.wait()