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
<circle fill="#4caf50" cx="24" cy="24" r="21"/>
    <polygon fill="#ccff90" points="34.6,14.6 21,28.2 15.4,22.6 12.6,25.4 21,33.8 37.4,17.4"/>
</g>
'''

svg_text_key = '''
<g class='key'>
  <defs>
    <filter x="-0.1" y="-0.1" width="1.2" height="1.2" id="solid">
      <feFlood flood-color="#ccff90" result="bg" />
      <feMerge>
        <feMergeNode in="bg"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
<text filter="url(#solid)" text-anchor="middle" x="%s" y="%s" font-family="Microsoft YaHei" font-size="10.00">%s</text>
</g>
'''

svg_icon_flask = '''
<g transform="translate(%s, %s) scale(0.01)">
  <symbol id="flask" viewBox="0 0 448 512">
    <path fill="#1389fd" d="M437.2 403.5L320 215V64h8c13.3 0 24-10.7 24-24V24c0-13.3-10.7-24-24-24H120c-13.3 0-24 10.7-24 24v16c0 13.3 10.7 24 24 24h8v151L10.8 403.5C-18.5 450.6 15.3 512 70.9 512h306.2c55.7 0 89.4-61.5 60.1-108.5zM137.9 320l48.2-77.6c3.7-5.2 5.8-11.6 5.8-18.4V64h64v160c0 6.9 2.2 13.2 5.8 18.4l48.2 77.6h-172z"></path>
  </symbol>
  <a href="%s">
  <use xlink:href="#flask"/>
  </a>
</g>
'''

class PlatformView(object):
    def __init__(self):
        self.slug = ""

    def check_finish(self, title):
        return False

    def get_problem(self, id):
        return None

    def check_flask(self, id):
        return False

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
        # add finish icon
        if self.check_finish(title):
            t = BeautifulSoup(svg_icon_finish % (str(x0-8), str(y0-6)), "xml").select_one("g")
            n.append(t)
        # key text
        p1 = points[1].split(",")
        x1 = float(p1[0])
        y1 = float(p1[1])
        p2 = points[2].split(",")
        x2 = float(p2[0])
        y2 = float(p2[1])
        # pro = self.m.problem_map[title]
        pro = self.get_problem(title)
        # add key text
        if 'key' in pro.tags:
            key_node = BeautifulSoup(svg_text_key % (str((x1+x0)/2), str(y2+5), pro.tags['key']), "xml").select_one("g")
            graph.append(key_node)
        # add solution
        # flask = self.leet.check_flask(title)
        flask = self.check_flask(title)
        if flask != "":
            url = "https://github.com/acm-clan/algorithm-stone/blob/main/user/%s/%s" % (self.slug, flask)
            text = svg_icon_flask % (str(x0-13), str(y2-9), url)
            t = BeautifulSoup(text, "xml").select_one("g")
            n.append(t)