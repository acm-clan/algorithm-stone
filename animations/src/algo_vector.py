from manimlib import *
from algo_node import *

class AlgoVector(VGroup):
    def __init__(self, datas, **kwargs):
        self.datas = datas
        super().__init__(**kwargs)
        for k in datas:
            self.add(AlgoNode(str(k)))
        self.arrange()


