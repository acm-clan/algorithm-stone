from manimlib import *
from algomanim.algonode import AlgoNode
from algomanim.metadata import attach_metadata

class AlgoBinaryTreeNode(AlgoNode):
    def __init__(self, scene, val, parent=None):
        self.parent = parent
        self.left = None
        self.right = None
        self.id = None # pylint: disable=C0103

        self.recursive_update_depth()

        super().__init__(scene, val)
        if parent:
            self.lines[parent] = Line(ORIGIN, ORIGIN, stroke_width=5, color=WHITE), None

    def set_parent(self, parent):
        self.parent = parent
        self.lines[parent] = Line(ORIGIN, ORIGIN, stroke_width=5, color=WHITE), None

    def set_left(self, left):
        self.left = left
        self.left.set_parent(self)

        self.recursive_update_depth()

    def set_right(self, right):
        self.right = right
        self.right.set_parent(self)
        self.recursive_update_depth()

    def recursive_size(self):
        num_nodes = 1
        if self.left:
            num_nodes += self.left.recursive_size()
        if self.right:
            num_nodes += self.right.recursive_size()
        return num_nodes

    def recursive_insert(self, val):
        curr_node = self
        # If value is less than curr_node, insert to the left
        if val < curr_node.val:
            if curr_node.left is None:
                new_node = AlgoBinaryTreeNode(curr_node.scene, val, curr_node)
                curr_node.set_left(new_node)
                return new_node
            curr_node = curr_node.left
        # Else insert to the right
        else:
            if curr_node.right is None:
                new_node = AlgoBinaryTreeNode(curr_node.scene, val, curr_node)
                curr_node.set_right(new_node)
                return new_node
            curr_node = curr_node.right
        # curr_node is filled, try next one
        return curr_node.recursive_insert(val)

    def recursive_update_depth(self):
        if self.parent is None:
            self.id = 1
            self.depth = 1
        else:
            self.depth = self.parent.depth + 1
            if self.parent.left == self:
                self.id = self.parent.id * 2
            else:
                self.id = self.parent.id * 2 + 1

        if self.left is not None:
            self.left.recursive_update_depth()

        if self.right is not None:
            self.right.recursive_update_depth()

    def recursive_show(self, max_depth, metadata=None, animated=True, w_prev=False):
        self.show(max_depth, metadata=metadata, animated=animated, w_prev=w_prev)
        if self.left is not None:
            self.left.recursive_show(max_depth, metadata=metadata, animated=animated,
                w_prev=w_prev)

        if self.right is not None:
            self.right.recursive_show(max_depth, metadata=metadata, animated=animated,
                w_prev=w_prev)

    @attach_metadata
    def recursive_find(self, val, metadata=None, animated=True, w_prev=False):
        if self.val == val:
            super().highlight(metadata=metadata, animated=animated, w_prev=w_prev)
            super().dehighlight(metadata=metadata, animated=animated, w_prev=False)
            return self

        if val > self.val:
            return self.right.recursive_find(val)

        return self.left.recursive_find(val)

    def get_x_pos(self, node_id, max_depth):
        # finding the id of the middle leaf node OF THE WHOLE TREE
        total_leaf_nodes = 2 ** (max_depth - 1)
        middle_node_id = 2 ** (max_depth - 1) + (total_leaf_nodes - 1) / 2

        return int(middle_node_id - node_id) * \
            ((float(self.scene.settings['node_size']) + 0.5) * LEFT)

    def show(self, max_depth, metadata=None, animated=True, w_prev=False): # pylint: disable=W0221:
        levels = max_depth - self.depth

        # the 2 leaf nodes that this node needs to be at the center of
        leftmost_id = self.id * (2 ** levels)
        rightmost_id = leftmost_id + (2 ** levels) - 1

        pos_x = (self.get_x_pos(leftmost_id, max_depth) +
                    self.get_x_pos(rightmost_id, max_depth)) / 2
        pos_y = (self.depth - 1) * ((float(self.scene.settings['node_size']) + 0.5) * DOWN)

        self.grp.move_to(pos_x + pos_y)
        if self.parent is not None:
            self.add_line(self.parent, metadata=metadata,
                                             animated=animated, w_prev=w_prev)

        super().show(metadata=metadata, animated=animated, w_prev=True)


class AlgoBinaryTree:
    def __init__(self, scene, max_depth, root=None, show=True):
        self.root = root
        self.max_depth = max_depth + 1
        self.scene = scene

        if show:
            self.show_tree(animated=False)

    @attach_metadata
    def show_tree(self, metadata=None, animated=True, w_prev=False):
        ''' Display Tree on Sceen '''
        if self.root is not None:
            self.root.recursive_show(self.max_depth, metadata=metadata, animated=animated,
                w_prev=w_prev)

    @attach_metadata
    def insert(self, val, metadata=None, animated=True, w_prev=False):
        ''' Insert element into tree '''
        new_node = self.root.recursive_insert(val)
        new_node.recursive_show(self.max_depth, metadata=metadata, animated=animated,
            w_prev=w_prev)

    @attach_metadata
    def find(self, val, metadata=None, animated=True, w_prev=False):
        return self.root.recursive_find(val, metadata=metadata, animated=animated, w_prev=w_prev)

    def size(self):
        ''' Returns the total number of nodes of the tree '''
        return self.root.recursive_size()
