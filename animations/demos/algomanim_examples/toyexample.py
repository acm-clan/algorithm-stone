# pylint: skip-file

from manimlib import *
from algomanim.algoscene import AlgoScene
from algomanim.algolist import AlgoList


class ToyScene(AlgoScene):
    def algo(self):
        algolist = AlgoList(self, [1, 3, 5, 2, 4])

        # algolist.highlight(*[0, 2, 4])
        # algolist.pop(4)
        left = algolist.slice(0, 5 // 2, move=LEFT, shift=True)
        # left.hide()
