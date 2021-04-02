from manimlib import *
import networkx as nx
from .algo_vgroup import *
from .algo_node import *

class AlgoGraph(AlgoVGroup):
    def __init__(self, scene, nodes=[], edges=[], **kwargs):
        self.nodes = nodes
        self.arrows = {}
        self.scene = scene
        super().__init__(**kwargs)
        
        self.init_networkx(nodes, edges)

        for k in nodes:
            n = AlgoNode(str(k))
            p = self.get_node_pos(k)
            n.shift(p)
            self.add(n)

        for k in edges:
            if k[0] == k[1]:
                a = Arrow(self.get_node_pos(k[0]), self.get_node_pos(k[1])+RIGHT*0.1, path_arc=np.pi*1.5).scale(0.5)
                self.arrows[(k[0], k[1])] = a
                self.add(a)
            else:
                a = Arrow(self.get_node_pos(k[0]), self.get_node_pos(k[1]))
                self.add(a)
                self.arrows[(k[0], k[1])] = a

        self.center()

    def init_networkx(self, nodes, edges):
        self.g = nx.Graph()
        for k in nodes:
            self.g.add_node(k)
        for k in edges:
            self.g.add_edge(*k)
        self.pos_infos = nx.nx_agraph.graphviz_layout(self.g, prog='dot')
        # self.pos_infos = nx.random_layout(self.g, center=(0, 0), dim=2)
        
    def get_node_pos(self, k):
        p = self.pos_infos[k]
        ratio = 60
        return [p[0]/ratio, p[1]/ratio, 0]

    def clear_edges(self):
        self.g.clear_edges()

        for k in self.arrows:
            self.scene.play(FadeOut(k, run_time=0.3))
        self.arrows = []

    def add_edge(self, i, j):
        pass

    def remove_edge(self, i, j):
        pass

