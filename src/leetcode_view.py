from graphviz import Digraph
import theme
import util
import os
from pathlib import Path
import datamap
import leetcode
from svgpathtools import svg2paths
from bs4 import BeautifulSoup
import platform_view

class LeetcodeView(platform_view.PlatformView):
    def __init__(self, leet):
        self.leet = leet
        self.m = None
        self.slug = "leetcode"

    def check_finish(self, title):
        return self.leet.check_finish(title)

    def get_problem(self, title):
        return self.m.problem_map[title]

    def check_flask(self, title):
        return self.leet.check_flask(title)

    def is_valid_title(self, title):
        return title.isdigit()

    def post_process(self, path):
        self.add_finish_icon(path)

    def generate_leetcode(self, leet, file, slug, out_name):
        c = util.get_file_content(util.get_map(file))
        m = datamap.DataMap(c)
        self.m = m
        g = Digraph('stones', encoding='utf-8')

        for n in m.nodes:
            if n.is_root:
                count = self.get_module_problem_count(m)
                label = "%s(%s)" % (n.name, str(count))
                # 根节点
                g.node(name=n.name, label=label, style='filled', target="_parent", href="https://leetcode-cn.com/tag/"+slug, 
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
                title = leet.get_title(p.id)
                level = leet.get_level(p.id)
                problem = leet.get_problem(p.id)
                idstr = str(p.id)
                if title == None:
                    continue 
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
                    continue
                slug = problem['data']['question']['questionTitleSlug']

                # 题目节点
                g.node(name=idstr, label=title, target="_parent", href="https://leetcode-cn.com/problems/"+slug, 
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
    leet = leetcode.Leetcode()
    view = LeetcodeView(leet)
    leet.update_db()
    view.generate_leetcode(leet, "leetcode/leetcode-dp.txt", "dynamic-programming", "leetcode_dp")
    view.generate_leetcode(leet, "leetcode/leetcode-tree.txt", "tree", "leetcode_tree")
    view.generate_leetcode(leet, "leetcode/leetcode-string.txt", "string", "leetcode_string")
    view.generate_leetcode(leet, "leetcode/leetcode-mini.txt", "", "leetcode_mini")
    view.generate_leetcode(leet, "leetcode/leetcode-linked-list.txt", "linked-list", "leetcode_linked_list")
    view.generate_leetcode(leet, "leetcode/leetcode-union-find.txt", "union-find", "leetcode_union_find")
    view.generate_leetcode(leet, "leetcode/leetcode-heap-stack-queue.txt", "", "leetcode_heap_stack_queue")
    view.generate_leetcode(leet, "leetcode/leetcode-geometry.txt", "geometry", "leetcode_geometry")
    view.generate_leetcode(leet, "leetcode/leetcode-binary-search.txt", "binary-search", "leetcode_binary_search")
    leet.close_db()
