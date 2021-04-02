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

    def create_group(self):
        groups = VGroup()
        for i in range(self.data.shape[0]):
            s = AlgoNode(str(i), is_circle=True)
            groups.add(s)
        groups.arrange()
        self.add(groups)
        groups.shift(RIGHT*2+UP*2)
        self.groups = groups

    def construct(self):
        # self.start_logo()
        self.create_area()
        # 从area创建网络

        # create person
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

        self.wait()

        
        
