from manim_imports_ext import *
import io

# 动画红黑树，旋转的艺术

class RBScene(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_colors(self, direction=UL):
        v = VGroup()
        scale = 0.15
        tscale = 0.6

        target = Square(color=COLOR_GRAND).scale(scale)
        text = AlgoText("祖父节点").scale(tscale).next_to(target)
        v.add(VGroup(*[target, text]))

        target = Square(color=COLOR_UNCLE).scale(scale)
        text = AlgoText("叔叔节点").scale(tscale).next_to(target)
        v.add(VGroup(*[target, text]))

        target = Square(color=COLOR_PARENT).scale(scale)
        text = AlgoText("父节点").scale(tscale).next_to(target)
        v.add(VGroup(*[target, text]))

        target = Square(color=COLOR_BROTHER).scale(scale)
        text = AlgoText("兄弟节点").scale(tscale).next_to(target)
        v.add(VGroup(*[target, text]))

        target = Square(color=COLOR_TARGET_DELETE).scale(scale)
        text = AlgoText("目标节点（删除）").scale(tscale).next_to(target)
        v.add(VGroup(*[target, text]))

        target = Square(color=COLOR_TARGET_INSERT).scale(scale)
        text = AlgoText("目标节点（插入）").scale(tscale).next_to(target)
        v.add(VGroup(*[target, text]))

        v.arrange(direction=UP, aligned_edge=LEFT, buff=0.1)

        v.to_edge(edge=direction)
        self.update_frame()
        v.fix_in_frame()
        self.add(v)

class RedBlackTreePreface(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        # self.start_logo(subtitle="红黑树")
        self.wait(100)

class RedBlackTreeWhatIs(RBScene):
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
        self.start_logo(subtitle="红黑树", tex=True, tex_map={"红":RED_D})
        self.init_message("红黑树的性质", tex=True, tex_map={"红":RED_D})
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

        self.show_message("红黑树是一种二叉查找树", tex=True, tex_map={"红":RED_D})
        root = tree.get_node(tree.root.id)
        left = tree.get_node(tree.root.left.id)
        right = tree.get_node(tree.root.right.id)

        self.show_message("左孩子的值小于根节点", tex=True, tex_map={"左孩子":BLUE_D, "根节点":BLUE_D})
        self.compare_nodes(left, root, "<")

        self.show_message("右孩子的值大于根节点", tex=True, tex_map={"右孩子":BLUE_D, "根节点":BLUE_D})
        self.compare_nodes(right, root, ">")
        
        self.show_message("任意节点左右子树分别为二叉查找树", tex=True, tex_map={"二叉查找树":BLUE_D})
        self.hide_and_show(tree, root)

        self.show_message("红黑树有5条性质", tex=True, tex_map={"红":RED_D, "5": BLUE_D})

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

        self.show_message("1 每个节点是红色或者黑色，包括叶子nil节点", tex=True, tex_map={"红色":RED_D, "黑色": GREY_E, "nil": BLUE_D})
        panel.light(0, color="#93582e")
        
        self.show_message("2 根节点是黑色", tex=True, tex_map={"黑色":GREY_E, "根节点":BLUE_D})
        root_node = tree.get_node(tree.root.id)
        self.play(ApplyWave(root_node), CircleIndicate(root_node, color=RED, run_time=2))
        panel.light(1, color="#93582e")

        self.show_message("3 叶子nil节点是黑色", tex=True, tex_map={"黑色":GREY_E, "nil":BLUE_D})
        self.indicate_nils(tree)
        panel.light(2, color="#93582e")
        
        self.show_message("4 如果一个节点是红色，则其子节点都是黑色", tex=True, tex_map={"红色":RED_D, "黑色":GREY_E})
        n = tree.root.right
        l = n.left
        r = n.right
        self.indicate_nodes(tree, [tree.get_node(n.id), tree.get_node(l.id), tree.get_node(r.id)])
        panel.light(3, color="#93582e")

        self.reset_speed_up()
        self.show_message("5 任意节点到叶子节点的所有路径上，黑色节点数量相同", tex=True, tex_map={"路径":BLUE_D, "黑色节点数量":BLUE_D})
        self.show_message("如上树中根节点到所有叶子节点的黑色节点数量都是3", tex=True, tex_map={"根节点":BLUE_D, "3":BLUE_D, "叶子节点":BLUE_D})
        panel.light(4, color="#93582e")
        
        self.wait()

class RedBlackTreeRotate(RBScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_left(self):
        tree = AlgoRBTree(self)
        tree.ctx.insert_message = True
        tree.ctx.delete_message = True
        tree.ctx.animate = True
        self.add(tree)

        arr = [1,2,3]
        vector = AlgoVector(self, arr)
        self.play(ShowCreation(vector))

        self.show_message("插入和删除操作会破坏红黑树的性质", tex=True, tex_map={"红":RED_D})
        self.show_message("维护这些性质是通过旋转来完成的", tex=True, tex_map={"旋转":BLUE_D})
        self.show_message("来看这3个节点的插入操作", tex=True, tex_map={"3":BLUE_D})

        self.play(vector.to_edge, UP)

        tree.shift(UP*2)
        index = 0
        
        for i in arr:
            self.play(FocusOn(vector.submobjects[index]), ApplyMethod(vector.submobjects[index].set_color, GREY), run_time=1)
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
        tree.ctx.insert_message = True
        tree.ctx.delete_message = True
        tree.ctx.animate = True
        self.add(tree)
        tree.shift(UP*2)

        index = 0
        for i in arr:
            self.play(FocusOn(vector.submobjects[index]), ApplyMethod(vector.submobjects[index].set_color, GREY), run_time=0.5)
            tree.set(i, i)
            index += 1

        self.show_message("节点1插入后，需要右旋节点3达到平衡", tex=True, tex_map={"右旋": BLUE, "1":RED, "3":RED})

    def construct(self):
        self.start_logo(animate=False)
        # self.show_colors()
        self.init_message("红黑树的旋转", tex=True, tex_map={"红": RED_D})

        self.show_left()

        self.reset_speed_up()
        self.show_right()

        self.wait()

# 3 case
class RedBlackTreeInsert(RBScene):
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
        self.init_message("红黑树插入的3个case",tex=True, tex_map={"case":RED_D, "3":RED})
        # left case 
        self.show_message("节点在左边的情况",tex=True, tex_map={"左边":BLUE_D})
        self.show_colors()
        self.rand(5, 6, fadeout=True)

        # right case 1,2,3
        self.show_message("节点在右边的情况",tex=True, tex_map={"右边":BLUE_D})
        self.rand(3, 6, fadeout=False)

        self.wait()

# 4 case
class RedBlackTreeDelete(RBScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def rand(self, seed, count, animate_index, max):
        tree = AlgoRBTree(self)
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

        sub_arr = arr[animate_index:animate_index+max]
        vector = AlgoVector(self, sub_arr).to_edge(UL, buff=LARGE_BUFF)
        self.add(vector)

        c = 0
        for i in arr:
            if index >= animate_index:
                tree.ctx.delete_message = True
                tree.ctx.animate = True
                tree.update_nodes()
                self.add(tree)
                self.update_frame()
                self.play(ApplyMethod(vector.submobjects[c].set_color, GREY), run_time=0.8)
                vector.submobjects[c].add(AlgoExmark().scale(1).move_to(vector.submobjects[c].get_center()))
                c += 1
            tree.delete(i)
            index += 1
            if c == max:
                break

        self.wait(2)
        self.play(FadeOut(tree), FadeOut(vector))
        self.wait()

    def construct(self):
        self.start_logo(animate=False)
        self.init_message("红黑树删除的4个case", tex=True, tex_map={"4":RED, "case":RED})
        # left case 1,2,3,4
        self.show_message("节点在左边的情况",tex=True, tex_map={"左边":BLUE_D})
        self.show_colors(direction=UR)
        self.rand(560, 9, 3, 3)

        # right case 1,2,3,4
        self.show_message("节点在右边的情况",tex=True, tex_map={"右边":BLUE_D})
        self.rand(18, 8, 2, 3)
        
        self.wait()

def memory():
    import os
    import psutil
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
    return memoryUse



class RedBlackTreeEnd(RBScene):
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

        self.show_message("插入元素")
        for i in arr:
            if index == 82:
                print("hi")
            print("insert:", memory(), index, i)
            tree.set(i, i)
            index += 1

        np.random.shuffle(arr)
        index = 1
        self.show_message("删除元素")
        for i in arr:
            print("delete:", index, i)
            tree.delete(i)
            index += 1

        self.play(FadeOut(tree))

    def construct(self):
        self.start_logo(animate=False)
        self.init_message("红黑树完整示例", tex=True, tex_map={"红": RED_D})

        count = 10
        self.show_message("在最后，让我们创建一个%d个节点的树"%(count), tex=True, tex_map={str(count):RED})
        self.show_message("便于我们更加直观的了解红黑树是如何运作的", tex=True, tex_map={"红": RED_D})
        self.camera.frame.shift(OUT*10)

        self.reset_speed_up()
        self.show_colors()
        self.rand(1, count)

        self.show_message("完成红黑树，谢谢观看！", tex=True, tex_map={"红":RED})
        self.wait()
