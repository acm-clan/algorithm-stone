from manimlib import *
from algomanim.algoscene import AlgoScene, AlgoTransform
from algomanim.algolist import AlgoList

class MutableBubbleSortScene(AlgoScene):
    def algo(self):
        algolist = AlgoList(self, [25, 43, 5, 18, 30])
        swaps_made = True
        while swaps_made:
            swaps_made = False
            for i in range(algolist.len() - 1):
                j = i + 1
                val_i = algolist.get_val(i)
                val_j = algolist.get_val(j)
                self.insert_pin("compare", algolist.nodes[i], algolist.nodes[j])
                if val_i < val_j:
                    swaps_made = True
                    algolist.change_val(i, val_j)
                    algolist.change_val(j, val_i)

    def customize(self):
        self.chain_pin_highlight("compare")

    # pylint: disable=E1136, W0221
    def chain_pin_highlight(self, pin_str):
        pins = self.find_pin(pin_str)
        prev_pair = None
        for pin in pins:
            curr_pair = pin.get_args()
            idx = pin.get_index()

            if prev_pair is not None:
                anim_action = self.create_play_action(
                    AlgoTransform([prev_pair[0].node.set_fill,
                        self.settings['node_color']], transform=ApplyMethod,
                        color_index=1), w_prev=False
                )
                self.add_action_pair(anim_action, index=idx)
                idx += 1
                anim_action = self.create_play_action(
                    AlgoTransform([prev_pair[1].node.set_fill,
                        self.settings['node_color']], transform=ApplyMethod,
                        color_index=1), w_prev=True
                )
                self.add_action_pair(anim_action, index=idx)
                idx += 1

            anim_action = self.create_play_action(
                AlgoTransform([curr_pair[0].node.set_fill,
                    self.settings['highlight_color']], transform=ApplyMethod,
                    color_index=1), w_prev=prev_pair is not None
            )
            self.add_action_pair(anim_action, index=idx)
            idx += 1
            anim_action = self.create_play_action(
                AlgoTransform([curr_pair[1].node.set_fill,
                    self.settings['highlight_color']], transform=ApplyMethod,
                    color_index=1), w_prev=True
            )
            self.add_action_pair(anim_action, index=idx)
            prev_pair = curr_pair
