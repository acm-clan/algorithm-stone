from manimlib import *
from algomanim.algoscene import AlgoScene
from algomanim.algobinarytree import AlgoBinaryTree, AlgoBinaryTreeNode

class BinaryTreeScene(AlgoScene):
    def preconfig(self, settings):
        settings['node_size'] = 0.5
        settings['node_shape'] = 'circle'
        settings['highlight_color'] = "#e74c3c" # red

    def algo(self):
        vals = [4, 2, 3, 1, 5]
        root = AlgoBinaryTreeNode(self, vals[0])
        tree = AlgoBinaryTree(self, 2, root)
        for i in range(1, len(vals)):
            tree.insert(vals[i])

        tree.find(3)
