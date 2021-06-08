from manimlib import *
import networkx as nx

from algo_tree import AlgoTreeNode
from .algo_vgroup import *
from .algo_node import *
from .algo_tree import *
import numpy

class AlgoTrieTreeNode(AlgoTreeNode):
    def __init__(self):
        self.end = False
        self.c = numpy.empty(26, dtype=object)

class AlgoTrieTree(AlgoTree):
    def __init__(self, scene, data=[], **kwargs):
        self.scene = scene
        super().__init__(**kwargs)
        # empty
        self.root = AlgoTrieTreeNode()

    def add_word(self, word):
        self.scene.show_message("插入单词%s"%(word))
        p = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if p.c[index] == None:
                p.c[index] = AlgoTrieTreeNode()
                self.update_tree()
            p = p.c[index]
            self.update_tree()
        p.end = True
        self.update_tree()

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

    def update_tree(self):
        # 数据层
        nodes, edges = self.calc_tree_data(self.root)
        # layout
        pos_infos = self.calc_networkx(nodes, edges)
        # 
        self.move_nodes(pos_infos, nodes, edges)
        # 构造树

    def query(self, word):
        p = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not p.c[index]:
                return False
            p = p.c[index]
        return p.end
            