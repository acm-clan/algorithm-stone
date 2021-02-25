from graphviz import Digraph
import util
import os
from pathlib import Path
import datamap
import leetcode

def get_map(map_file):
    path = Path(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(path.parent.parent, "map", map_file))


def get_leetcode_map_txt(file):
    f = open(get_map(file), "r", encoding="utf-8")
    t = f.read()
    return t

def generate_leetcode(leet, file, slug, out_name):
    m = datamap.DataMap(get_leetcode_map_txt(file))
    g = Digraph('stones', encoding='utf-8')

    for n in m.nodes:
        if n.is_root:
            g.node(name=n.name, style='filled', target="_parent", href="https://leetcode-cn.com/tag/"+slug, fillcolor="orangered", color='lightgrey', fontcolor="white", fontname="Microsoft YaHei", shape='box')
        else:
            # 普通模块节点
            label = "%s(%s)" % (n.name, str(len(n.problems)))
            g.node(name=n.name, label=label, style='filled', fillcolor="lightslategray", color='lightgrey', fontcolor="white", fontname="Microsoft YaHei", shape='box')
            g.edge(n.parent, n.name)

        # add problem
        last = ""
        for p in n.problems:
            title = leet.get_title(p.id)
            level = leet.get_level(p.id)
            problem = leet.get_problem(p.id)
            idstr = str(p.id)
            title = idstr+". "+title
            color = "lightgrey"

            if level == "Easy":
                color = "greenyellow"
            elif level == "Medium":
                color = "orange"
            elif level == "Hard":
                color = "red"
            else:
                print("unknown level:", level)
            slug = problem['data']['question']['questionTitleSlug']

            # 题目节点
            is_finished = leet.check_finish(idstr)

            if is_finished:
                g.node(name=idstr, label=title, style='filled', fillcolor="lawngreen", target="_parent", href="https://leetcode-cn.com/problems/"+slug, 
                    color=color, fontname="Microsoft YaHei", shape='box')
            else:
                g.node(name=idstr, label=title, target="_parent", href="https://leetcode-cn.com/problems/"+slug, 
                    color=color, fontname="Microsoft YaHei", shape='box')

            if len(last) > 0:
                g.edge(last, idstr)
            else:
                g.edge(n.name, idstr)
            last = idstr

    g.format = 'svg'
    g.render(filename=util.get_images(out_name))
    os.remove(util.get_images(out_name))

def process_leetcode():
    leet = leetcode.Leetcode()
    leet.update_db()
    generate_leetcode(leet, "leetcode-dp.txt", "dynamic-programming", "leetcode_dp")
    generate_leetcode(leet, "leetcode-tree.txt", "tree", "leetcode_tree")
    leet.close_db()

def main():
    process_leetcode()

if __name__ == "__main__":
    main()
