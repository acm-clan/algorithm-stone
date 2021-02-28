import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import json
import requests
from sqlitedict import SqliteDict
import util
import os

class PageProblemInfo:
    def __init__(self):
        self.id = ""
        self.url = ""
        self.name = ""
        self.tags = ""
        self.rate = 0
        self.solved = 0

class Codeforces:
    def __init__(self):
        self.dict = self.init_db()
        self.finished = []
        # read user
        p = util.get_root("user", "codeforces")
        entries = os.listdir(p)
        self.finished = entries

    def init_db(self):
        d = SqliteDict(util.get_db('codeforces.sqlite'), autocommit=True)
        return d

    def save_problem_meta(self, id, str):
        self.dict["codeforces_problem_meta_%s" % id] = str
    
    def get_problem_meta(self, id):
        return self.dict.get("codeforces_problem_meta_%s" % id)

    def get_db_problem(self, id):
        return self.dict.get("codeforces_problem_%s" % id)

    def save_db_problem(self, id, data):
        self.dict["codeforces_problem_%s" % id] = data

    def get_page_problems(self, page_id):
        url = "https://codeforces.com/problemset/page/%d" % (page_id)
        f = urllib.request.urlopen(url)
        content = f.read().decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        p = soup.select("table.problems")[0]
        trs = p.select("tr")
        probleams = []

        for k in trs:
            if len(k.select("td.id")) == 0:
                continue
            info = PageProblemInfo()
            nodeid = k.select("td.id a")[0]
            info.id = nodeid.get_text().strip()

            if self.get_problem_meta(info.id) != None:
                continue

            self.save_problem_meta(info.id, str(k))
            info.url = nodeid["href"].strip()
            info.name = k.select("td")[1].select("div")[0].select("a")[0].get_text().strip()
            info.tags = k.select("td")[1].select("div")[1].select("a")
            probleams.append(info)

        return probleams

    def check_problem(self, id, cid, index):
        if self.get_db_problem(id) != None:
            return
        url = "https://codeforces.com/problemset/problem/%s/%s" % (cid, index)
        
        try:
            f = urllib.request.urlopen(url)
            content = f.read().decode('utf-8')
            self.save_db_problem(id, content)
        except Exception as e:
            print("check problem error:", e)
            pass

    def update_db(self):
        url = "https://codeforces.com/api/problemset.problems"
        
        try:
            f = urllib.request.urlopen(url)
            content = f.read().decode('utf-8')
            qlist = json.loads(content)
        
            for k in qlist["result"]["problems"]:
                id = str(k['contestId'])+str(k['index'])
                print("id:", id, k['name'])
                value = json.dumps(k)
                self.save_db_problem(id, value)
        except Exception as e:
            print("update_db error:", e)
            pass
    
    def close_db(self):
        pass

