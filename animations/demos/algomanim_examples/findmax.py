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
