from manim_imports_ext import *

# 红黑树的噩梦，可以结束了

class RBPropertyPanel(AlgoVGroup):
    def __init__(self, scene, **kwargs):
        super().__init__(**kwargs)

        arr = [AlgoText("1 每个节点是红色或者黑色，包括叶子nil节点"),
        AlgoText("2 根节点是黑色"),
        AlgoText("3 叶子节点是黑色"),
        AlgoText("4 如果一个节点是红色，则其子节点都是黑色"),
        AlgoText("5 对于每一个节点，从该节点到叶子节点的所有路径上，黑色节点数量相同")]
        text_group = VGroup()
        text_group.add(*arr)
        text_group.arrange(direction=DOWN)
        self.add(text_group)

        rect = SurroundingRectangle(text_group)
        self.add(rect)
        self.center()

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
        self.init_message("红黑树的性质")
        tree = AlgoRBTree(self)
        tree.ctx.insert_message = False
        tree.ctx.delete_message = False
        tree.ctx.animate = False

        self.add(tree)
        max_value = 100
        n = 8
        random.seed(3)
        arr = np.random.choice(max_value, size=n, replace=False)
        tree.shift(UP*2)
        for i in arr:
            tree.set(i, i)

        # 
        self.show_message("红黑树是自平衡二叉查找树")
        self.show_message("左孩子的值大于根节点")
        self.show_message("右孩子的值小于根节点")
        self.show_message("左右子树分别为二叉查找树")
        self.show_message("红黑树有5条性质")

        p = RBPropertyPanel(self)
        p.to_edge(RIGHT)
        self.play(ShowCreation(p))

        self.snapshot()

        self.show_message("1 每个节点是红色或者黑色，包括叶子nil节点")
        self.show_message("2 根节点是黑色")
        self.show_message("3 叶子节点是黑色")
        self.show_message("4 如果一个节点是红色，则其子节点都是黑色")
        self.show_message("5 对于每一个节点，从该节点到叶子节点的所有路径上，黑色节点数量相同")
        
        self.wait()

class RedBlackTreeRotate(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        self.init_message("红黑树的旋转")
        tree = AlgoRBTree(self)
        tree.ctx.insert_message = True
        tree.ctx.delete_message = False
        tree.ctx.animate = True
        self.add(tree)

        arr = [1,2,3]
        v = AlgoVector(self, arr)
        self.play(ShowCreation(v))
        self.play(v.to_edge, UP)

        self.show_message("插入和删除操作会破坏红黑树的5条性质")
        self.show_message("维护这5条性质是通过旋转来完成的")
        self.show_message("来看这3个节点的插入操作")

        tree.shift(UP*2)
        for i in arr:
            tree.set(i, i)

        self.show_message("节点3插入后，需要左旋达到平衡")

        self.show_message("如果节点换成是[3, 2, 1]")
        arr = [3, 2, 1]
        v2 = AlgoVector(self, arr)
        v2.to_edge(UP)
        self.play(Transform(v, v2))
        self.play(Uncreate(tree))
        self.remove(tree)

        tree = AlgoRBTree(self)
        tree.ctx.insert_message = True
        tree.ctx.delete_message = False
        tree.ctx.animate = True
        self.add(tree)
        tree.shift(UP*2)
        for i in arr:
            tree.set(i, i)

        self.show_message("节点1插入后，需要右旋达到平衡")

        self.wait()

# 3 case
class RedBlackTreeInsert(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def construct(self):
        self.init_message("红黑树插入")
        tree = AlgoRBTree(self)
        self.add(tree)
        max_value = 100
        n = 8
        random.seed(3)
        arr = np.random.choice(max_value, size=n, replace=False)
        print(arr)
        tree.shift(UP*2)
        for i in arr:
            tree.set(i, i)
        for i in arr:
            tree.delete(i)

# 4 case
class RedBlackTreeDelete(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        pass

class RedBlackTreeEnd(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        pass