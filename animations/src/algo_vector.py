from manimlib import *
from .algo_vgroup import *
from .algo_node import *

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

    def add_arrow(self, index = 0, color=BLUE, text=""):
        arrow = Arrow(start=UP, end=DOWN).scale(0.2).set_color(color)
        if text != "":
            t = Text(text, color=color).next_to(arrow, direction=RIGHT, buff=0.05).scale(0.3)
            arrow.add(t)

        self.arrows.append(arrow)
        self.add(arrow)
        self.move_arrow(arrow, index, animate=False)
        return arrow

    def clear_arrows(self):
        for k in self.arrows:
            self.remove(k)

    def move_arrow(self, arrow, index, run_time=1, animate=True):
        if index < 0:
            obj = self.submobjects[0]
            w = obj.get_bounding_box_point(RIGHT) - obj.get_bounding_box_point(LEFT)
            p = obj.get_bounding_box_point(UP) - w + UP*0.3
            if animate:
                self.scene.play(ApplyMethod(arrow.move_to, p, run_time=run_time))
            else:
                arrow.move_to(p)
        else:
            p = self.submobjects[index].get_bounding_box_point(UP) + UP*0.3
            if animate:
                self.scene.play(ApplyMethod(arrow.move_to, p, run_time=run_time))
            else:
                arrow.move_to(p)

    def size(self):
        return len(self.datas)

    def get(self, index):
        return self.datas[index]

    def get_node(self, index):
        return self.submobjects[index]

    def set(self, index, data):
        self.datas[index] = data
        new_node = AlgoNode(str(data))
        old_node = self.submobjects[index]
        p = old_node.get_center()
        # self.replace_submobject(index, new_node)
        new_node.shift(p)
        old_node.text_obj.become(new_node.text_obj)

    def swap(self, i, j):
        if i == j:
            return
        # data
        self.datas[i], self.datas[j] = self.datas[j], self.datas[i]
        # obj
        self.scene.play(Swap(self[i], self[j]))
        self.scene.add_sound("swap", gain=0)
        self.submobjects[i], self.submobjects[j] = self.submobjects[j], self.submobjects[i]