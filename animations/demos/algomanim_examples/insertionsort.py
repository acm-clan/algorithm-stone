# pylint: disable = W0201
from manimlib import *
from algomanim.algoscene import AlgoScene
from algomanim.algolist import AlgoList


class InsertionSortScene(AlgoScene):
    def algo(self):
        self.insert_pin('intro')

        algolist = AlgoList(self, [25, 16, 39, 44, 5, 1])

        for i in range(algolist.len()):
            self.insert_pin('range', algolist.nodes[0], algolist.nodes[i])
            for j in range(0, i):
                self.insert_pin('highlight', algolist, [i, j])
                if algolist.compare(i, j, text=True):
                    algolist.swap(i, j)
            self.insert_pin('sorted')

    def customize(self):
        # add introduction
        intro_pin = self.find_pin('intro')[0]
        index = intro_pin.get_index()
        intro_text = self.create_text('Insertion Sort Algorithm')
        intro_text.shift(2*UP)
        intro_transform = lambda: Write(intro_text)
        self.add_transform(index, intro_transform)

        # add sliding window to show sorted range
        range_pins = self.find_pin('range')
        self.custom_box = None
        for pin in range_pins:
            index = pin.get_index()
            first_node = pin.get_args()[0]
            last_node = pin.get_args()[1]
            self.add_static(index, self.update_surrounding_box, [first_node, last_node])

        # add sorted text
        sorted_pins = self.find_pin('sorted')
        for pin in sorted_pins:
            index = pin.get_index()
            self.add_static(index, self.add_sorted_text)

    # -------- customisation static functions -------- #

    def update_surrounding_box(self, first_node, last_node):
        old_box = self.custom_box
        new_box = SurroundingRectangle(VGroup(first_node.grp, last_node.grp))
        if old_box is None:
            self.add(new_box)
        else:
            self.play(ReplacementTransform(old_box, new_box))
        self.custom_box = new_box

    def add_sorted_text(self):
        text = self.create_text('Sorted')
        text.next_to(self.custom_box, UP)
        text.align_to(self.custom_box, LEFT)
        self.play(Write(text))
        self.play(FadeOut(text))
