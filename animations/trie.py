from manim_imports_ext import *

class TrieScene(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = ["to", "tea", "ted", "ten", "inn", "in"]

    def construct(self):
        self.start_logo(subtitle="Trie前缀树")
        self.wait(2)
