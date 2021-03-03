from graphviz import Digraph
import time
import util
import os
from pathlib import Path
import datamap
import codeforces
import theme

def get_module_problem_count(m):
    c = 0
    for n in m.nodes:
        c += len(n.problems)
    return c

def generate_codeforces(code, file, out_name):
    m = datamap.DataMap(util.get_file_content(util.get_map(file)))
    g = Digraph('stones', encoding='utf-8')

    for n in m.nodes:
        if n.is_root:
            count = get_module_problem_count(m)
            label = "%s(%s)" % (n.name, str(count))
            # 根节点
            g.node(name=n.name, label=label, style='filled', target="_parent", href="https://codeforces.com/problemset", 
                fontsize='14',
                fillcolor="orangered", color='lightgrey', fontcolor="white", fontname="Microsoft YaHei", shape='box')
        else:
            # 普通模块节点
            label = "%s(%s)" % (n.name, str(len(n.problems)))
            g.node(name=n.name, label=label, style='filled', fillcolor="lightslategray", color='lightgrey', 
                fontsize='12',
                fontcolor="white", fontname="Microsoft YaHei", shape='box')
            g.edge(n.parent, n.name, color=theme.color_arrow)

        # add problem
        last = ""
        for p in n.problems:
            problem = code.get_db_problem(p.id)
            title = problem['name']
            level = code.get_level(problem)

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

            # 题目节点
            is_finished = code.check_finish(idstr)
            href = "https://codeforces.com/problemset/problem/%d/%s" % (problem['contestId'], problem['index'])

            if is_finished:
                g.node(name=idstr, label=title, style='filled', fillcolor="lawngreen", target="_parent", 
                    href=href, 
                    color=color, fontname="Microsoft YaHei", fontsize='12', shape='box')
            else:
                g.node(name=idstr, label=title, target="_parent", href=href, 
                    color=color, fontname="Microsoft YaHei", fontsize='12', shape='box')

            if len(last) > 0:
                g.edge(last, idstr, color=theme.color_arrow)
            else:
                g.edge(n.name, idstr, color=theme.color_arrow)
            last = idstr

    g.format = 'svg'
    g.render(filename=util.get_images(out_name))
    os.remove(util.get_images(out_name))

def process():
    c = codeforces.Codeforces()
    c.update_db()
    generate_codeforces(c, "codeforces.txt", "codeforces")
    c.close_db()