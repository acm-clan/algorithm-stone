# pylint: disable=E1101, W0105, R0913
from manimlib import *
from algomanim.algonode import AlgoNode
from algomanim.algoaction import AlgoTransform, AlgoSceneAction
from algomanim.metadata import LowerMetadata
from algomanim.algoobject import AlgoObject
from algomanim.metadata import Metadata, attach_metadata


class AlgoList(AlgoObject):

    '''
    Animated List data structure

    Args:
        scene (AlgoScene): AlgoScene containing this list
        arr ([]): List of values to be displayed as AlgoNodes
        show (bool): Whether this scene is shown with animation
        displacement: Vector indicating the list's position wrt to the origin

    Attributes:
        nodes (AlgoNode[]): List of AlgoNodes created from the input values
        grp (VGroup): A Manim VGroup of the Manim objects corresponding to the nodes
    '''

    def __init__(self, scene, arr, show=True, displacement=None):
        super().__init__(scene)

        # Make and arrange nodes
        self.nodes = [AlgoNode(scene, val) for val in arr]
        self.displacement = ORIGIN if displacement is None else displacement
        if displacement is not None and len(self.nodes) > 0:
            self.nodes[0].grp.move_to(displacement)

        for i in range(1, len(self.nodes)):
            self.nodes[i].grp.next_to(self.nodes[i - 1].grp, RIGHT)

        # Group nodes together
        self.grp = None
        self.group(immediate_effect=True)

        # Subscribe to the scene for scene transformations like Shifts
        scene.track_algoitem(self)

        if show:
            initialisation_meta = Metadata("create_list")
            self.center(animated=False, metadata=initialisation_meta)
            self.show_list(animated=False, metadata=initialisation_meta)
            self.scene.add_metadata(initialisation_meta)

    @attach_metadata
    def swap(self, i, j, metadata=None, animated=True, w_prev=False):
        ''' Swaps the nodes at indexes i and j '''
        temp = self.nodes[i]
        self.nodes[i] = self.nodes[j]
        self.nodes[j] = temp
        self.nodes[i].swap_with(self.nodes[j], metadata=metadata, animated=animated, w_prev=w_prev)

    @attach_metadata
    def compare(self, i, j, metadata=None, animated=True, w_prev=False,
                highlights=True, text=False):
        ''' Compare two nodes at indexes i and j '''
        if highlights:
            # Add highlight animations
            self.dehighlight(*list(range(len(self.nodes))),
                             metadata=metadata, animated=animated, w_prev=w_prev)
            self.highlight(i, j, metadata=metadata, animated=animated, w_prev=w_prev)
        # Get nodes' values
        val1 = self.get_val(i)
        val2 = self.get_val(j)
        if text:
            # Add associated text
            self.add_text(f"{str(val1)}"
                          + ("<" if val1<val2 else (">" if val1>val2 else "=="))
                          + f"{str(val2)}",
                          "compare", UP,
                          metadata=metadata, animated=animated, w_prev=w_prev)
        return val1 < val2


    def group(self, metadata=None, immediate_effect=False):
        ''' Restores the internal VGroup of list nodes, especially if the list has been edited '''
        def group():
            self.grp = VGroup(*[n.grp for n in self.nodes])

        # Update the VGroup of the list
        if immediate_effect:
            group()
        else:

            dummy_action = AlgoSceneAction.create_static_action(group, [])
            dummy_action_pair = self.scene.add_action_pair(dummy_action,
                                                           dummy_action, animated=False)

            # Not designed to be a Higher level func
            if metadata:
                lower_meta = LowerMetadata.create(dummy_action_pair,
                                                  [n.val for n in self.nodes], show_in_panel=False)
                metadata.add_lower(lower_meta)

    @attach_metadata
    def show_list(self, metadata=None, animated=True, w_prev=False):
        ''' Display the list on screen '''
        if self.empty():
            # empty list, nothing to do
            return

        # Show all nodes in the list
        for node in self.nodes:
            node.show(metadata=metadata, animated=animated, w_prev=w_prev)

    @attach_metadata
    def hide_list(self, metadata=None, animated=True, w_prev=False):
        ''' Hide the list from screen '''
        if self.empty():
            # empty list, nothing to do
            return

        # Hide all nodes in list at the same time
        AlgoObject.loop_fn_w_prev(self.nodes, AlgoNode.hide,
                                  animated=animated, metadata=metadata, init_w_prev=w_prev)

        # Unsubscribe from the scene
        self.scene.untrack_algoitem(self)

    @attach_metadata
    def highlight(self, *indexes, metadata=None, animated=True, w_prev=False):
        ''' Highlight nodes at the specified indexes '''
        nodes_to_highlight = [self.nodes[i] for i in indexes]

        # Highlight all nodes at the same time
        AlgoObject.loop_fn_w_prev(nodes_to_highlight, AlgoNode.highlight,
                                  animated=animated, metadata=metadata, init_w_prev=w_prev)

    @attach_metadata
    def dehighlight(self, *indexes, metadata=None, animated=True, w_prev=False):
        ''' Dehighlight nodes at the specified indexes '''
        nodes_to_dehighlight = [self.nodes[i] for i in indexes]

        # Dehighlight all nodes at the same time
        AlgoObject.loop_fn_w_prev(nodes_to_dehighlight, AlgoNode.dehighlight,
                                  animated=animated, metadata=metadata, init_w_prev=w_prev)

    def get_val(self, index):
        ''' Returns the value of the node at the given index '''
        return self.nodes[index].val

    def change_val(self, index, val):
        ''' Change the value of the node at the given index '''
        self.nodes[index].change_value(val)

    def len(self):
        ''' Returns the length of the list '''
        return len(self.nodes)

    def empty(self):
        ''' Returns true if the list is empty '''
        return not self.nodes

    @attach_metadata
    def append(self, val, metadata=None, animated=True, w_prev=False, center=True):
        ''' Appends a new node with the given value to the end of the list '''
        node = AlgoNode(self.scene, val)

        if self.empty():
            node.grp.move_to(self.displacement)
        else:
            node.set_next_to(self.nodes[-1], RIGHT, metadata=metadata)

        self.nodes.append(node)
        # Update positioning of list
        node.show(metadata=metadata, animated=animated, w_prev=w_prev)

        # Update the VGroup of the list
        self.group(metadata=metadata, immediate_effect=True)

        # Center list
        if center:
            self.center(metadata=metadata, animated=animated, w_prev=False)

    @attach_metadata
    def pop(self, i=None, metadata=None, animated=True):
        '''
        Removes the node at the specified index and closes the gap in the list if necessary
        If no index is specified, removes the last node by default
        '''
        if i is None:
            i = self.len()-1
        elif i < 0 or i >= self.len():
            return
        left_node = self.nodes[i - 1] if i != 0 else None
        right_nodes = self.nodes[i + 1:] if i != len(self.nodes) - 1 else None

        self.nodes[i].hide(metadata=metadata, animated=animated)
        self.nodes.remove(self.nodes[i])

        # Update the VGroup of the list
        self.group(metadata=metadata)

        if right_nodes is not None and left_node is not None:
            # gap only needs to be closed if there are nodes on the left and right
            # if not, simply centering the remaining list would be enough
            right_grp = VGroup(*[node.grp for node in right_nodes])

            anim_action = self.scene.create_play_action(
                AlgoTransform([right_grp.next_to, left_node.grp, RIGHT], transform=ApplyMethod)
            )
            static_action = AlgoSceneAction.create_static_action(
                right_grp.next_to,
                [left_node.grp, RIGHT]
            )

            action_pair = self.scene.add_action_pair(anim_action, static_action, animated=animated)

            # Initialise a LowerMetadata class for this low level function
            lower_meta = LowerMetadata("pop", action_pair)
            metadata.add_lower(lower_meta)

    @staticmethod
    def align_nodes_from_first_node(algolist, metadata, w_prev=False):
        '''
        Re-aligns nodes starting from the node at the start of the list
        No need for w_prev as it is currently non-animated
        '''
        for i in range(1, algolist.len()):
            algolist.nodes[i].set_next_to(algolist.nodes[i - 1], RIGHT,
                                          metadata=metadata, animated=False,
                                          w_prev=w_prev)

    @staticmethod
    def align_nodes_from_last_node(algolist, metadata, w_prev=False):
        '''
        Re-aligns nodes starting from the node at the end of the list
        No need for w_prev as it is currently non-animated
        '''
        for i in reversed(range(0, algolist.len() - 1)):
            algolist.nodes[i].set_next_to(algolist.nodes[i + 1], LEFT,
                                          metadata=metadata, animated=False,
                                          w_prev=w_prev)

    @attach_metadata
    def slice(self, start, stop, move=LEFT, metadata=None,
              animated=True, shift=False, shift_vec=UP):
        '''
        Slices the list, returning the equivalent of list[start: stop]
        Set move to LEFT, RIGHT or 0 (no movement) to denote which direction
        the slice should be shifted in
        The slice must be contiguous
        '''
        # Fix indices if needed
        if start < 0:
            start = 0
        if stop > self.len():
            stop = self.len()

        # Highlight the sublist we want to keep
        self.highlight(*range(start, stop), animated=animated, metadata=metadata)

        # Dehighlight the sublist we want to keep
        self.dehighlight(*range(start, stop), animated=animated, metadata=metadata)

        '''
        The sliced list is first aligned to its original position in the list.
        The hidden list is positioned where the sliced list will end up,
        and its center is used to define the movement of the sliced list.
        Both slices are hidden from the screen during this process.
        '''

        # Shift the scene up so that that we make space for the new list
        if shift:
            self.scene.shift_scene(shift_vec, metadata=metadata)

        # Create sliced list in background
        sublist = AlgoList(self.scene,
                           [n.val for n in self.nodes][start:stop], show=False)

        # Align to its original position in the list
        sublist.nodes[0].set_next_to(self.nodes[start], 0, metadata=metadata)
        AlgoList.align_nodes_from_first_node(sublist, metadata=metadata)

        hidden_sublist = AlgoList(self.scene,
                                  [0 for _ in self.nodes][start:stop], show=False)

        # Position hidden sliced list by taking reference from last element
        hidden_sublist.nodes[-1].set_next_to(self.nodes[stop - 1], DOWN + move,
                                             metadata=metadata)
        AlgoList.align_nodes_from_last_node(hidden_sublist, metadata=metadata)

        sublist.set_next_to(hidden_sublist, vector=0,
                            panel_name="move_slice", specific_val=[n.val for n in sublist.nodes],
                            metadata=metadata, animated=True)

        # Get rid of hidden_sublist
        hidden_sublist.hide_list(metadata=metadata, animated=False)

        return sublist

    @attach_metadata
    def concat(self, other_list, metadata=None, animated=True, w_prev=False, center=False):
        ''' Concatenates this list and other_list, then centres them '''
        # Set other list to the right of this list
        other_list.set_next_to(self, RIGHT, metadata=metadata, animated=animated, w_prev=w_prev)

        # Add lists together
        self.nodes += other_list.nodes

        # Update the VGroup of the list
        self.group(metadata=metadata)

        if center:
            self.center(metadata=metadata, animated=animated, w_prev=w_prev)

        return self

    # pylint: disable=R0914, R0915
    @attach_metadata
    def merge(self, left_list, right_list, metadata=None, animated=True,
              replace=False, shift=False, shift_vec=UP):
        '''
        Merges left_list and right_list, returning the resultant list
        If replace is True, hides left_list and right_list, then moves
        merged_list to the midpoint of both lists
        '''
        # make hidden copies of left_list and right_list at their respective positions
        left_list_copy = AlgoList(self.scene, [n.val for n in left_list.nodes], show=False)
        left_list_copy.set_next_to(left_list, vector=0, animated=False)

        right_list_copy = AlgoList(self.scene, [n.val for n in right_list.nodes], show=False)
        right_list_copy.set_next_to(right_list, vector=0, animated=False)

        # reveal the copies silently
        left_list_copy.show(animated=False)
        right_list_copy.show(animated=False)

        # create a hidden dummy list of the final length
        left_len = left_list.len()
        right_len = right_list.len()

        final_len = left_len + right_len
        hidden_merged_list = AlgoList(self.scene, [0 for _ in range(0, final_len)], show=False)

        # arrange the hidden list between and below the two lists
        hidden_merged_list.nodes[0].set_next_to(left_list_copy.nodes[0], DOWN,
                                                metadata=metadata, animated=False)
        AlgoList.align_nodes_from_first_node(hidden_merged_list, metadata=metadata)
        hidden_merged_list.center_x([left_list_copy, right_list_copy],
                                    metadata=metadata, animated=False)

        # show the merge by moving the copied nodes to the respective places
        left_index = 0
        right_index = 0
        curr_index = 0

        merged_list_vals = []

        while left_index < left_len and right_index < right_len:

            fst_left = left_list_copy.nodes[left_index]
            fst_right = right_list_copy.nodes[right_index]

            # highlight the nodes to be compared
            fst_left.highlight(metadata=metadata, animated=animated)
            fst_right.highlight(metadata=metadata, animated=animated, w_prev=True)

            fst_left.dehighlight(metadata=metadata, animated=animated)
            fst_right.dehighlight(metadata=metadata, animated=animated, w_prev=True)

            # select the smaller node
            node_to_move = fst_left
            if node_to_move.val > fst_right.val:
                node_to_move = fst_right
                right_index += 1
            else:
                left_index += 1

            # highlight and move the node
            node_to_move.highlight(metadata=metadata, animated=animated)
            node_to_move.set_next_to(hidden_merged_list.nodes[curr_index],
                                     panel_name="merge_item", specific_val=[node_to_move.val],
                                     vector=0, animated=animated, metadata=metadata)

            # track the added value
            merged_list_vals.append(node_to_move.val)

            # increment curr_index
            curr_index += 1

        if left_index == left_len and right_index != right_len:
            # left list was exhausted
            rem_right = VGroup(*[n.grp for n in right_list_copy.nodes[right_index:]])
            rem_hidden = VGroup(*[n.grp for n in hidden_merged_list.nodes[curr_index:]])

            # highlight right slice
            right_list_copy.highlight(*range(right_index, right_len),
                                      metadata=metadata, animated=animated)

            vals_to_move = [n.val for n in right_list_copy.nodes[right_index:]]
            merged_list_vals += vals_to_move

            # move it accordingly
            AlgoObject.move_group_to_group(self.scene, rem_right, rem_hidden,
                                           panel_name="merge_rest", specific_val=vals_to_move,
                                           animated=animated, metadata=metadata)
        elif right_index == right_len and left_index != left_len:
            # right list was exhausted
            rem_left = VGroup(*[n.grp for n in left_list_copy.nodes[left_index:]])
            rem_hidden = VGroup(*[n.grp for n in hidden_merged_list.nodes[curr_index:]])

            # highlight left slice
            left_list_copy.highlight(*range(left_index, left_len),
                                     metadata=metadata, animated=animated)

            vals_to_move = [n.val for n in left_list_copy.nodes[left_index:]]
            merged_list_vals += vals_to_move

            # move it accordingly
            AlgoObject.move_group_to_group(self.scene, rem_left, rem_hidden,
                                           panel_name="merge_rest", specific_val=vals_to_move,
                                           animated=animated, metadata=metadata)

        # silently create the final merged list and arrange it
        merged_list = AlgoList(self.scene, merged_list_vals, show=False)
        merged_list.set_next_to(hidden_merged_list, vector=0,
                                metadata=metadata)

        # show the final merged list and hide the list copies
        merged_list.show(metadata=metadata, animated=False)

        left_list_copy.hide_list(metadata=metadata, animated=False)
        right_list_copy.hide_list(metadata=metadata, animated=False)
        hidden_merged_list.hide_list(metadata=metadata, animated=False)

        if replace:
            merged_list.replace(left_list, right_list,
                                animated=animated, metadata=metadata)

        if shift:
            self.scene.shift_scene(shift_vec, metadata)

        return merged_list

    @attach_metadata
    def replace(self, *lists, animated=True, metadata=None, shift=False,
                shift_vec=UP, w_prev=False):
        '''
        Destroys the given list(s) and moves this list to its/their original position
        Given lists assumed to be in a single line
        '''
        # hide all the given lists at the same time
        AlgoObject.loop_fn_w_prev(lists, AlgoList.hide_list,
                                  animated=animated, metadata=metadata, init_w_prev=w_prev)

        # move this list to the middle pt found
        self.move_to_calculated_pt(lists, pt_fn=AlgoObject.center_up_pt,
                                   panel_name="replace",
                                   metadata=metadata, animated=animated)

        if shift:
            self.scene.shift_scene(shift_vec, metadata)
