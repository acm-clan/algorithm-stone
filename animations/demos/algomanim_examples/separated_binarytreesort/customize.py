from manimlib import *

# pylint: disable=R0914,W0613
def my_customize(self):
    pin = self.find_pin("list_elems")[0]
    idx = pin.get_index()
    text_position = 2 * UP

    title_text = self.add_text("First, we insert the elements of the list \
        into a binary tree", idx, text_position)

    self.add_wait(idx + 1, wait_time = 0.25)

    chain_pin_highlight(self, "inserted_node")

    tree_finished_pin = self.find_pin("finished_tree_build")[0]
    idx2 = tree_finished_pin.get_index()
    self.fast_forward(idx + 2, idx2)
    title_text = self.change_text("Now, we do an INORDER traversal of the tree",
        title_text, idx2)

    chain_pin_highlight(self, "visited_node")

    self.fast_forward(idx2 + 1)
    self.change_text("We have a sorted list!", title_text)

def chain_pin_highlight(self, pin_str):
    pins = self.find_pin(pin_str)
    prev_node = None
    node_highlight = lambda node: \
        [ApplyMethod(node.node.set_fill, self.settings['highlight_color'])]
    node_dehighlight = lambda node: \
        [ApplyMethod(node.node.set_fill, self.settings['node_color'])]
    for pin in pins:
        node = pin.get_args()[0]
        self.add_transform(pin.get_index(), node_highlight, [node])
        if prev_node is not None:
            self.add_transform(pin.get_index() + 1, node_dehighlight, [prev_node])
        prev_node = node
