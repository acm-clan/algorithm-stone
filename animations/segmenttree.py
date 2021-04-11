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

    def construct(self):
        self.camera.background_rgba = [1, 1, 1, 0.5]
        self.start_logo()
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

    def construct(self):
        self.start_logo(animate=False)

        self.init_messaged("线段树是一棵树，从数组进行构造")

        array = AlgoVector(self, self.datas)
        array.shift(UP)
        self.play(ShowCreation(array))
        self.play(array.to_edge, LEFT)

        tree = AlgoSegTree(self, self.datas)
        tree.shift(UP*0.5).scale(0.9)
        self.play(ShowCreation(tree))
        self.play(tree.to_edge, RIGHT)

        self.show_message("问题规约：给你一个数组，将数组元素放到叶子节点，父节点为左右子树的和")
        # 
        self.wait()

class SegmentTreeBase(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datas = np.arange(6)

class SegmentTreeBuild(SegmentTreeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def travel(self, n:AlgoSegTreeNode):
        if n.l == n.r:
            # leaf
            node = self.tree.get_node(n.id)
            node.set_color(BLUE)
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
        array.set_color(BLUE)
        self.play(ShowCreation(array))
        self.play(array.to_edge, UP)
        self.array = array

        self.show_message("后序创建二叉树", delay=0)
        self.tree = AlgoSegTree(self, self.datas)
        self.tree.scale(0.9)
        self.tree.shift(UP*0.5)
        self.add(self.tree)
        self.tree.hide_all()
        self.travel(self.tree.root)

        self.play(Uncreate(self.tree), Uncreate(array))
        self.show_message("再来看看如何更新线段树")

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
        self.start_logo(animate=False)
        self.init_message("构造线段树")
        self.build_segment_tree()

class SegmentTreeUpdate(SegmentTreeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def find_element(self, node, val, new_val):
        if not node:
            return
        if node.l==node.r and node.v == val:
            n = self.tree.get_node(node.id)
            self.play(n.set_color, RED)
            self.show_message("修改元素")
            n.set_text(str(new_val))
            n.set_color(RED)
            node.v = new_val
            return

        if node.l == node.r:
            return

        self.find_element(node.left, val, new_val)
        self.find_element(node.right, val, new_val)
        old_v = node.v
        node.v = node.left.v + node.right.v
        if old_v != node.v:
            n = self.tree.get_node(node.id)
            self.show_message("更新元素%d -> %d"%(old_v, node.v))
            self.play(FocusOn(n))
            n.set_text(str(node.v))
            self.play(n.set_color, RED)

    def construct(self):
        self.start_logo(animate=False)
        self.init_message("更新线段树")
        array = AlgoVector(self, self.datas)
        array.set_color(BLUE)
        self.play(ShowCreation(array))
        self.play(array.to_edge, LEFT)
        self.array = array
        
        self.tree = AlgoSegTree(self, self.datas).scale(0.9)
        self.tree.to_edge(edge=RIGHT).shift(LEFT)
        self.play(ShowCreation(self.tree))
        # 3 -> 7
        self.show_messaged("比如将3更新为7")
        new_node = AlgoNode("7", color=RED)
        self.play(ShowCreation(new_node))
        self.play(new_node.next_to, self.array.get_node(3), DOWN)
        arrow = Arrow(new_node, self.array.get_node(3)).set_color(BLUE)
        self.play(ShowCreation(arrow))

        self.show_message("首先是找到元素")

        # find
        self.find_element(self.tree.root, 3, 7)
        self.wait(10)

class SegmentTreeQuery(SegmentTreeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def query(self, node, l, r):
        if node.l == l and node.r == r:
            self.play(self.tree.get_node(node.id).set_color, BLUE)
            self.show_message("找到区间[%d, %d]"%(l, r))
            self.wait()
            return node.v
        m = math.floor((node.l+node.r)/2)
        # 
        if r <= m:
            arrow = self.tree.get_edge(node.id, node.left.id)
            self.play(arrow.set_color, BLUE)
            return self.query(node.left, l, r)
        elif l >m:
            arrow = self.tree.get_edge(node.id, node.right.id)
            self.play(arrow.set_color, BLUE)
            return self.query(node.right, l, r)

        arrow = self.tree.get_edge(node.id, node.left.id)
        self.play(arrow.set_color, BLUE)
        arrow = self.tree.get_edge(node.id, node.right.id)
        self.play(arrow.set_color, BLUE)
        return self.query(node.left, l, m)+self.query(node.right, m+1, r)


    def construct(self):
        self.start_logo(animate=False)
        self.init_message("查询线段树")

        self.tree = AlgoSegTree(self, self.datas).scale(0.9).shift(UP*0.5)
        self.play(ShowCreation(self.tree))

        for i in range(0, 1):
            for j in range(i, 6):
                for k in self.tree.arrows:
                    v = self.tree.arrows[k]
                    v.set_color("#6e6e6c")
                for k in self.tree.node_objs:
                    v = self.tree.node_objs[k]
                    v.set_color("#6e6e6c")
                self.show_message("查询区间[%d,%d]的和"%(i, j))
                value = self.query(self.tree.root, i, j)
        self.show_message("完成线段树，谢谢观看")
        self.wait(10)
