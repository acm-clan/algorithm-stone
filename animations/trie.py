from manim_imports_ext import *

class TrieScene(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = ["to", "tea", "ted", "ten", "inn", "in"]
        self.data_find = ["te", "ted", "ins"]

    def construct(self):
        self.go_speed_up()
        self.reset_speed_up()
        
        self.start_logo(subtitle="Trie前缀树", animate=True)
        self.init_message("Trie树也叫做前缀树、字典树")

        vector = AlgoVector(self, datas=self.data, is_rect=True)
        self.add(vector)
        vector.set_color(GOLD)
        self.play(vector.shift, UP*3.5)

        self.show_message("如上所示，有6个单词")
        self.show_message("前缀树是如何存储这些单词的呢？")
        self.show_message("我们先来看看前缀树的插入操作")
        
        tree = AlgoTrieTree(self)
        for w in self.data:
            tree.add_word(w)
            
        self.add(tree)
        
        self.show_message("前缀树的查询操作")

        vector2 = AlgoVector(self, datas=self.data_find, is_rect=True)
        vector2.shift(UP*3.5)
        vector2.set_color(GOLD)
        self.play(Transform(vector, vector2))
        
        i = 0
        for w in self.data_find:
            v = tree.query(w)
            if v:
                self.play(vector2.submobjects[i].set_color, BLUE)
            else:
                self.play(vector2.submobjects[i].set_color, GREEN)
            print("word %s %s"%(w, v))
            i += 1

        self.wait(2)
        self.show_message("完成Trie前缀树，谢谢观看！")
        self.wait(10)
