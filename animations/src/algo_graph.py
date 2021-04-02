from manimlib import *
import networkx as nx
from .algo_vgroup import *
from .algo_node import *

class AlgoGraph(AlgoVGroup):
    def __init__(self, scene, nodes=[], edges=[], **kwargs):
        self.nodes = nodes
        self.arrows = []
        self.scene = scene
        super().__init__(**kwargs)
        
        self.init_networkx(nodes, edges)

        for k in nodes:
            n = AlgoNode(str(k))
            p = self.get_node_pos(k)
            n.shift(p)
            self.add(n)

        for k in edges:
            self.add(Arrow(self.get_node_pos(k[0]), self.get_node_pos(k[1])))

        self.center()

    def init_networkx(self, nodes, edges):
        self.g = nx.Graph()
        for k in nodes:
            self.g.add_node(k)
        for k in edges:
            self.g.add_edge(*k)
        self.pos_infos = nx.nx_agraph.graphviz_layout(self.g, prog='dot')
        
    def get_node_pos(self, k):
        p = self.pos_infos[k]
        ratio = 60
        return [p[0]/ratio, p[1]/ratio, 0]


        