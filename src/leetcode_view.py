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

svg_text_key = '''
<g class='key'>
  <defs>
    <filter x="-0.1" y="-0.1" width="1.2" height="1.2" id="solid">
      <feFlood flood-color="#CCFF90" result="bg" />
      <feMerge>
        <feMergeNode in="bg"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
<text filter="url(#solid)" text-anchor="middle" x="%s" y="%s" font-family="Microsoft YaHei" font-size="10.00">%s</text>
</g>
'''

class LeetcodeView:
    def __init__(self, leet):
        self.leet = leet
        self.m = None

    def get_module_problem_count(self, m):
        c = 0
        for n in m.nodes:
            c += len(n.problems)
        return c

    def post_process_problem_node(self, graph, n):
        title = n.title.get_text()
        
        # get positions
        points = n.g.polygon['points'].split()
        p0 = points[0].split(",")
        x0 = float(p0[0])
        y0 = float(p0[1])
        t = BeautifulSoup(svg_icon_finish % (str(x0-8), str(y0-6)), "xml").select_one("g")
        # add finish icon
        if self.leet.check_finish(title):
            n.append(t)
        # key text
        p1 = points[1].split(",")
        x1 = float(p1[0])
        y1 = float(p1[1])
        p2 = points[2].split(",")
        x2 = float(p2[0])
        y2 = float(p2[1])
        pro = self.m.problem_map[title]
        # add key text
        if 'key' in pro.tags:
            key_node = BeautifulSoup(svg_text_key % (str((x1+x0)/2), str(y2+5), pro.tags['key']), "xml").select_one("g")
            graph.append(key_node)

    def leetcode_add_finish_icon(self, path):
        c = util.get_file_content(path)
        b = BeautifulSoup(c, "xml")
        nodes = b.select("g.node")
        graph = b.select_one("g.graph")
        for n in nodes:
            title = n.title.get_text()
            if not title.isdigit():
                continue
            self.post_process_problem_node(graph, n)
        content = b.prettify()
        util.save_file_content(path, content)

    def leetcode_post_process(self, path):
        self.leetcode_add_finish_icon(path)

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
