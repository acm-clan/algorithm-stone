# -*- encoding: utf-8 -*-
from manim_imports_ext import *

# 307.区域检索-数组可修改

class SegmentTreeDiffScene(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datas = np.array([1, 2, 3, 4, 5, 6])
        self.group = []
        for i in range(self.datas.shape[0]):
            self.group.append(i)

    def show_diff(self):
        self.show_message("首先，让我们来看看区间问题的常见3个解法")
        
        table = AlgoTable(self, np.array([
            ["",       "区间求和",  "区间最大值",  "区间修改",    "单点修改"],
            ["前缀和", AlgoCheckmark(), AlgoExmark(), AlgoExmark(), AlgoExmark(),],
            ["树状数组", AlgoCheckmark(), AlgoCheckmark(), AlgoExmark(), AlgoCheckmark(),],
            ["线段树", AlgoCheckmark(), AlgoCheckmark(), AlgoCheckmark(), AlgoCheckmark(),],
        ], dtype=object))

        self.play(ShowCreation(table), run_time=4)
        
        rect = SurroundingRectangle(table)
        self.play(ShowCreation(rect))

        self.show_message("前缀和、树状数组、线段树")

        self.show_message("前缀和一般用于固定的数组")
        
        self.show_message("树状数组是一种很高效的数据结构")
        self.show_message("功能能满足大部分需求")

        self.show_message("线段树则是一种非常灵活的数据结构")
        self.show_message("本动画重点讲解线段树")
        self.play(FadeOut(table), FadeOut(rect))

    def what_is_segment_tree(self):
        self.show_message("线段树是一棵树")

        self.show_message("从数组进行构造")

        array = AlgoVector(self, self.datas)
        self.play(ShowCreation(array))
        self.play(array.to_edge, LEFT)

        # 
        tree = AlgoSegTree(self, self.datas)
        self.play(ShowCreation(tree))
        self.play(tree.to_edge, RIGHT)

    def show_problem(self):
        pass

    def construct(self):
        # self.add_sound("bg2")
        # self.start_logo()
        self.init_message("线段树")
        self.show_diff()
        # 
        self.show_problem()
        # 
        self.wait(1)

class SegmentTreeWhatIs(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datas = np.array([1, 2, 3, 4, 5, 6])
        self.group = []
        for i in range(self.datas.shape[0]):
            self.group.append(i)

    def what_is_segment_tree(self):
        self.show_message("线段树是一棵树")
        self.show_message("从数组进行构造")

        array = AlgoVector(self, self.datas)
        self.play(ShowCreation(array))
        self.play(array.to_edge, LEFT)

        tree = AlgoSegTree(self, self.datas)
        self.play(ShowCreation(tree))
        self.play(tree.to_edge, RIGHT)

        self.show_message("问题转换：给你一个数组，将数组元素放到叶子节点，父节点为左右子树的和")

    def show_problem(self):
        pass

    def construct(self):
        # self.init_message("线段树是一棵树")
        self.what_is_segment_tree()
        # 
        self.wait()

class SegmentTreeBase(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.datas = np.random.randint(100, size=8)
        self.datas = np.arange(6)
        print("datas:", self.datas)

class SegmentTreeBuild(SegmentTreeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def travel(self, n:AlgoSegTreeNode):
        if n.l == n.r:
            # leaf
            self.tree.show_node(n.id)
            return
        self.travel(n.left)
        self.travel(n.right)
        # parent
        self.tree.show_node(n.id)
        self.tree.show_edge(n.id, n.left.id)
        self.tree.show_edge(n.id, n.right.id)

    def build_segment_tree(self):
        array = AlgoVector(self, self.datas)
        self.play(ShowCreation(array))
        self.play(array.to_edge, UP)
        self.array = array

        self.show_message("后序创建二叉树")
        self.tree = AlgoSegTree(self, self.datas)
        self.tree.shift(UP)
        self.add(self.tree)
        self.tree.hide_all()
        self.travel(self.tree.root)

        # add image
        image = ImageMobject("assets/segment-tree-build.png")
        self.play(ShowCreation(image))

    def find_element(self, node, val, new_val):
        if node.l==node.r and node.v == val:
            n = self.tree.get_node(node.id)
            self.play(n.set_color, RED)
            self.show_message("修改元素")
            n.set_text(str(new_val))
            n.v = new_val
            return
        self.find_element(node.l, val, new_val)
        self.find_element(node.r, val, new_val)
        node.v = node.l.v + node.r.v
        n = self.tree.get_node(node.id)
        n.set_text(str(node.v))
        self.show_message("更新节点")
        self.play(FocusOn(n))

    def construct(self):
        self.init_message("构造线段树")
        self.build_segment_tree()
        # 
        self.show_message("当我们学会创建线段树之后，我们就基本明白了线段树是什么")
        self.show_message("接下来，让我们看看如何单点更新元素")

        # 3 -> 7
        new_node = AlgoNode("7")
        self.play(ShowCreation(new_node))
        self.play(new_node.next_to, self.array.get_node(3), DOWN)
        self.show_message("首先是找到元素")
        self.find_element(self.tree.root, 3, 7)
        self.wait(10)

class SegmentTreeUpdate(SegmentTreeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_segment_tree(self):
        self.tree = AlgoSegTree(self, self.datas)
        self.tree.shift(UP)
        self.add(self.tree)

    def find_element(self, node, val, new_val):
        if node.l==node.r and node.v == val:
            n = self.tree.get_node(node.id)
            self.play(n.set_color, RED)
            self.show_message("修改元素")
            n.set_text(str(new_val))
            n.v = new_val
            return
        self.find_element(node.l, val, new_val)
        self.find_element(node.r, val, new_val)
        node.v = node.l.v + node.r.v
        n = self.tree.get_node(node.id)
        n.set_text(str(node.v))
        self.show_message("更新节点")
        self.play(FocusOn(n))

    def construct(self):
        self.init_message("构造线段树")
        self.build_segment_tree()
        # 
        self.show_message("当我们学会创建线段树之后，我们就基本明白了线段树是什么")
        self.show_message("接下来，让我们看看如何单点更新元素")

        # 3 -> 7
        new_node = AlgoNode("7")
        self.play(ShowCreation(new_node))
        self.play(new_node.next_to, self.array.get_node(3), DOWN)
        self.show_message("首先是找到元素")
        self.find_element(self.tree.root, 3, 7)
        self.wait(10)

class SegmentTreeQuery(SegmentTreeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_segment_tree(self):
        self.show_message("后序创建二叉树")
        self.tree = AlgoSegTree(self, self.datas)
        self.tree.shift(UP)
        self.add(self.tree)
        self.tree.hide_all()
        self.travel(self.tree.root)

    def find_element(self, node, val, new_val):
        if node.l==node.r and node.v == val:
            n = self.tree.get_node(node.id)
            self.play(n.set_color, RED)
            self.show_message("修改元素")
            n.set_text(str(new_val))
            n.v = new_val
            return
        self.find_element(node.l, val, new_val)
        self.find_element(node.r, val, new_val)
        node.v = node.l.v + node.r.v
        n = self.tree.get_node(node.id)
        n.set_text(str(node.v))
        self.show_message("更新节点")
        self.play(FocusOn(n))

    def construct(self):
        self.init_message("构造线段树")
        self.build_segment_tree()
        # 
        self.show_message("再来看看如何查询线段树")

        self.show_message("比如查询区间[2,2]")

        
        self.wait(10)


class MainScene(AlgoScene):
    def construct(self):
        SegmentTreeWhatIs().construct()
        SegmentTreeBuild().construct()
        SegmentTreeUpdate().construct()
        SegmentTreeQuery().construct()

        self.finish()
