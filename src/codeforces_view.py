from graphviz import Digraph
import re
import theme
import util
import os
from pathlib import Path
import datamap
import codeforces
from svgpathtools import svg2paths
from bs4 import BeautifulSoup
import platform_view

class CodeforcesView(platform_view.PlatformView):
    def __init__(self, cf):
        self.cf = cf
        self.m = None

    def get_module_problem_count(self, m):
        c = 0
        for n in m.nodes:
            c += len(n.problems)
        return c

    def check_finish(self, title):
        return self.cf.check_finish(title)

    def get_problem(self, title):
        return self.m.problem_map[title]

    def check_flask(self, title):
        return self.cf.check_flask(title)

    def leetcode_add_finish_icon(self, path):
        c = util.get_file_content(path)
        b = BeautifulSoup(c, "xml")
        nodes = b.select("g.node")
        graph = b.select_one("g.graph")
        for n in nodes:
            title = n.title.get_text()
            if not re.match("[0-9]+[A-Za-z]+", title):
                continue
            self.post_process_problem_node(graph, n)
        content = b.prettify()
        util.save_file_content(path, content)

    def post_process(self, path):
        self.leetcode_add_finish_icon(path)

    def generate_codeforces(self, code, file, out_name):
        m = datamap.DataMap(util.get_file_content(util.get_map(file)))
        self.m = m
        g = Digraph('stones', encoding='utf-8')

        for n in m.nodes:
            if n.is_root:
                count = self.get_module_problem_count(m)
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
                href = "https://codeforces.com/problemset/problem/%d/%s" % (problem['contestId'], problem['index'])

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
        self.post_process(util.get_images(out_name)+".svg")

def process():
    cf = codeforces.Codeforces()
    cf.update_db()
    view = CodeforcesView(cf)
    view.generate_codeforces(cf, "codeforces.txt", "codeforces")
    cf.close_db()