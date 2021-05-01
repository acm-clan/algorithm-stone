from manimlib import *
import copy
import networkx as nx
from .algo_vgroup import *
from .algo_node import *
import queue

COLOR_TARGET_INSERT = GREEN_D
COLOR_TARGET_DELETE = RED_D
COLOR_PARENT = YELLOW_D
COLOR_UNCLE = BLUE
COLOR_GRAND = PURPLE
COLOR_BROTHER = TEAL

class DataNode(object):
    def __init__(self, id, k, v, raw):
        self.id = id
        self.k = k
        self.v = v
        self.raw = raw

class AlgoRBTreeNode(object):
    def __init__(self, t, scene, id, k, v, color):
        self.id = id
        self.tree = t
        self.k = k
        self.v = v
        self.scene = scene
        self.color = color
        self.p = t.nil()
        self.left = t.nil()
        self.right = t.nil()

    def addChild(self, t, z):
        y = self
        if y.isNil():
            t.root = z
        elif z.k < y.k:
            y.left = z
        else:
            y.right = z

    def isNil(self):
        return self.k < 0

    def isNotNil(self):
        return not self.isNil()

    def isLeaf(self):
        return self.left.isNil() and self.right.isNil()
    
    def isLeft(self):
        return self == self.p.left

    def isRight(self):
        return self == self.p.right

    def brother(self):
        if self.isLeft():
            return self.p.right
        else:
            return self.p.left

    def replaceChild(self, t, u, v):
        if u == self.left:
            self.left = v
            self.setLeft(t, v)
        else:
            self.right = v
            self.setRight(t, v)
        v.p = self
        v.setParent(t, self)

    def setLeft(self, t, x):
        self.left = x
        t.add_edge(self, x)
    
    def setRight(self, t, x):
        self.right = x
        t.add_edge(self, x)
    
    def setParent(self, t, x):
        self.p = x
        t.add_edge(self.p, self)

    def setColor(self, c):
        if self.color == c:
            return
        self.color = c
        n = self.tree.get_node(self.id)
        if n:
            if self.tree.ctx.animate:
                self.scene.play(FocusOn(n), run_time=1)
                self.scene.play(ApplyMethod(n.set_color, c))
            else:
                n.set_color(c)

class AlgoRBTreeContext():
    def __init__(self):
        self.animate = True
        self.insert_message = True
        self.delete_message = True
        self.run_time = 0.8
        self.wait_time = 2

