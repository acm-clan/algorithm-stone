from manimlib import *
import networkx as nx
from .algo_vgroup import *
from .algo_node import *

# tree的配置等信息
class AlgoTreeContext():
    def __init__(self):
        self.animate = True
        self.insert_message = True
        self.delete_message = True
        self.run_time = 0.8
        self.wait_time = 2

# 通用树节点
class AlgoTreeNode(object):
    def __init__(self, tree):
        # 节点唯一id
        self.id = tree.gen_id()
        # 显示在节点上的文本
        self.text = str(id)
        # 左右孩子
        self.left = None
        self.right = None
        self.color = WHITE

    def setText(self, t):
        self.text = t

# 通用树结构
class AlgoTree(AlgoVGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 每个节点有一个id
        self.tree_node_id = 0
        # 显示的对象
        self.node_objs = {}
        self.edge_objs = {}
        # tree的配置信息
        self.ctx = AlgoTreeContext()

    # 生成一个节点id
    def gen_id(self):
        self.tree_node_id = self.tree_node_id + 1
        return self.tree_node_id
    
    # 检查节点是否创建
    def check_node(self, p):
        if p.id not in self.node_objs:
            self.add_node(p)

    # 检查边是否创建
    def check_edge(self, x, y):
        if (x.id, y.id) not in self.edge_objs:
            self.add_edge(x, y)

    # 增加一个节点
    def add_node(self, z:AlgoTreeNode):
        if z.id in self.node_objs:
            return
        n = AlgoNode(str(z.text))

        n.set_color(z.color)
        self.node_objs[z.id] = n
        self.add(n)
        n.next_to(self)

    # 增加一条边
    def add_edge(self, n, t):
        if not n or not t:
            return
        arrow = Arrow(ORIGIN, ORIGIN, thickness=0.03, buff=1.25)
        arrow.set_color(GREY_BROWN)
        self.add(arrow)
        self.edge_objs[(n.id, t.id)] = arrow

    # 默认为二叉树
    def calc_tree_data(self):
        q = []
        q.append(self.root)
        nodes = []
        edges = []

        while len(q)>0:
            p = q.pop(0)
            nodes.append(AlgoTreeNode(p.id))

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

    # 通过graphviz计算节点位置
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

    # 获取节点的位置
    def get_node_pos(self, k):
        p = self.pos_infos[k]
        ratio = 60
        return [p[0]/ratio, p[1]/ratio, 0]

    # 获取节点
    def get_node(self, id):
        if id not in self.node_objs:
            return None
        return self.node_objs[id]

    # 获取边对象
    def get_edge(self, i, j):
        return self.edge_objs[(i, j)]

    # 更新操作，移动节点和边
    def move_nodes(self, nodes, edges):
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
    
    def update_tree(self):
        # 数据层
        nodes, edges = self.calc_tree_data()
        # layout
        self.calc_networkx(nodes, edges)
        # move nodes and edges
        self.move_nodes(nodes, edges)