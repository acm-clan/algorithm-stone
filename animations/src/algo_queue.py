from manimlib import *
from .algo_node import *
from .algo_vgroup import *

class AlgoQueue(AlgoVGroup):
    def __init__(self, datas=[], **kwargs):
        self.datas = datas
        super().__init__(**kwargs)
        for k in datas:
            self.add(AlgoNode(str(k)))
        self.arrange()

    def size(self):
        return len(self.datas)

    def push(self, data):
        self.add(AlgoNode(str(data)))
        self.datas.append(data)
        self.arrange()

    def pop(self):
        self.remove(self.submobjects[0])
        del self.datas[0]
        self.arrange()

    def empty(self):
        return len(self.datas) == 0

        

