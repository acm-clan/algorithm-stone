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
                s = Square(1).add(Text(str(self.data[i][j])))
                s.shift(DOWN*i + RIGHT*j)
                self.dim.add(s)
        self.dim.center()
        self.dim.shift(LEFT*3)
        self.add(self.dim)

    def find(self, i):
        print("find:", i, self.group[i])
        if self.group[i] != i:
            self.group[i] = self.find(self.group[i])
            print("find assign:", i, "->", self.group[i])
        return self.group[i]

    def union(self, group, i, j):
        gi = self.find(i)
        gj = self.find(j)
        self.group[gi] = self.group[gj]
        print("union:", gi, gj, "->", self.group[gi])
        self.graph.remove_edge(gi, gi)
        self.graph.add_edge(gi, gj)

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
        nodes = []
        edges = []
        for i in range(self.data.shape[0]):
            nodes.append(i)

        for i in range(self.data.shape[0]):
            for j in range(i, self.data.shape[1]):
                if self.data[i][j] == 1:
                    edges.append((i, j))

        graph = AlgoGraph(self, nodes, edges)
        graph.shift(RIGHT*2)
        self.graph = graph
        self.add(graph)

    def explain_union(self):
        # union is edge
        self.show_message("union是合并2个图，执行后只会有一个根节点，其中一个图根节点指向另外一个图的根节点")

    def explain_find(self):
        self.show_message("find是查找元素所在图的根节点")

    def construct(self):
        # self.init_message("并查集")
        # self.start_logo()
        self.create_area()
        # 从area创建网络
        self.create_network()
        # 从网络开始union
        for i in range(self.data.shape[0]):
            for j in range(i+1, self.data.shape[1]):
                if self.data[i][j] == 1:
                    self.union(self.group, i, j)

        self.wait()

    def old(self):
        persons = VGroup()
        for i in range(self.data.shape[0]):
            s = Square(1).add(Text(str(i)))
            persons.add(s)
        persons.arrange()
        self.add(persons)
        persons.shift(RIGHT*2)

        self.create_group()

        for i in range(self.data.shape[0]):
            for j in range(i+1, self.data.shape[1]):
                if self.data[i][j] == 1:
                    # i -> j
                    self.union(self.group, i, j)

        print("----------------------")
        c = 0
        for i in range(self.data.shape[0]):
            if self.group[i] == i:
                c+=1
            print(i, "->", self.find(i))
        
        print("group count:", c)

    def show_words(self):
        self.show_message("每个集合都是一个图结构")
        self.wait()
        self.show_message("显然有2个图")
        self.wait()
        self.show_message("如何从程序角度知道只有2个图？")
        self.wait()

        
        
