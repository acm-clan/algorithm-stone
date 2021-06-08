from manimlib import *
import networkx as nx
from .algo_vgroup import *
from .algo_node import *
import numpy

class AlgoTreeNode(object):
    def __init__(self, id):
        self.id = id

class AlgoTree(AlgoVGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tree_node_id = 0
        self.node_objs = {}
        self.edge_objs = {}

    def gen_id(self):
        self.tree_node_id = self.tree_node_id + 1
        return self.tree_node_id
    
    def check_node(self, p):
        if p.id not in self.node_objs:
            self.add_node(p)

    def check_edge(self, x, y):
        if (x.id, y.id) not in self.edge_objs:
            self.add_edge(x, y)

    def add_edge(self, n, t):
        if not n or not t:
            return
        a = Arrow(ORIGIN, ORIGIN, thickness=0.03, buff=1.25)
        a.set_color(GREY)
        self.add(a)
        self.edge_objs[(n.id, t.id)] = a

    def calc_tree_data(self):
        q = []
        q.append(self.root)
        nodes = []
        edges = []

        while len(q)>0:
            p = q.pop(0)
            nodes.append(AlgoTreeNode(p.id))

            if p.left:
                self.check_node(p.left)
                self.check_edge(p, p.left)
                edges.append((p.id, p.left.id))
                q.append(p.left)
            if p.right:
                self.check_node(p.right)
                self.check_edge(p, p.right)
                edges.append((p.id, p.right.id))
                q.append(p.right)

        return nodes, edges

    def add_node(self, z):
        if z.id in self.node_objs:
            return
        n = AlgoNode(str(z.k))

        n.set_color(RED)
        self.node_objs[z.id] = n
        self.add(n)
        n.next_to(self)

    def calc_networkx(self, nodes, edges):
        self.g = nx.Graph()
        for k in nodes:
            self.g.add_node(k.id)
        for k in edges:
            self.g.add_edge(*k)
        layout = nx.nx_agraph.graphviz_layout(self.g, prog='dot', args='-Grankdir="TB"')
        points = layout
        x = [points[k][0] for k in points]
        y = [points[k][1] for k in points]
        c = (sum(x) / len(points), sum(y) / len(points))
        for k in layout:
            layout[k] = np.array(layout[k])-np.array(c)

        return layout