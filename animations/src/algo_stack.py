from manimlib import *
from . import *

class AlgoStack(VGroup):
    def __init__(self, scene, datas, **kwargs):
        self.scene = scene
        self.datas = datas
        super().__init__(**kwargs)
        # add base line
        line = Line(start=UP, end=DOWN).scale(0.5).set_color(BLUE)
        self.add(line)
        self.base_line = line
        # add node
        self.nodes = []
        for k in datas:
            n = AlgoNode(str(k))
            self.add(n)
            self.nodes.append(n)
        self.arrange()

    def push(self, data):
        n = AlgoNode(str(data))
        self.add(n)
        self.datas.append(data)
        self.nodes.append(n)
        self.arrange()
        print("stack push size:", len(self.datas))

    def pop(self):
        p = self.nodes[-1]
        self.remove(p)
        self.scene.play(FadeOut(p.copy()))
        del self.datas[-1]
        del self.nodes[-1]
        self.arrange()
        print("stack pop size:", len(self.datas))

    def empty(self):
        return len(self.datas) == 0

    def top(self):
        if self.empty():
            print("error call top data")
            return None
        return self.nodes[len(self.nodes)-1]

    def top_data(self):
        if self.empty():
            print("error call top data")
            return None
        return self.datas[len(self.datas)-1]
