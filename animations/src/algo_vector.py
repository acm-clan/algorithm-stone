from manimlib import *
from algo_node import *

class AlgoVector(VGroup):
    def __init__(self, datas=[], **kwargs):
        self.datas = datas
        super().__init__(**kwargs)
        for k in datas:
            self.add(AlgoNode(str(k)))
        self.arrange()

    def size(self):
        return len(self.datas)

    def get_node_data(self, index):
        return self.datas[index]

    def set_node_data(self, index, data):
        self.datas[index] = data
        self.replace_submobject(index, AlgoNode(str(data)))

