from manimlib import *
import networkx as nx
from .algo_vgroup import *
from .algo_node import *
import numpy

class AlgoTrieTreeNode(object):
    def __init__(self):
        self.end = False
        self.c = numpy.empty(26, dtype=object)

class AlgoTrieTree(AlgoVGroup):
    def __init__(self, scene, data=[], **kwargs):
        self.scene = scene
        super().__init__(**kwargs)
        # empty
        self.root = AlgoTrieTreeNode()

    def add_word(self, word):
        p = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if p.c[index] == None:
                p.c[index] = AlgoTrieTreeNode()
            p = p.c[index]
        p.end = True

    def find_word_internal(self, p, word):
        pass

    def query(self, word):
        p = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not p.c[index]:
                return False
            p = p.c[index]
        return p.end
            