from manimlib import *
from algomanim.algoscene import AlgoScene
from algomanim.algolist import AlgoList
from algomanim.algobinarytree import AlgoBinaryTree, AlgoBinaryTreeNode

class BinaryTreeSortScene(AlgoScene):
    def preconfig(self, settings):
        settings['node_size'] = 0.5
        settings['node_shape'] = 'circle'
        settings['highlight_color'] = "#e74c3c" # red

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

        self.insert_pin("finished")

    # pylint: disable=R0914
    def customize(self):
        pin = self.find_pin("list_elems")[0]
        idx = pin.get_index()
        text_position = 2 * UP

        title_text = self.add_text("First, we insert the elements of the list \
            into a binary tree", idx, text_position)

        self.add_wait(idx + 1, wait_time = 0.25)

        self.chain_pin_highlight("inserted_node")

        tree_finished_pin = self.find_pin("finished_tree_build")[0]
        idx2 = tree_finished_pin.get_index()
        title_text = self.change_text("Now, we do an INORDER traversal of the tree",
                                      title_text, index=idx2)
        self.fast_forward(idx + 2, idx2)

        self.chain_pin_highlight("visited_node")

        self.fast_forward(idx2 + 1)

        last_pin = self.find_pin("finished")[0]
        self.change_text("We have a sorted list!", title_text, index=last_pin.get_index())