class AlgoRBTree(AlgoVGroup):
    def __init__(self, scene, **kwargs):
        self.edge_objs = {}
        self.node_objs = {}
        self.ctx = AlgoRBTreeContext()

        self.scene = scene
        
        self.edges = []
        self.nodes = []
        
        super().__init__(**kwargs)

        self.node_id = 0
        self.raw_nil = None
        self.raw_nil = AlgoRBTreeNode(self, scene, 0, -1, 0, BLACK)
        self.root = self.nil()
        # self.add_node(nil)
        self.center()

    def nil(self):
        id = self.get_node_id()
        if self.raw_nil == None:
            return None
        n = copy.copy(self.raw_nil)
        n.id = id
        return n

    def insert(self, z):
        y = self.nil()
        x = self.root
        while x.isNotNil():
            y = x
            if z.k < x.k:
                x = x.left
            else:
                x = x.right
        z.p = y
        y.addChild(self, z)

        self.add_node(z)

        self.scene.show_message("插入元素%d"%(z.k), animate=self.ctx.insert_message)

        self.update_nodes()

        self.insertFixup(z)
        self.update_nodes()

    def surround_node(self, id, color=GREEN):
        if self.ctx.animate:
            node = self.get_node(id)
            rect = SurroundingRectangle(node, color=color)
            def update_rect(node):
                rect.move_to(node)
            node.add_updater(update_rect)
            node.rect = rect
            rect.node = node
            self.scene.play(Write(rect), run_time=0.5)
            return rect
        return None

    def fadeout_rect(self, rect):
        if self.ctx.animate and rect != None:
            node = rect.node
            node.rect = None
            self.scene.play(FadeOut(rect), run_time=0.3)
    
    def insertFixup(self, z:AlgoRBTreeNode):
        raw_z = z
        while z.p.color == RED:
            rect_z = self.surround_node(z.id, color=COLOR_TARGET_INSERT)
            if z.p.isLeft():
                self.scene.show_message("父节点在左边", animate=self.ctx.insert_message)
                y = z.p.brother()
                if y.color == RED:
                    rect_y = self.surround_node(y.id, color=COLOR_UNCLE)
                    print("insert left case 1")
                    self.scene.show_message("插入%d case 1：叔叔节点存在并且为红色（无需旋转）"%(raw_z.k), animate=self.ctx.insert_message)
                    z.p.setColor(BLACK)
                    y.setColor(BLACK)
                    z.p.p.setColor(RED)
                    z = z.p.p
                    self.update_nodes()
                    self.fadeout_rect(rect_y)
                else:
                    if z.isRight():
                        print("insert left case 2")
                        self.scene.show_message("插入%d case 2：新节点在右边，左旋新节点再执行case 3"%(raw_z.k), animate=self.ctx.insert_message)
                        z = z.p
                        self.leftRotate(z)
                        self.update_nodes()
                    print("insert left case 3")
                    rect_p = self.surround_node(z.p.p.id, color=COLOR_GRAND)
                    self.scene.show_message("插入%d case 3：右旋祖父节点%d"%(raw_z.k, z.p.p.k), animate=self.ctx.insert_message)
                    z.p.setColor(BLACK)
                    z.p.p.setColor(RED)
                    self.rightRotate(z.p.p)
                    self.update_nodes()
                    self.fadeout_rect(rect_p)
            else:
                self.scene.show_message("父节点在右边", animate=self.ctx.insert_message)
                y = z.p.brother()
                if y.color == RED:
                    rect_y = self.surround_node(y.id, color=COLOR_UNCLE)
                    print("insert right case 1")
                    self.scene.show_message("插入%d case 1：叔叔节点存在并且为红色（无需旋转）"%(raw_z.k), animate=self.ctx.insert_message)
                    z.p.setColor(BLACK)
                    y.setColor(BLACK)
                    z.p.p.setColor(RED)
                    z = z.p.p
                    self.update_nodes()
                    self.fadeout_rect(rect_y)
                else:
                    if z.isLeft():
                        print("insert right case 2")
                        self.scene.show_message("插入%d case 2：新节点在左边，右旋再执行case 3"%(raw_z.k), animate=self.ctx.insert_message)
                        z = z.p
                        self.rightRotate(z)
                        self.update_nodes()
                    print("insert right case 3")
                    rect_p = self.surround_node(z.p.p.id, color=COLOR_GRAND)
                    self.scene.show_message("插入%d case 3：左旋祖父节点%d"%(raw_z.k, z.p.p.k), animate=self.ctx.insert_message)
                    z.p.setColor(BLACK)
                    z.p.p.setColor(RED)
                    self.leftRotate(z.p.p)
                    self.update_nodes() 
                    self.fadeout_rect(rect_p)
            self.fadeout_rect(rect_z)
        self.root.setColor(BLACK)

    def dumpInternal(self, n, d):
        if (not n):
            return
        for _ in range(d):
            print("--", end='')
        print("%d(%d %d)"%(n.k, n.k, n.v))
        self.dumpInternal(n.left, d + 1)
        self.dumpInternal(n.right, d + 1)

    def dump(self, n):
        self.dumpInternal(n, 1)

    def leftRotate(self, x):
        y = x.right
        # x.right = y.left
        x.setRight(self, y.left)

        if y.left.isNotNil():
            # y.left.p = x
            y.left.setParent(self, x)
        # y.p = x.p
        y.setParent(self, x.p)
        self.transplant(x, y)
        # y.left = x
        y.setLeft(self, x)
        # x.p = y
        x.setParent(self, y)

    def rightRotate(self, x):
        y = x.left
        # x.left = y.right
        x.setLeft(self, y.right)
        if y.right.isNotNil():
            # y.right.p = x
            y.right.setParent(self, x)
        # y.p = x.p
        y.setParent(self, x.p)
        self.transplant(x, y)
        # y.right = x
        y.setRight(self, x)
        # x.p = y
        x.setParent(self, y)

    def transplant(self, u, v):
        if u.p.isNil():
            self.root = v
            self.root.setParent(self, self.nil())
        else:
            u.p.replaceChild(self, u, v)

    def calc_networkx(self, nodes, edges):
        self.g = nx.Graph()
        for k in nodes:
            self.g.add_node(k.id)
        for k in edges:
            self.g.add_edge(*k)
        self.pos_infos = nx.nx_agraph.graphviz_layout(self.g, prog='dot', args='-Grankdir="TB"')
        points = self.pos_infos
        x = [points[k][0] for k in points]
        y = [points[k][1] for k in points]
        c = (sum(x) / len(points), sum(y) / len(points))
        for k in self.pos_infos:
            self.pos_infos[k] = np.array(self.pos_infos[k])-np.array(c)

        return self.pos_infos

    def calc_tree_data(self, root):
        q = []
        q.append(root)
        nodes = []
        edges = []

        while len(q)>0:
            p = q.pop(0)
            nodes.append(DataNode(p.id, p.k, p.v, p))

            if p.left:
                self.check_node(p.left)
                self.check_edge(p, p.left)
                edges.append((p.id, p.left.id))
                q.append(p.left)
            if p.right:
                self.check_node(p.right)
                self.check_edge(p, p.right)
                edges.append((p.id, p.right.id))
                q.append(p.right)

        return nodes, edges

    def check_edge(self, x, y):
        if (x.id, y.id) not in self.edge_objs:
            self.add_edge(x, y)

    def update_nodes(self):
        if not self.ctx.animate:
            return
        # 数据层
        nodes, edges = self.calc_tree_data(self.root)
        # layout
        pos_infos = self.calc_networkx(nodes, edges)
        # 
        self.move_nodes(pos_infos, nodes, edges)
        # 构造树

    def move_nodes(self, pos_infos, nodes, edges):
        self.nodes = nodes
        self.edges = edges

        # remove unused nodes
        keys = list(self.node_objs.keys())
        for k in keys:
            if k not in [x.id for x in self.nodes]:
                o = self.node_objs[k]
                self.remove(o)
                self.scene.remove(o)
                del self.node_objs[k]

        node_animations = []
        for k in self.nodes:
            n = self.get_node(k.id)
            p = self.get_node_pos(k.id)
            n.set_color(k.raw.color)
            if self.ctx.animate:
                node_animations.append(ApplyMethod(n.move_to, p, run_time=self.ctx.run_time))
                if hasattr(n, "rect") and n.rect != None:
                    node_animations.append(ApplyMethod(n.rect.move_to, p, run_time=self.ctx.run_time))
            else:
                node_animations.append(ApplyMethod(n.move_to, p, run_time=0.01))
                if hasattr(n, "rect") and  n.rect != None:
                    node_animations.append(ApplyMethod(n.rect.move_to, p, run_time=0.01))

        # remove edges
        keys = list(self.edge_objs.keys())
        for k in keys:
            if k not in self.edges:
                e = self.edge_objs[k]
                self.remove(e)
                self.scene.remove(e)
                del self.edge_objs[k]

        animations = []
        for k in self.edges:
            e = self.get_edge(*k)
            p1 = np.array(self.get_node_pos(k[0]))+DOWN*0.25
            p2 = np.array(self.get_node_pos(k[1]))+UP*0.25

            if self.ctx.animate:
                animations.append(ApplyMethod(e.put_start_and_end_on, p1, p2, run_time=self.ctx.run_time))
            else:
                animations.append(ApplyMethod(e.put_start_and_end_on, p1, p2, run_time=0.01))

        self.scene.play(*node_animations, *animations)

        if self.ctx.animate:
            self.scene.wait(self.ctx.wait_time)

    def set(self, k, v):
        if self.root.isNil():
            self.scene.show_message("插入元素%d"%(k), animate=self.ctx.insert_message, delay=0)
            z = AlgoRBTreeNode(self, self.scene, self.get_node_id(), k, v, BLACK)
            self.root = z
            self.add_node(z)
            self.update_nodes()
        else:
            z = AlgoRBTreeNode(self, self.scene, self.get_node_id(), k, v, RED)
            self.insert(z)
      
    def add_node(self, z):
        if z.id in self.node_objs:
            return
        n = AlgoNode(str(z.k))
        
        if z.isNil():
            n.scale(0.5)
            tri = Triangle().scale(0.2)
            n.add(tri)
            tri.center()
            n.outline_obj.scale(0)
            n.text_obj.scale(0)

        n.set_color(RED)
        self.node_objs[z.id] = n
        self.add(n)
        n.next_to(self)
        # add edges
        self.add_edge(z.p, z)
        self.add_edge(z, z.left)
        self.add_edge(z, z.right)
    
    def add_edge(self, n, t):
        if not n or not t:
            return
        a = Arrow(ORIGIN, ORIGIN, thickness=0.03, buff=1.25)
        a.set_color(GREY)
        self.add(a)
        self.edge_objs[(n.id, t.id)] = a

    def get_node(self, id):
        if id not in self.node_objs:
            return None
        return self.node_objs[id]

    def get_nil_nodes(self):
        n = []
        for k in self.nodes:
             if k.k == -1:
                 n.append(self.get_node(k.id))
        return n

    def get_edge(self, i, j):
        return self.edge_objs[(i, j)]

    def getInternal(self, n, k):
        if not n or n.isNil():
            return None
        if n.k == k:
            return n
        if k < n.k:
            return self.getInternal(n.left, k)
        return self.getInternal(n.right, k)

    def treeMinimum(self, x):
        p = x
        while p.left.isNotNil():
            p = p.left
        return p

    def deleteInternal(self, z):
        self.scene.show_message("删除节点%d"%(z.k), animate=self.ctx.delete_message)
        y = z
        value = z.k
        origin_color = y.color
        x = None

        if (z.left.isNil()):
            x = z.right
            self.transplant(z, z.right)
        elif (z.right.isNil()):
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.treeMinimum(z.right)
            origin_color = y.color
            x = y.right
            if (y.p == z):
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        
        self.update_nodes()

        if (origin_color == BLACK):
            self.deleteFixUp(x, value)

    def deleteFixUp(self, x, value):
        while (x != self.root and x.color == BLACK):
            rect_x = self.surround_node(x.id, color=COLOR_TARGET_DELETE)
            if (x.isLeft()):
                w = x.brother()
                if (w.color == RED):
                    rect_x1 = self.surround_node(w.id, color=COLOR_BROTHER)
                    rect_p = self.surround_node(x.p.id, color=COLOR_PARENT)
                    print("delete left case 1")
                    self.scene.show_message("删除%d case 1：兄弟节点是红色，左旋父节点%d"%(value, x.p.k), animate=self.ctx.delete_message)
                    w.setColor(BLACK)
                    x.p.setColor(RED)
                    self.leftRotate(x.p)
                    w = x.p.right
                    self.update_nodes()
                    self.fadeout_rect(rect_x1)
                    self.fadeout_rect(rect_p)
                if (w.left.color == BLACK and w.right.color == BLACK):
                    print("delete left case 2")
                    rect_w = self.surround_node(w.id, color=COLOR_BROTHER)
                    self.scene.show_message("删除%d case 2：兄弟节点的子节点都是黑色"%(value), animate=self.ctx.delete_message)
                    w.setColor(RED)
                    x = x.p
                    self.fadeout_rect(rect_w)
                else:
                    if (w.right.color == BLACK):
                        rect_w = self.surround_node(w.id, color=COLOR_BROTHER)
                        print("delete left case 3")
                        self.scene.show_message("删除%d case 3：兄弟节点的右孩子为黑色，右旋兄弟节点"%(value), animate=self.ctx.delete_message)
                        w.left.setColor(BLACK)
                        w.setColor(RED)
                        self.rightRotate(w)
                        w = x.p.right
                        self.update_nodes()
                        self.fadeout_rect(rect_w)

                    print("delete left case 4")
                    rect_p = self.surround_node(x.p.id, color=COLOR_PARENT)
                    self.scene.show_message("删除%d case 4：左旋父节点"%(value), animate=self.ctx.delete_message)
                    w.color = x.p.color
                    x.p.setColor(BLACK)
                    w.right.setColor(BLACK)
                    self.leftRotate(x.p)
                    x = self.root
                    self.update_nodes()
                    self.fadeout_rect(rect_p)
            else:
                w = x.p.left
                if (w.color == RED):
                    rect_x1 = self.surround_node(w.id, color=COLOR_BROTHER)
                    rect_p = self.surround_node(x.p.id, color=COLOR_PARENT)
                    print("delete right case 1")
                    self.scene.show_message("删除%d case 1：兄弟节点是红色，右旋父节点%d"%(value, x.p.k), animate=self.ctx.delete_message)
                    w.setColor(BLACK)
                    x.p.setColor(RED)
                    self.rightRotate(x.p)
                    w = x.p.left
                    self.update_nodes()
                    self.fadeout_rect(rect_x1)
                    self.fadeout_rect(rect_p)
                if (w.right.color == BLACK and w.left.color == BLACK):
                    print("delete right case 2")
                    rect_w = self.surround_node(w.id, color=COLOR_BROTHER)
                    self.scene.show_message("删除%d case 2：兄弟节点的子节点都是黑色，设置父节点为红色"%(value), animate=self.ctx.delete_message)
                    w.setColor(RED)
                    x = x.p
                    self.update_nodes()
                    self.fadeout_rect(rect_w)
                else:
                    if (w.left.color == BLACK):
                        rect_w = self.surround_node(w.id, color=COLOR_BROTHER)
                        print("delete right case 3")
                        self.scene.show_message("删除%d case 3：兄弟节点的左孩子为黑色，右旋兄弟节点"%(value), animate=self.ctx.delete_message)
                        w.right.setColor(BLACK)
                        w.setColor(RED)
                        self.leftRotate(w)
                        w = x.p.left
                        self.update_nodes()
                        self.fadeout_rect(rect_w)
                    print("delete right case 4")
                    rect_p = self.surround_node(x.p.id, color=COLOR_PARENT)
                    self.scene.show_message("删除%d case 4：右旋父节点"%(value), animate=self.ctx.delete_message)
                    w.color = x.p.color
                    x.p.setColor(BLACK)
                    w.left.setColor(BLACK)
                    self.rightRotate(x.p)
                    x = self.root
                    self.update_nodes()
                    self.fadeout_rect(rect_p)
            self.fadeout_rect(rect_x)
        x.setColor(BLACK)

    def delete(self, k):
        # print("remove ", k)
        z = self.getInternal(self.root, k)
        if z:
            self.deleteInternal(z)

    def get_node_id(self):
        self.node_id += 1
        return self.node_id

    def check_node(self, p):
        if p.id not in self.node_objs:
            self.add_node(p)

    def hide_all(self):
        for k in self.node_objs:
            self.remove(self.node_objs[k])

        for k in self.edge_objs:
            self.remove(self.edge_objs[k])

    def show_node(self, id):
        n = self.get_node(id)
        self.scene.play(FadeIn(n))

    def show_edge(self, i, j):
        a = self.edge_objs[(i, j)]
        self.scene.play(FadeIn(a))

    def get_node_pos(self, k):
        p = self.pos_infos[k]
        ratio = 60
        return [p[0]/ratio, p[1]/ratio, 0]
