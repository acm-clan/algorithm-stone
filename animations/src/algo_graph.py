from manimlib import *
import networkx as nx
from .algo_vgroup import *
from .algo_node import *

class AlgoGraph(AlgoVGroup):
    def __init__(self, scene, nodes=[], edges=[], **kwargs):
        self.nodes = nodes
        self.arrows = {}
        self.node_objs = {}
        self.scene = scene
        super().__init__(**kwargs)
        
        self.init_networkx(nodes, edges)

        for k in nodes:
            n = AlgoNode(str(k))
            p = self.get_node_pos(k)
            n.shift(p)
            self.node_objs[k] = n
            self.add(n)

        for k in edges:
            self.add_edge_internal(k[0], k[1])

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

    def add_edge_internal(self, i, j):
        if i == j:
            a = Arrow(self.get_node_pos(i), self.get_node_pos(j)+RIGHT*0.1, path_arc=np.pi*1.5, thickness=0.03).scale(0.5)
            self.arrows[(i, j)] = a
            self.add(a)
        else:
            a = Arrow(self.get_node_pos(i), self.get_node_pos(j), thickness=0.03)
            self.add(a)
            self.arrows[(i, j)] = a

    def add_edge(self, i, j):
        ni = self.node_objs[i]
        nj = self.node_objs[j]
        if i == j:
            a = Arrow(ni.get_center(), nj.get_center()+RIGHT*0.1, path_arc=np.pi*1.5, thickness=0.03).scale(0.5)
            self.arrows[(i, j)] = a
            self.add(a)
            self.scene.play(FadeIn(a), run_time=0.3)
        else:
            a = Arrow(ni.get_center(), nj.get_center(), thickness=0.03)
            self.add(a)
            self.arrows[(i, j)] = a
            self.scene.play(FadeIn(a), run_time=0.3)

    def remove_edge(self, i, j):
        a = self.arrows[(i, j)]
        self.remove(a)
        self.scene.play(FadeOut(a))
        del  self.arrows[(i, j)]

    def get_node(self, i):
        return self.node_objs[i]
