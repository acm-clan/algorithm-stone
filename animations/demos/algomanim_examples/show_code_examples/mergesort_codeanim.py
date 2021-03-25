# pylint: skip-file
from manimlib import *
from algomanim.algoscene import AlgoScene
from algomanim.algolist import AlgoList


class MergeSortScene(AlgoScene):
    def algo(self):
        algolist = AlgoList(self, [4, 3, 1, 4])

        # ----- helper fns ----- #
        def mergesort(self, algolist):
            if algolist.len() > 1:
                # find middle index
                mid_pt = algolist.len() // 2  # 2
                # slice list into two
                left = algolist.slice(0, mid_pt, move=LEFT, shift=True)
                right = algolist.slice(mid_pt, algolist.len(), move=RIGHT)
                left = mergesort(self, left)
                right = mergesort(self, right)
                merged_list = algolist.merge(left, right, replace=True, shift=True, shift_vec=DOWN)
                merged_list.replace(algolist)
                return merged_list
            return algolist
        # ---------------------- #

        mergesort(self, algolist)

    def preconfig(self, settings):
        settings['show_code'] = True
