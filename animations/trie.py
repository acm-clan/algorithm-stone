from manim_imports_ext import *

class TrieScene(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = ["to", "tea", "ted", "ten", "inn", "in"]
        self.data_find = ["hello", "te", "ted", "ins"]

    def construct(self):
        # self.start_logo(subtitle="Trie前缀树")

        tree = AlgoTrieTree(self)
        for w in self.data:
            tree.add_word(w)

        for w in self.data_find:
            v = tree.query(w)
            print("word %s %s"%(w, v))

        self.wait(2)
