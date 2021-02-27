from graphviz import Digraph
import util
import os
from pathlib import Path
import datamap
import codeforces

def generate_codeforces(c, filename, slug, svgfile):
    pass

def process():
    c = codeforces.Codeforces()
    c.update_db()
    generate_codeforces(c, "leetcode-dp.txt", "dynamic-programming", "leetcode_dp")
    c.close_db()