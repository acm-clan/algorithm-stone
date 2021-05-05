from manim_imports_ext import *

# 547 省份数量

class UnionFind(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = np.array([
            [1,1,0,1],
            [1,1,0,0],
            [0,0,1,0],
            [1,0,0,1]
        ])
        self.group = []
        for i in range(self.data.shape[0]):
            self.group.append(i)

    def create_area(self):
        self.dim = VGroup()
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                s = Square(0.8, color=WHITE).add(AlgoText(str(self.data[i][j])))
                s.shift(DOWN*i + RIGHT*j)
                self.dim.add(s)
        self.dim.center()
        self.dim.shift(LEFT*3+UP)
        self.play(ShowCreation(self.dim))
        self.show_message("这是对称矩阵，有%d个市"%(self.data.shape[0]))

        for i in range(self.data.shape[0]):
            for j in range(i, self.data.shape[1]):
                obj = self.dim.submobjects[i*self.data.shape[0]+j]
                self.play(obj.set_color, BLUE, run_time=0.3)
        self.show_message("1表示连通，0表示不连通", delay=4)

        obj = self.dim.submobjects[0*self.data.shape[0]+1]
        # self.play(obj.set_color, RED, run_time=0.3)
        self.show_message("比如[0][1]为1表示城市0和1之间连通")
        self.play(FocusOn(obj, color=RED))
        self.play(Indicate(obj))
        self.wait()

    def find(self, i):
        if self.group[i] != i:
            self.group[i] = self.find(self.group[i])
        return self.group[i]

    def union(self, group, i, j):
        gi = self.find(i)
        gj = self.find(j)

        obj = self.dim.submobjects[i*self.data.shape[0]+j]
        self.play(obj.set_color, RED, run_time=0.3)

        self.group[gi] = self.group[gj]
        self.show_message("%d和%d连通"%(i, j))
        self.show_message("%d的根节点为%d，%d的根节点%d"%(i, gi, j, gj))
        self.show_message("根节点%d指向根节点%d"%(gi, gj))
        self.graph.remove_edge(gi, gi)

        n = self.graph.get_node(gi)
        self.play(n.set_color, WHITE, run_time=0.5)

        self.graph.add_edge(gi, gj)
        self.show_message("%d和%d合并在一个图中，根节点有且只有一个%d"%(i, j, gj), delay=3)

    def create_group(self):
        groups = VGroup()
        for i in range(self.data.shape[0]):
            s = AlgoNode(str(i), is_circle=True)
            groups.add(s)
        groups.arrange()
        self.add(groups)
        groups.shift(RIGHT*2+UP*2)
        self.groups = groups

    def create_network(self):
        self.show_message("通过对称矩阵我们可以得到图", 2)
        nodes = []
        edges = []
        for i in range(self.data.shape[0]):
            nodes.append(i)

        for i in range(self.data.shape[0]):
            for j in range(i, self.data.shape[1]):
                if self.data[i][j] == 1:
                    edges.append((i, j))

        graph = AlgoGraph(self, nodes, edges)
        graph.shift(RIGHT*2+UP)
        self.graph = graph
        self.play(ShowCreation(graph))

        for i in range(self.data.shape[0]):
            n = self.graph.get_node(i)
            self.play(n.set_color, GREEN, run_time=0.1)

        for i in range(self.data.shape[0]):
            for j in range(i+1, self.data.shape[1]):
                if self.data[i][j] == 1:
                    graph.remove_edge(i, j)
                    
        self.show_message("每个节点初始状态都指向自己", 2)

    def construct(self):
        self.add_sound("bg002")
        self.start_logo()
        m = self.init_message("并查集")
        leet = AlgoText("LeetCode 547.省份数量", color=GOLD_E).center().to_edge(UP).shift(UP*0.2)
        self.play(ShowCreation(leet))
        
        self.create_area()
        # 从area创建网络
        self.create_network()
        # 从网络开始union
        for i in range(self.data.shape[0]):
            for j in range(i+1, self.data.shape[1]):
                if self.data[i][j] == 1:
                    self.union(self.group, i, j)

        # 遍历每个元素
        c = 0
        for i in range(self.data.shape[0]):
            if self.group[i] == i:
                c += 1
        
        self.show_message("遍历，根节点指向自己的节点数量为%d"%(c))
        self.show_message("完成并查集，谢谢观看！")

        self.wait()
