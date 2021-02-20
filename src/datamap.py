
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
        self.parse()

    def print(self):
        pass

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
                return pos + 1
            elif state == 1:
                name += c
            pos += 1
        return -1

    def consume_node(self, pos):
        node = DataMapNode("", [], False, None)
        pos = self.consume_name(pos, node)
        print("name:", node.name)
        if pos > 0:
            self.nodes.append(node)
        return pos

    def parse(self):
        pos = 0
        while pos >= 0:
            pos = self.consume_node(pos)
            print("consume node:", pos)
        print("parse finished:", self.nodes)


        