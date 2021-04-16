from manim_imports_ext import *

# 红黑树的噩梦，可以结束了

class RedBlackTreePreface(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        # self.start_logo(subtitle="红黑树")
        self.wait(100)

class RedBlackTreeWhatIs(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        self.wait()

class RedBlackTreeInsert(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def construct(self):
        tree = AlgoRBTree(self)
        max_value = 100
        n = 10
        random.seed(3)
        arr = np.random.choice(max_value, size=n, replace=False)
        print(arr)
        for i in arr:
            tree.set(i, i)
        tree.center()
        # self.play(ShowCreation(tree))
        # self.wait(10)

class RedBlackTreeDelete(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        pass

class RedBlackTreeRotate(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        tree = AlgoRBTree(self)
        n = 1000
        random.seed(3)
        arr = np.random.choice(n, size=n, replace=False)
        print(arr)
        for i in arr:
            tree.set(i, i)
        for i in arr:
            tree.remove(i)
        self.wait()

