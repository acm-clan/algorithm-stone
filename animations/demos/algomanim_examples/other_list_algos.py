# pylint: disable=W0201, R0914
from manimlib import *
from algomanim.algoscene import AlgoScene
from algomanim.algolist import AlgoList


class FindMaxScene(AlgoScene):
    def algo(self):
        algolist = AlgoList(self, [25, 40, 5, 60, 50, 80])

        cur_max_idx = 0
        self.insert_pin('max_changed', algolist.get_val(cur_max_idx))

        for i in range(1, algolist.len()):
            if algolist.compare(cur_max_idx, i, text=True):
                cur_max_idx = i
                self.insert_pin('max_changed', algolist.get_val(cur_max_idx))

    def preconfig(self, settings):
        settings['node_shape'] = 'circle'
        settings['node_size'] = 1.5
        settings['highlight_color'] = '#33cccc'  # teal

    def customize(self):
        # add title to beginning
        text = self.add_text('Find Maximum Value', 0, position=2*UP)

        # search for pins that were previously set
        pins = self.find_pin('max_changed')
        for pin in pins:
            # extract val from list of args
            max_val = pin.get_args()[0]

            # find index to add text transformation to
            index = pin.get_index()

            # create new text object to morph to
            text = self.change_text(f'Current Max Value: {max_val}', text, index, position=2*UP)


class BinarySearchScene(AlgoScene):
    def algo(self):
        algolist = AlgoList(self, list(range(0, 31, 3)))
        val = 27
        mid_pt = 0
        first = 0
        last = algolist.len()-1
        index = -1

        self.insert_pin('intro', val)

        while (first <= last) and (index == -1):
            self.insert_pin('searching_range', algolist.nodes[first], algolist.nodes[last])

            mid_pt = (first+last)//2

            self.insert_pin('highlight', algolist.nodes[mid_pt])
            self.insert_pin('compare', algolist.get_val(mid_pt), val)
            self.insert_pin('dehighlight', algolist.nodes[mid_pt])

            if algolist.get_val(mid_pt) == val:
                index = mid_pt
            elif val < algolist.get_val(mid_pt):
                last = mid_pt -1
            else:
                first = mid_pt +1

        self.insert_pin('final_highlight', algolist.nodes[index])
        self.insert_pin('found_val', index)

    def preconfig(self, settings):
        settings['node_shape'] = 'circle'
        settings['node_size'] = 1
        settings['highlight_color'] = '#33cccc'  # teal

    def customize(self):
        # add introduction
        intro_pin = self.find_pin('intro')[0]
        index = intro_pin.get_index()
        val = intro_pin.get_args()[0]
        self.add_text(f'Find value, {val}, in Sorted List', 0, position=2*UP)

        # add animation for searching range box
        searching_range_pins = self.find_pin('searching_range')
        # box needs to be created at animation creation time
        self.custom_box = None
        # update surrounding box
        for pin in searching_range_pins:
            index = pin.get_index()
            first_node = pin.get_args()[0]
            last_node = pin.get_args()[1]
            self.add_static(index, self.update_surrounding_box, [first_node, last_node])

        # add highlight animations
        highlight_pins = self.find_pin('highlight')
        for pin in highlight_pins:
            index = pin.get_index()
            node = pin.get_args()[0]
            self.add_transform(index, ApplyMethod, args=[node.node.set_fill,
                                                         node.highlight_color])

        # add compare texts
        compare_pins = self.find_pin('compare')
        old_text = None
        for pin in compare_pins:
            index = pin.get_index()
            val1 = pin.get_args()[0]
            val2 = pin.get_args()[1]
            new_text = self.create_text(f'{val1}' \
                + ('<' if val1<val2 else ('>' if val1>val2 else '==')) \
                + f'{val2}')
            new_text.shift(UP)
            self.add_static(index, self.update_text, [old_text, new_text])
            old_text = new_text

        # add dehighlight animations
        dehighlight_pins = self.find_pin('dehighlight')
        for pin in dehighlight_pins:
            index = pin.get_index()
            node = pin.get_args()[0]
            self.add_transform(index, ApplyMethod, args=[node.node.set_fill,
                                                         node.node_color])

        # add found val text
        found_pin = self.find_pin('found_val')[0]
        index = found_pin.get_index()
        found_index = found_pin.get_args()[0]
        new_text = self.create_text(f'Found Value {val} at index {found_index}!')
        new_text.shift(UP)
        self.add_static(index, self.update_text, [old_text, new_text])
        old_text = new_text

        # add last highlight animations
        final_highlight_pins = self.find_pin('final_highlight')
        for pin in final_highlight_pins:
            index = pin.get_index()
            node = pin.get_args()[0]
            self.add_transform(index, ApplyMethod, args=[node.node.set_fill, '#ff6666'])

    # -------- customisation static functions -------- #

    def update_text(self, old_text, new_text):
        if old_text is not None:
            self.play(ReplacementTransform(old_text, new_text))
        else:
            self.add(new_text)

    def update_surrounding_box(self, first_node, last_node):
        old_box = self.custom_box
        new_box = SurroundingRectangle(VGroup(first_node.grp, last_node.grp))
        if old_box is None:
            self.add(new_box)
        else:
            self.play(ReplacementTransform(old_box, new_box))
        self.custom_box = new_box
