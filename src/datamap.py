
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
        self.parse()

    def consume_problems(self, pos, node):
        length = len(self.data)
        p = ""

        while pos < length:
            c = self.data[pos]
            if c == '[':
                return pos
            if c >= '0' and c <= '9':
                p += c
            elif c == '[':
                return pos
            elif len(p) > 0:
                # print("add problem:", p)
                node.problems.append(int(p))
                p = ""
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

        self.nodes.append(node)
        return pos

    def parse(self):
        pos = 0
        while pos >= 0:
            pos = self.consume_node(pos)
        # print("parse finished:", self.nodes)


        