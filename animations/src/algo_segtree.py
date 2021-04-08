from manimlib import *
import networkx as nx
from .algo_vgroup import *
from .algo_node import *

class AlgoSegTreeNode(object):
    def __init__(self, id, l, r, v, left=None, right=None):
        self.l = l
        self.r = r
        self.v = v
        self.id = id
        self.left = left
        self.right = right

class AlgoSegTree(AlgoVGroup):
    def __init__(self, scene, datas = [], **kwargs):
        self.datas = datas
        self.arrows = {}
        self.node_objs = {}
        self.scene = scene
        
        self.edges = []
        self.nodes = []
        
        super().__init__(**kwargs)

        self.root = self.build(datas, 0, len(datas)-1)
        
        self.init_networkx(self.nodes, self.edges)

        for k in self.nodes:
            n = AlgoNode(str(k["data"]))
            p = self.get_node_pos(k["id"])
            n.shift(p)
            self.node_objs[k["id"]] = n
            self.add(n)

        for k in self.edges:
            self.add_edge_internal(k[0], k[1])

        self.center()

    def hide_all(self):
        for k in self.node_objs:
            self.remove(self.node_objs[k])

        for k in self.arrows:
            self.remove(self.arrows[k])

    def show_node(self, id):
        n = self.get_node(id)
        self.scene.play(FadeIn(n))

    def show_edge(self, i, j):
        a = self.arrows[(i, j)]
        self.scene.play(FadeIn(a))

    def build(self, datas, l, r):
        if l == r:
            id = len(self.nodes)
            self.nodes.append({"id":id, "data":datas[l]})
            return AlgoSegTreeNode(id, l, r, datas[l])
        m = math.floor((l+r)/2)
        left = self.build(datas, l, m)
        right = self.build(datas, m+1, r)

        val = left.v+right.v
        id = len(self.nodes)
        self.edges.append([id, left.id])
        self.edges.append([id, right.id])
        self.nodes.append({"id":id, "data":val})
        return AlgoSegTreeNode(id, l, r, val, left, right)

    def init_networkx(self, nodes, edges):
        self.g = nx.Graph()
        for k in reversed(nodes):
            self.g.add_node(k["id"])
        for k in reversed(edges):
            self.g.add_edge(*k)
        self.pos_infos = nx.nx_agraph.graphviz_layout(self.g, prog='dot', args='-Grankdir="TB"')
        
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
