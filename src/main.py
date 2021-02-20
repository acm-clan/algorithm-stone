from graphviz import Digraph
import os
from pathlib import Path
import datamap


def get_map(map_file):
    path = Path(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(path.parent.parent, "map", map_file))


def get_leetcode_txt():
    f = open(get_map("leetcode.txt"), "r", encoding="utf-8")
    t = f.read()
    return t


def main():
    m = datamap.DataMap(get_leetcode_txt())
    g = Digraph('stones', encoding='utf-8')

    for n in m.nodes:
        g.node(name=n.name, color='lightgrey', fontname="Microsoft YaHei")
        if not n.is_root:
            g.edge(n.parent, n.name)

        # add problem
        last = ""
        for p in n.problems:
            g.node(name=str(p), color='lightgrey', fontname="Microsoft YaHei")
            if len(last) > 0:
                g.edge(last, str(p))
            else:
                g.edge(n.name, str(p))
            last = str(p)

    g.render()
    # g.view()


if __name__ == "__main__":
    main()
