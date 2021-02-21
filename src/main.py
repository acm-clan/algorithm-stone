from graphviz import Digraph
import os
from pathlib import Path
import datamap
import leetcode

def get_map(map_file):
    path = Path(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(path.parent.parent, "map", map_file))


def get_leetcode_txt():
    f = open(get_map("leetcode.txt"), "r", encoding="utf-8")
    t = f.read()
    return t


def main():
    leet = leetcode.Leetcode()
    leet.update_db()
    m = datamap.DataMap(get_leetcode_txt())
    g = Digraph('stones', encoding='utf-8')

    for n in m.nodes:
        g.node(name=n.name, color='lightgrey', fontname="Microsoft YaHei")
        if not n.is_root:
            g.edge(n.parent, n.name)

        # add problem
        last = ""
        for p in n.problems:
            title = leet.get_title(p)
            g.node(name=title, color='lightgrey', fontname="Microsoft YaHei")
            if len(last) > 0:
                g.edge(last, title)
            else:
                g.edge(n.name, title)
            last = title

    g.render()
    leet.close_db()
    # g.view()


if __name__ == "__main__":
    main()
