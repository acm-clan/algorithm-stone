from manimlib import *
from algomanim.algoscene import AlgoScene
from algomanim.algolist import AlgoList

class ShortBubbleSortScene(AlgoScene):
    def algo(self):
        algolist = AlgoList(self, [25, 43])
        swaps_made = True
        while swaps_made:
            swaps_made = False
            for i in range(algolist.len() - 1):
                j = i + 1
                if algolist.compare(i, j, text=True):
                    swaps_made = True
                    algolist.swap(i, j)

    def custom_fade_out_transform(self):
        self.save_mobjects = self.mobjects
        return list(map(FadeOut, self.save_mobjects))

    def custom_fade_in_transform(self):
        result = list(map(FadeIn, self.save_mobjects))
        self.save_mobjects = []
        return result

    def preconfig(self, settings):
        settings['highlight_color'] = "#FF0000"

    def customize(self):
        # demonstrating the allowed edits that can be made for animations

        # 1) find the animations for your different functions
        self.find_action_pairs(metadata_name='compare', occurence=2, lower_level='swap')

        # 2) animations are fast forwarded (2x speed) for second iteration
        self.fast_forward(45, 75)

        # 3) insert a wait in between animations
        self.add_wait(75)

        # 4) Add Custom Transforms into the list to be executed in runtime
        self.add_transform(76, self.custom_fade_out_transform)

        # 5) skip remaining animations from third iteration till the end
        self.skip(77)

        self.add_transform(len(self.action_pairs), self.custom_fade_in_transform)
