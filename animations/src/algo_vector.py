from manimlib import *
from algo_node import *
from algo_vgroup import *


class AlgoVector(AlgoVGroup):
    def __init__(self, scene, datas=[], **kwargs):
        self.datas = datas
        self.arrows = []
        self.scene = scene
        super().__init__(**kwargs)
        for k in datas:
            self.add(AlgoNode(str(k)))
        self.arrange()

    def set_sub(self, index, sub_value):
        node = self.submobjects[index]
        node.set_sub(sub_value)

    def add_arrow(self):
        arrow = Arrow(start=UP, end=DOWN).scale(0.2).set_color(BLUE)
        self.arrows.append(arrow)
        self.add(arrow)
        return arrow

    def clear_arrows(self):
        for k in self.arrows:
            self.remove(k)

    def move_arrow(self, arrow, index):
        p = self.submobjects[index].get_bounding_box_point(UP)
        self.scene.play(ApplyMethod(arrow.move_to, p))

    def size(self):
        return len(self.datas)

    def get_node_data(self, index):
        return self.datas[index]

    def set_node_data(self, index, data):
        self.datas[index] = data
        self.replace_submobject(index, AlgoNode(str(data)))
        self.arrange()
