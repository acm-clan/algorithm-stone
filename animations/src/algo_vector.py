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
    
    def print(self):
        print(" ".join(str(i) for i in self.datas))

    def set_sub(self, index, sub_value):
        node = self.submobjects[index]
        node.set_sub(sub_value)

    def add_arrow(self, index = 0):
        arrow = Arrow(start=UP, end=DOWN).scale(0.2).set_color(BLUE)
        self.arrows.append(arrow)
        self.add(arrow)
        self.move_arrow(arrow, index)
        return arrow

    def clear_arrows(self):
        for k in self.arrows:
            self.remove(k)

    def move_arrow(self, arrow, index):
        p = self.submobjects[index].get_bounding_box_point(UP)
        self.scene.play(ApplyMethod(arrow.move_to, p))

    def size(self):
        return len(self.datas)

    def get(self, index):
        return self.datas[index]

    def set(self, index, data):
        self.datas[index] = data
        self.replace_submobject(index, AlgoNode(str(data)))
        self.arrange()

    def swap(self, i, j):
        if i == j:
            return
        # data
        self.datas[i], self.datas[j] = self.datas[j], self.datas[i]
        # obj
        self.scene.play(Swap(self[i], self[j]))
        self.scene.add_sound("swap", gain=0)
        self.submobjects[i], self.submobjects[j] = self.submobjects[j], self.submobjects[i]