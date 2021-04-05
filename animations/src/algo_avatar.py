from manimlib import *
import networkx as nx
from .algo_vgroup import *
from .algo_node import *

class AlgoAvatar(AlgoVGroup):
    def __init__(self, scene, **kwargs):
        self.scene = scene
        super().__init__(**kwargs)

        bgs = VGroup()
        bgs.add(RoundedRectangle(width=4, stroke_width=0, corner_radius=0.2, stroke_color="#333", 
            height=2.8, fill_color="#000", fill_opacity=1).scale(1.05))
        bgs.add(RoundedRectangle(width=4, stroke_width=0, corner_radius=0.2, stroke_color="#333", 
            height=2.8, fill_color="#ff443f", fill_opacity=1))
        
        bgs.add(RoundedRectangle(width=2.6, stroke_width=0, corner_radius=0.2, stroke_color="#333", 
            height=2.0, fill_color="#333", fill_opacity=1).scale(1.1).shift(LEFT*0.4))
        bgs.add(RoundedRectangle(width=2.6, stroke_width=0, corner_radius=0.2, stroke_color="#333", 
            height=2.0, fill_color="#00dceb", fill_opacity=1).shift(LEFT*0.4))
        self.add(bgs)

        buttons = VGroup()
        buttons.add(Line(LEFT, RIGHT, color="#fff").scale(0.05).shift(RIGHT*1.4+UP*1.2))
        buttons.add(Dot(fill_color="#333").scale(1).shift(RIGHT*1.7+UP*1.2))
        c = Circle(fill_color="#767676", stroke_color="#333", fill_opacity=1)
        c.add(Line(color="#333").rotate(180).scale(0.3))
        c.scale(0.2).shift(RIGHT*1.5+UP*0.8)
        buttons.add(c)
        c = Circle(fill_color="#767676", stroke_color="#333", fill_opacity=1)
        c.add(Line(color="#333").rotate(190).scale(0.3))
        c.scale(0.2).shift(RIGHT*1.5+UP*0.25)
        buttons.add(c)
        buttons.add(Line(LEFT, RIGHT, color="#333").scale(0.15).shift(RIGHT*1.5+DOWN*0.1))
        buttons.add(Line(LEFT, RIGHT, color="#333").scale(0.15).shift(RIGHT*1.5+DOWN*0.25))
        buttons.add(Line(LEFT, RIGHT, color="#333").scale(0.15).shift(RIGHT*1.5+DOWN*0.4))
        self.add(buttons.shift(DOWN*0.3))

        top = VGroup()
        top.add(Line(ORIGIN, UP, color="#eca240").rotate_about_origin(45)).scale(1)
        top.add(Line(ORIGIN, UP, color="#eca240").rotate_about_origin(-45)).scale(1)
        self.add(top)
        top.next_to(bgs, direction=UP, buff=0)

    def talk(self):
        print("talk")
    