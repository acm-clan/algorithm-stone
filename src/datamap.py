import zhon
from zhon import hanzi

legal_punctuation = [':', '-']

class Problem:
    def __init__(self, id, tags):
        self.id = id
        self.tags = tags

class DataMapNode:
    def __init__(self, name, problems, is_root, parent):
        self.name = name
        self.problems = problems
        self.is_root = is_root
        self.parent = parent
    
    def __repr__(self):
        return "%s %s" % (self.name, self.is_root)

    def __str__(self):
        return self.name

class DataMap:
    def __init__(self, data):
        self.data = data
        self.nodes = []
        self.last_root_name = ""
        self.problem_map = {}
        self.parse()

    def consume_blank(self, pos):
        length = len(self.data)
        while pos < length:
            c = self.data[pos]
            if c.strip():
                return pos
            pos += 1
        return pos

    def consume_key(self, pos):
        length = len(self.data)
        # pos = self.consume_blank(pos)
        t = ""
        while pos < length:
            c = self.data[pos]
            if c == ')':
                return t, pos
            if c.isalpha():
                t += c
            elif len(t)>0:
                return t, pos
            pos += 1

    def consume_value(self, pos):
        length = len(self.data)
        t = ""
        while pos < length:
            c = self.data[pos]
            if c.isalnum() or (c in hanzi.punctuation) or (c in legal_punctuation):
                t += c
            elif len(t) > 0:
                return t, pos
            pos += 1

    def consome_problem_tags(self, pos):
        tags = {}
        while True:
            key, pos = self.consume_key(pos)
            if key == "":
                break
            value, pos = self.consume_value(pos)
            tags[key] = value
        return pos, tags

    def consume_problems(self, pos, node):
        length = len(self.data)
        p = ""
        tags = {}

        while pos < length:
            c = self.data[pos]
            if c == '[':
                return pos
            elif c == '(':
                pos, tags = self.consome_problem_tags(pos)
            elif (c >= '0' and c <= '9') or c.isalpha():
                p += c
            elif len(p) > 0:
                pb = Problem(p, tags)
                node.problems.append(pb)
                self.problem_map[p] = pb
                p = ""
                tags = {}
            pos += 1
        return pos

    def consume_name(self, pos, node):
        length = len(self.data)
        state = 0
        name = ""
        while pos < length:
            c = self.data[pos]
            if c == '[':
                state = 1
            elif c == ']':
                node.name = name.strip()
                node.is_root = not node.name.startswith("-")
                if not node.is_root:
                    node.name = node.name[1:].strip()
                    node.parent = self.last_root_name
                else:
                    self.last_root_name = node.name
                return pos + 1
            elif state == 1:
                name += c
            pos += 1
        return -1

    def consume_node(self, pos):
        node = DataMapNode("", [], False, None)
        pos = self.consume_name(pos, node)
        if pos < 0:
            return pos
        
        # print("name:", node.name)

        pos = self.consume_problems(pos, node)
        if pos < 0:
            return pos
        if node.name != "未分类":
            self.nodes.append(node)
        return pos

    def parse(self):
        pos = 0
        while pos >= 0:
            pos = self.consume_node(pos)
        # print("parse finished:", self.nodes)


        