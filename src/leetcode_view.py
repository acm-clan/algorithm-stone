from graphviz import Digraph
import theme
import util
import os
from pathlib import Path
import datamap
import leetcode
from svgpathtools import svg2paths
from bs4 import BeautifulSoup

svg_icon_finish = '''
<g transform="translate(%s, %s) scale(0.3)">
<circle fill="#4CAF50" cx="24" cy="24" r="21"/>
    <polygon fill="#CCFF90" points="34.6,14.6 21,28.2 15.4,22.6 12.6,25.4 21,33.8 37.4,17.4"/>
</g>
'''

class LeetcodeView:
    def __init__(self, leet):
        self.leet = leet

    def get_module_problem_count(self, m):
        c = 0
        for n in m.nodes:
            c += len(n.problems)
        return c

    def post_process_problem_node(self, n):
        title = n.title.get_text()
        if not self.leet.check_finish(title):
            return
        # get positions
        points = n.g.polygon['points'].split()[0].split(",")
        x = float(points[0])-8
        y = float(points[1])-6
        t = BeautifulSoup(svg_icon_finish % (str(x), str(y)), "xml").select_one("g")
        n.append(t)

    def leetcode_add_finish_icon(self, path):
        c = util.get_file_content(path)
        b = BeautifulSoup(c, "xml")
        nodes = b.select("g.node")
        for n in nodes:
            title = n.title.get_text()
            if not title.isdigit():
                continue
            self.post_process_problem_node(n)
        content = b.prettify()
        util.save_file_content(path, content)

    def leetcode_post_process(self, path):
        self.leetcode_add_finish_icon(path)

    def generate_leetcode(self, leet, file, slug, out_name):
        m = datamap.DataMap(util.get_file_content(util.get_map(file)))
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
                is_finished = leet.check_finish(idstr)

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
        self.leetcode_post_process(util.get_images(out_name)+".svg")

def process():
    leet = leetcode.Leetcode()
    view = LeetcodeView(leet)
    leet.update_db()
    view.generate_leetcode(leet, "leetcode-dp.txt", "dynamic-programming", "leetcode_dp")
    view.generate_leetcode(leet, "leetcode-tree.txt", "tree", "leetcode_tree")
    view.generate_leetcode(leet, "leetcode-linked-list.txt", "linked-list", "leetcode_linked_list")
    view.generate_leetcode(leet, "leetcode-union-find.txt", "union-find", "leetcode_union_find")
    leet.close_db()
