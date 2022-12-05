import urllib.request
import urllib.parse
import json
import requests
from sqlitedict import SqliteDict
import util
import os

db_path = 'leetcode.db'
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

def withUrl(u):
    return "https://leetcode-cn.com/"+u

def leetcode_key(id):
    return "leetcode_"+str(id)

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

class Leetcode:
    def __init__(self):
        self.dict = self.init_db()
        self.finished = []
        self.flasks = []
        # read user
        p = util.get_root("user", "leetcode")
        entries = os.listdir(p)
        for k in entries:
            if k.endswith(".cpp") or k.endswith(".py"):
                self.finished.append(k)
            elif k.endswith(".md"):
                self.flasks.append(k)

    def init_db(self):
        d = SqliteDict(util.get_db('leetcode.sqlite'), autocommit=True)
        return d

    def close_db(self):
        self.dict.close()

    def get_tag_problems(self, tag):
        problems = self.get_all_problems()
        datas = [] 
        for k in problems:
            try:
                j = json.loads(problems[k])
                tags = j['data']['question']['topicTags']
                paid_only = j['data']['question']['paid_only']
                if len(tags) > 0:
                    for t in tags:
                        if t['slug'] == tag and paid_only == False:
                            datas.append(j)
                            break
            except Exception as e:
                print("unknow key:", k, e)
                pass
        return datas

    def get_all_problems(self):
        d = {}
        for k, v in self.dict.iteritems():
            if k.startswith("leetcode_") and k[9].isdigit():
                d[k] = v
        return d

    def save_problem(self, id, content):
        self.dict[leetcode_key(id)] = content
        self.dict.commit()

    def get_problem_content(self, id):
        v = self.dict.get(leetcode_key(id))
        return v

    def get_level(self, id):
        content = self.get_problem_content(id)
        if content == None:
            print("title not exist:", id)
            return str(id)
        j = json.loads(content)
        return j['data']['question']['difficulty']

    def check_finish(self, id):
        for k in self.finished:
            if k.startswith(id+"."):
                return True
        return False

    def check_flask(self, id):
        for k in self.flasks:
            if k.startswith(id+"."):
                return k
        return ""

    def get_problem(self, id):
        content = self.get_problem_content(id)
        if content == None:
            print("title not exist:", id)
            return str(id)
        j = json.loads(content)
        return j

    def get_title(self, id):
        content = self.get_problem_content(id)
        if content == None:
            print("title not exist:", id)
            return str(id)
        j = json.loads(content)
        return j['data']['question']['translatedTitle']

    def get_title_with_slug(self, id, slug, paid_only):
        content = self.get_problem_content(id)

        if content:
            j = json.loads(content)
            return j['data']['question']['translatedTitle']

        session = requests.Session()
        headers = {'User-Agent': user_agent, 'Connection':
                   'keep-alive', 'Content-Type': 'application/json',
                   'Referer': withUrl('problems/') + slug}

        url = withUrl('graphql')
        params = {'operationName': "getQuestionDetail",
                  'variables': {'titleSlug': slug},
                  'query': '''query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    questionFrontendId
                    questionTitle
                    questionTitleSlug
                    translatedTitle
                    translatedContent
                    content
                    difficulty
                    stats
                    similarQuestions
                    categoryTitle
                    topicTags {
                    name
                    slug
                }
            }
        }'''}

        json_data = json.dumps(params).encode('utf8')
        resp = session.post(url, data=json_data, headers=headers, timeout=10)
        content = resp.text
        j = json.loads(content)
        j['data']['question']['paid_only'] = paid_only
        self.save_problem(id, json.dumps(j))
        return j['data']['question']['translatedTitle']

    def get_update_db_time(self):
        t = self.dict.get("leetcode_update_db_time")
        if t == None:
            return 0
        return t

    def save_update_db_time(self):
        self.dict["leetcode_update_db_time"] = util.now()

    def update_db(self):
        t = self.get_update_db_time()
        if util.now()-t < 24*3600*1000:
            return

        url = withUrl("api/problems/all/")
        f = urllib.request.urlopen(url)
        content = f.read().decode('utf-8')
        qlist = json.loads(content)

        try:
            for q in qlist['stat_status_pairs']:
                id = q['stat']['question_id']
                front_id = q['stat']['frontend_question_id']
                if is_int(front_id):
                    id = int(front_id)
                level = q['difficulty']['level']
                slug = q['stat']['question__title_slug']
                paid_only = q['paid_only']
                title = self.get_title_with_slug(id, slug, paid_only)
                print("id:", id, level, title)
            
            self.save_update_db_time()
        except Exception as e:
            print("leetcode update db error:", e)
            pass
