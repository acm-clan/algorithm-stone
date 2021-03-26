from manimlib import *
from algo_node import *

class AlgoStack(VGroup):
    def __init__(self, datas, **kwargs):
        self.datas = datas
        super().__init__(**kwargs)
        for k in datas:
            self.add(AlgoNode(str(k)))
        self.arrange()

    def push(self, data):
        self.add(AlgoNode(str(data)))
        self.datas.append(data)
        self.arrange()

    def pop(self):
        self.remove(self.submobjects[len(self.submobjects)-1])
        del self.datas[-1]
        self.arrange()

    def empty(self):
        return len(self.datas) == 0

    def top_data(self):
        if self.empty():
            print("error call top data")
            return None
        return self.datas[len(self.datas)-1]
