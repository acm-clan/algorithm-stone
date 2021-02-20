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

m = datamap.DataMap(get_leetcode_txt())
m.print()

def main():
    g = Digraph('stones')
    g.node(name='a',color='red')
    g.node(name='b',color='blue')
    g.edge('a','b',color='green')
    # g.view()

if __name__ == "__main__":
    # execute only if run as a script
    main()
    