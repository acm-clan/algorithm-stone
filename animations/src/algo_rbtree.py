from manimlib import *
import networkx as nx
from .algo_vgroup import *
from .algo_node import *
import queue

nil = None

class AlgoRBTreeNode(object):
    def __init__(self, id, k, v, color):
        self.id = id
        self.k = k
        self.v = v
        self.color = color
        self.p = nil
        self.left = nil
        self.right = nil
        # self.obj = AlgoNode(str(k))

    def addChild(self, t, z):
        y = self
        if y == nil:
            t.root = z
        elif z.k < y.k:
            y.left = z
        else:
            y.right = z
    
    def isLeft(self):
        return self == self.p.left

    def isRight(self):
        return self == self.p.right

    def brother(self):
        if self.isLeft():
            return self.p.right
        else:
            return self.p.left

    def replaceChild(self, u, v):
        if u == self.left:
            self.left = v
        else:
            self.right = v
        v.p = self

class AlgoRBTree(AlgoVGroup):
    def __init__(self, scene, **kwargs):
        self.edge_objs = {}
        self.node_objs = {}
        self.scene = scene
        
        self.edges = []
        self.nodes = []
        
        super().__init__(**kwargs)

        self.node_id = 0
        global nil
        nil = AlgoRBTreeNode(self.get_node_id(), 0, 0, BLACK)
        self.root = nil

        # add nil to the scene
        
        # self.add(self.root.obj)

        self.center()

    def insert(self, z):
        y = nil
        x = self.root
        while x != nil:
            y = x
            if z.k < x.k:
                x = x.left
            else:
                x = x.right
        z.p = y
        y.addChild(self, z)
        self.insertFixup(z)
    
    def insertFixup(self, z:AlgoRBTreeNode):
        while z.p.color == RED:
            if z.p.isLeft():
                y = z.p.brother()
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z.isRight():
                        z = z.p
                        self.leftRotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.rightRotate(z.p.p)
            else:
                y = z.p.brother()
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z.isLeft():
                        z = z.p
                        self.rightRotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.leftRotate(z.p.p)
        self.root.color = BLACK

    def dumpInternal(self, n, d):
        if (not n):
            return
        for _ in range(d):
            print("--", end='')
        print("%d(%d %d)"%(n.k, n.k, n.v))
        self.dumpInternal(n.left, d + 1)
        self.dumpInternal(n.right, d + 1)

    def dump(self, n):
        self.dumpInternal(n, 1)

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != nil:
            y.left.p = x
        y.p = x.p
        self.transplant(x, y)
        y.left = x
        x.p = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != nil:
            y.right.p = x
        y.p = x.p
        self.transplant(x, y)
        y.right = x
        x.p = y

    def transplant(self, u, v):
        if u.p == nil:
            self.root = v
            self.root.p = nil
        else:
            u.p.replaceChild(u, v)

    def set(self, k, v):
        print("set ", k, v)
        if self.root == nil:
            self.root = AlgoRBTreeNode(self.get_node_id(), k, v, BLACK)
        else:
            z = AlgoRBTreeNode(self.get_node_id(), k, v, RED)
            self.insert(z)
        # self.dump(self.root)

    def getInternal(self, n, k):
        if not n or n == nil:
            return None
        if n.k == k:
            return n
        if k < n.k:
            return self.getInternal(n.left, k)
        return self.getInternal(n.right, k)

    def treeMinimum(self, x):
        p = x
        while p.left != nil:
            p = p.left
        return p

    def deleteInternal(self, z):
        y = z
        origin_color = y.color
        x = None

        if (z.left == nil):
            x = z.right
            self.transplant(z, z.right)
        elif (z.right == nil):
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.treeMinimum(z.right)
            origin_color = y.color
            x = y.right
            if (y.p == z):
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if (origin_color == BLACK):
            self.deleteFixUp(x)

    def deleteFixUp(self, x):
        while (x != self.root and x.color == BLACK):
            if (x.isLeft()):
                w = x.brother()
                if (w.color == RED):
                    w.color = BLACK
                    x.p.color = RED
                    self.leftRotate(x.p)
                    w = x.p.right
                if (w.left.color == BLACK and w.right.color == BLACK):
                    w.color = RED
                    x = x.p
                else:
                    if (w.right.color == BLACK):
                        w.left.color = BLACK
                        w.color = RED
                        self.rightRotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.right.color = BLACK
                    self.leftRotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if (w.color == RED):
                    w.color = BLACK
                    x.p.color = RED
                    self.rightRotate(x.p)
                    w = x.p.left
                if (w.right.color == BLACK and w.left.color == BLACK):
                    w.color = RED
                    x = x.p
                else:
                    if (w.left.color == BLACK):
                        w.right.color = BLACK
                        w.color = RED
                        self.leftRotate(w)
                        w = x.p.left

                    w.color = x.p.color
                    x.p.color = BLACK
                    w.left.color = BLACK
                    self.rightRotate(x.p)
                    x = self.root
        x.color = BLACK

    def remove(self, k):
        print("remove ", k)
        z = self.getInternal(self.root, k)
        if z:
            self.deleteInternal(z)

    def get_node_id(self):
        self.node_id += 1
        return self.node_id

    def travel_to_nodes(self, root):
        q = []
        q.append(root)

        while len(q)>0:
            p = q.pop(0)
            self.nodes.append({"id":p.id, "data": p.v})

            if p.left:
                self.edges.append([p.id, p.left.id])
                q.append(p.left)
            if p.right:
                self.edges.append([p.id, p.right.id])
                q.append(p.right)

    def hide_all(self):
        for k in self.node_objs:
            self.remove(self.node_objs[k])

        for k in self.edge_objs:
            self.remove(self.edge_objs[k])

    def show_node(self, id):
        n = self.get_node(id)
        self.scene.play(FadeIn(n))

    def show_edge(self, i, j):
        a = self.edge_objs[(i, j)]
        self.scene.play(FadeIn(a))

    def init_networkx(self, nodes, edges):
        self.g = nx.Graph()
        for k in nodes:
            self.g.add_node(k["id"])
        for k in edges:
            self.g.add_edge(*k)
        self.pos_infos = nx.nx_agraph.graphviz_layout(self.g, prog='dot', args='-Grankdir="TB"')
        
    def get_node_pos(self, k):
        p = self.pos_infos[k]
        ratio = 60
        return [p[0]/ratio, p[1]/ratio, 0]
