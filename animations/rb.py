from manim_imports_ext import *
import io

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

    def compare_nodes(self, a, b, cmp):
        left = a.copy()
        right = b.copy()

        p = LEFT*4+UP*3

        self.play(ApplyMethod(left.move_to, p+LEFT*0.6), ApplyMethod(right.move_to, p+RIGHT*0.6), run_time=1)
        t = AlgoText(cmp, color=RED).next_to(left).shift(LEFT*0.05)
        self.play(FadeIn(t))
        self.wait(2)
        self.play(FadeOut(left), FadeOut(right), FadeOut(t))

    def hide_and_show(self, tree:AlgoRBTree, root):
        el = tree.get_edge(tree.root.id, tree.root.left.id)
        er = tree.get_edge(tree.root.id, tree.root.right.id)
        self.play(FadeOut(root), FadeOut(el), FadeOut(er))
        self.wait(2)
        self.play(FadeIn(root), FadeIn(el), FadeIn(er))
        self.wait()

    def indicate_nils(self, tree):
        self.reset_speed_up()
        nils = tree.get_nil_nodes()
        self.indicate_nodes(tree, nils)
        

    def indicate_nodes(self, tree, nodes):
        animations = []
        for k in nodes:
            a = ApplyWave(k)
            b = CircleIndicate(k, color=RED)
            animations.append(b)
            animations.append(a)
        self.play(*animations, run_time=1.5)

    def construct(self):
        self.go_speed_up()
        self.start_logo(subtitle="红黑树")
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
        tree.ctx.animate = True
        tree.update_nodes()

        self.show_message("红黑树是一种二叉查找树")
        root = tree.get_node(tree.root.id)
        left = tree.get_node(tree.root.left.id)
        right = tree.get_node(tree.root.right.id)

        self.show_message("左孩子的值小于根节点")
        self.compare_nodes(left, root, "<")

        self.show_message("右孩子的值大于根节点")
        self.compare_nodes(right, root, ">")
        
        self.show_message("任意节点左右子树分别为二叉查找树")
        self.hide_and_show(tree, root)

        self.show_message("红黑树有5条性质")

        text_list = [
            "1 每个节点是红色或者黑色",
            "2 根节点是黑色",
            "3 叶子nil节点是黑色",
            "4 如果一个节点是红色，则其子节点都是黑色",
            "5 对于每一个节点，从该节点到叶子节点的所有路径上，黑色节点数量相同",
        ]
        
        self.play(ApplyMethod(self.camera.frame.shift, RIGHT*3.0))
        panel = AlgoPropertyPanel(self, text_list).scale(0.7)
        panel.next_to(tree).shift(UP+LEFT*1.5)
        self.play(ShowCreation(panel))

        self.show_message("1 每个节点是红色或者黑色，包括叶子nil节点")
        panel.light(0)
        
        self.show_message("2 根节点是黑色")
        root_node = tree.get_node(tree.root.id)
        self.play(ApplyWave(root_node), CircleIndicate(root_node, color=RED, run_time=2))
        panel.light(1)

        self.show_message("3 叶子nil节点是黑色")
        self.indicate_nils(tree)
        panel.light(2)
        
        self.show_message("4 如果一个节点是红色，则其子节点都是黑色")
        n = tree.root.right
        l = n.left
        r = n.right
        self.indicate_nodes(tree, [tree.get_node(n.id), tree.get_node(l.id), tree.get_node(r.id)])
        panel.light(3)

        self.reset_speed_up()
        self.show_message("5 对于每一个节点，从该节点到叶子节点的所有路径上，黑色节点数量相同")
        self.show_message("如上树中根节点到所有叶子节点的黑色节点数量都是3")
        panel.light(4)
        
        self.wait()

