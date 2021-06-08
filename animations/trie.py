from manim_imports_ext import *

class TrieScene(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = ["to", "tea", "ted", "ten", "inn", "in"]
        self.data_find = ["hello", "te", "ted", "ins"]

    def construct(self):
        # self.start_logo(subtitle="Trie前缀树")

        vector = AlgoVector(self, datas=self.data)
        self.add(vector)
        self.play(vector.shift, UP*2)

        self.snapshot()

        tree = AlgoTrieTree(self)
        for w in self.data:
            tree.add_word(w)

        for w in self.data_find:
            v = tree.query(w)
            print("word %s %s"%(w, v))

        self.wait(2)
