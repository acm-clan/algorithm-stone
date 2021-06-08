from manimlib import *
from time import gmtime, strftime
from datetime import datetime
import random
from .algo_config import *
from .algo_logo import *

class AlgoScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        random.seed(datetime.now())
        # self.camera.background_rgba = [1, 1, 1, 0.5]
        # self.camera.background_rgba = [0, 0, 0, 0]
        # remove
        from pathlib import Path
        for p in Path(".").glob("algo*.png"):
            p.unlink()

    def show_sticky_label(text):
        leet = Text(text, color=GOLD_E).center().scale(0.2).to_edge(UP).shift(UP*0.2)
        self.play(ShowCreation(leet))

    def start_logo(self, animate=True, stay=False, subtitle="", tex=False, tex_map={}):
        v = self.create_six_background(color_start="#363636", color_end="#363636")
        self.add(v)
        
        text = VGroup(
            Text("ACM", font=AlgoFontName, color="#1fa0cf").scale(1),
            Text("算法日常", font=AlgoFontName, color="#93582e").scale(1)
        ).arrange(buff=0.1)

        self.add(text)

        if animate:
            self.play(Write(text))

        logo = AlgoLogo().scale(0.15).next_to(text, direction=LEFT)
        self.add(logo)

        sub = None
        if subtitle != "" and animate:
            if tex:
                sub = TexText(subtitle, color=WHITE, tex_to_color_map=tex_map).scale(1.2)
            else:
                sub = Text(subtitle, font=AlgoFontName, color=WHITE).scale(1)

            sub.next_to(text, direction=DOWN)
            self.play(ShowCreation(sub))

        # if animate:
            # self.play(ShowCreation(logo))

        group = VGroup(logo, text)

        if animate:
            self.play(group.arrange, run_time=1)
            self.wait()
        else:
            group.arrange()

        if not stay:
            if animate:
                self.play(group.scale, 0.3, run_time=1.5, rate_func=smooth)
                self.wait(0.3)
                self.play(group.to_edge, DL, run_time=1, rate_func=smooth)
            else:
                group.scale(0.3)
                group.to_edge(DL)
        if sub:
            self.play(ApplyMethod(sub.shift, UP*1.5), run_time=1)
            self.wait()
            self.play(FadeOut(sub))

        group.fix_in_frame()
        return group

    def create_serif_font(self, msg, color=WHITE):
        return Text(msg, font=AlgoSerifFontName, color=color)

    def init_message(self, msg, delay=3, tex=False, tex_map={}):
        if tex:
            m = TexText(msg, color=WHITE, tex_to_color_map=tex_map).scale(0.8).to_edge(DOWN).shift(UP*0.5)
        else:
            m = Text(msg, font=AlgoFontName, stroke_width=0, stroke_opacity=0.5, 
                stroke_color=None).scale(0.6).to_edge(DOWN).shift(UP*0.5).set_color(WHITE)
            
        self.play(Write(m), run_time=len(msg)*0.2)
        self.subtitle_message = m
        self.subtitle_message.fix_in_frame()
        self.wait(delay)
        return self.subtitle_message

    def init_messaged(self, msg, delay=0):
        return self.init_message(msg, delay=delay)

    def show_message(self, msg, delay=3, animate=True, tex=False, tex_map={}):
        if not animate:
            return
        self.remove(self.subtitle_message)
        
        if tex:
            m = TexText(msg, color=WHITE, tex_to_color_map=tex_map).scale(0.8).to_edge(DOWN).shift(UP*0.5)
        else:
            m = Text(msg, font=AlgoFontName, stroke_width=0, stroke_opacity=0.5, 
                stroke_color=None).scale(0.6).to_edge(DOWN).shift(UP*0.5).set_color(WHITE)

        m.fix_in_frame()
        self.subtitle_message = m
        self.play(Write(m), run_time=len(msg)*0.2)
        self.wait(delay)

    def show_messaged(self, msg, delay=0):
        self.show_message(msg, delay)

    def rand_color(self):
        r = lambda: random.randint(100, 255)+100
        return '#%02X%02X%02X' % (r(),r(),r())

    def finish(self):
        self.wait(10)

    def create_six_background(self, color_start="#f6f6f6", color_end="#fcfcfc"):
        v = VGroup()

        for i in range(0, 11):
            last = None
            for j in range(0, 21):
                r = 0
                if i % 2 == 1:
                    r = RIGHT*(0.5*math.sqrt(3.0))
                op = abs(4-i)
                colors = list(Color(color_start).range_to(Color(color_end), 7))
                p = Polygon(*self.polygon(6), color=colors[op]).shift(i*DOWN*1.5+r)
                if last != None:
                    p.next_to(last, RIGHT, buff=0)
                v.add(p)
                last = p

        v.center().scale(0.5)
        v.fix_in_frame()
        return v

    def polygon(self, sides, radius=1, rotation=0, translation=None):
        one_segment = math.pi * 2 / sides

        points = [
            [math.sin(one_segment * i + rotation) * radius,
            math.cos(one_segment * i + rotation) * radius, 0]
            for i in range(sides)]

        if translation:
            points = [[sum(pair) for pair in zip(point, translation)]
                    for point in points]

        return points

    def finish_scene(self, msg):
        self.show_messaged(msg)
        # add image
        code = ImageMobject("assets/code3.png").scale(0.3)
        self.play(ShowCreation(code))

    def snapshot(self):
        self.update_frame()
        image = self.get_image()
        v = random.random()
        path = "algo_image_%s_%d.png"%(datetime.now().strftime('%Y%m%d%H%M%S'), int(v*1000000))
        image.save(path)
        print("snapshot:", path)