class RedBlackTreeRotate(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_left(self):
        tree = AlgoRBTree(self)
        tree.ctx.insert_message = False
        tree.ctx.delete_message = False
        tree.ctx.animate = True
        self.add(tree)

        arr = [1,2,3]
        vector = AlgoVector(self, arr)
        self.play(ShowCreation(vector))

        self.show_message("插入和删除操作会破坏红黑树的性质")
        self.show_message("维护这些性质是通过旋转来完成的")
        self.show_message("来看这3个节点的插入操作")

        self.play(vector.to_edge, UP)

        tree.shift(UP*2)
        index = 0
        
        for i in arr:
            self.play(FocusOn(vector.submobjects[index]), ApplyMethod(vector.submobjects[index].set_color, GREY))
            self.show_message("插入节点%d"%(i), delay=0.5)
            tree.set(i, i)
            index += 1

        self.show_message("节点3插入后，需要左旋节点1达到平衡", tex=True, tex_map={"左旋": BLUE, "3":RED, "1":RED})
        self.remove(tree, vector)

    def show_right(self):
        self.show_message("如果节点换成是[3, 2, 1]")
        arr = [3, 2, 1]

        vector = AlgoVector(self, arr)
        self.play(ShowCreation(vector))
        self.play(vector.to_edge, UP)

        tree = AlgoRBTree(self)
        tree.ctx.insert_message = False
        tree.ctx.delete_message = False
        tree.ctx.animate = True
        self.add(tree)
        tree.shift(UP*2)

        index = 0
        for i in arr:
            self.play(FocusOn(vector.submobjects[index]), ApplyMethod(vector.submobjects[index].set_color, GREY))
            self.show_message("插入节点%d"%(i), delay=0.5)
            tree.set(i, i)
            index += 1

        self.show_message("节点1插入后，需要右旋节点3达到平衡", tex=True, tex_map={"右旋": BLUE, "1":RED, "3":RED})

    def construct(self):
        self.start_logo(animate=False)
        self.init_message("红黑树的旋转")

        self.show_left()

        self.reset_speed_up()
        self.show_right()

        self.wait()

# 3 case
class RedBlackTreeInsert(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def rand(self, seed, animate_index, fadeout=True):
        tree = AlgoRBTree(self)
        
        tree.ctx.insert_message = False
        tree.ctx.delete_message = False
        tree.ctx.animate = False
        max_value = 100
        np.random.seed(seed)
        n = 8
        arr = np.random.choice(max_value, size=n, replace=False)
        print(arr)
        tree.shift(UP*2)
        index = 0
        for i in arr:
            if index >= animate_index:
                tree.ctx.insert_message = True
                tree.ctx.animate = True
                tree.update_nodes()
                self.add(tree)
                self.update_frame()
            tree.set(i, i)
            index += 1

        if fadeout:
            self.play(FadeOut(tree))
    
    def construct(self):
        self.start_logo(animate=False)
        self.init_message("红黑树插入的3个case",tex=True, tex_map={"case":RED})
        # left case 
        self.rand(5, 6, fadeout=True)

        # right case 1,2,3
        self.rand(3, 6, fadeout=False)

        self.wait()

# 4 case
class RedBlackTreeDelete(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def rand(self, seed, count, animate_index):
        print("--------------rand-------------", seed)
        tree = AlgoRBTree(self)
        self.add(tree)
        tree.ctx.insert_message = False
        tree.ctx.delete_message = False
        tree.ctx.animate = False
        max_value = 100
        np.random.seed(seed)
        n = count
        arr = np.random.choice(max_value, size=n, replace=False)
        print(arr)
        tree.shift(UP*2)
        index = 0

        for i in arr:
            tree.set(i, i)

        np.random.shuffle(arr)
        for i in arr:
            if index >= animate_index:
                tree.ctx.delete_message = True
                tree.ctx.animate = True
            tree.delete(i)
            index += 1

        self.play(FadeOut(tree))

    def construct(self):
        self.init_message("红黑树删除的4个case")
        # left case 1,2,3,4
        self.rand(560, 9, 3)

        # right case 1,2,3,4
        self.rand(18, 8, 2)
        
        self.wait()

def memory():
    import os
    import psutil
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
    return memoryUse

class RedBlackTreeEnd(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def rand(self, seed, count):
        tree = AlgoRBTree(self)
        self.add(tree)
        tree.ctx.insert_message = False
        tree.ctx.delete_message = False
        tree.ctx.animate = True
        tree.ctx.run_time = 0.5
        tree.ctx.wait_time = 0.5

        max_value = count*2
        np.random.seed(seed)
        n = count
        arr = np.random.choice(max_value, size=n, replace=False)
        print(arr)
        tree.shift(UP*2)
        index = 1

        for i in arr:
            if index == 82:
                print("hi")
            print("insert:", memory(), index, i)
            tree.set(i, i)
            index += 1

        np.random.shuffle(arr)
        index = 1
        for i in arr:
            print("delete:", index, i)
            tree.delete(i)
            index += 1

        self.play(FadeOut(tree))

    def construct(self):
        self.init_message("红黑树大型树结构变化")
        self.show_message("在最后，让我们创建一个20个节点的巨型树")
        self.show_message("便于我们更加直观的了解红黑树是如何运作的")
        self.camera.frame.shift(OUT*10)
        self.rand(1, 200)

        self.show_message("完成红黑树，谢谢观看！")
        self.wait()
