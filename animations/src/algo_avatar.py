from manimlib import *
import networkx as nx
from .algo_vgroup import *
from .algo_node import *

class AlgoAvatar(AlgoVGroup):
    def __init__(self, scene, **kwargs):
        self.scene = scene
        super().__init__(**kwargs)

        left = Line([-2, 0, 0], [0, 4, 0])
        self.add(left)

        right = Line([2, 0, 0], [0, 4, 0])
        self.add(right)

        cu = CubicBezier([-1,2,0], [-3.32,2.62,0], [3.32,2.62,0],[1,2,0])
        self.add(cu)

        eyel = Circle(fill_color=RED, fill_opacity=1).move_to([-0.5, 3.25, 0]).scale(0.2)
        self.add(eyel)

        eyer = Circle(fill_color=RED, fill_opacity=1).move_to([0.5, 3.25, 0]).scale(0.2)
        self.add(eyer)

        glow = Circle(fill_color=RED, fill_opacity=1).move_to([0, 4, 0]).scale(0.2)
        self.add(glow)

    def talk(self):
        print("talk")
    