from manimlib import *
from algomanim.algoscene import AlgoScene
from algomanim.algolist import AlgoList
from algomanim.algobinarytree import AlgoBinaryTree, AlgoBinaryTreeNode
from .preconfig import my_preconfig
from .customize import my_customize

# pylint: disable=R0914
class BinaryTreeSortScene(AlgoScene):
    preconfig = my_preconfig
    customize = my_customize

    def inorder_traversal(self, node, curr_list):
        if node is None:
            return
        self.inorder_traversal(node.left, curr_list)
        self.insert_pin("visited_node", node)
        curr_list.append(node.val)
        self.inorder_traversal(node.right, curr_list)

    def algo(self):
        unsorted_list = [25, 43, 5, 18, 30, 3, 50]
        algolist = AlgoList(self, unsorted_list, displacement=UP)
        self.insert_pin("list_elems")

        self.insert_pin("inserted_node", algolist.nodes[0])
        root = AlgoBinaryTreeNode(self, algolist.nodes[0].val)
        algotree = AlgoBinaryTree(self, 3, root)
        for node in algolist.nodes[1:]:
            self.insert_pin("inserted_node", node)
            algotree.insert(node.val)

        self.insert_pin("finished_tree_build")
        sorted_list = AlgoList(self, [], displacement=3.5 * DOWN)
        self.inorder_traversal(root, sorted_list)
