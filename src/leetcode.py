import urllib.request
import urllib.parse
import json
import requests
from sqlitedict import SqliteDict
import util

db_path = 'leetcode.db'
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

def withUrl(u):
    return "https://leetcode-cn.com/"+u

def leetcode_key(id):
    return "leetcode_"+str(id)

class Leetcode:
    def __init__(self):
        self.dict = self.init_db()

    def init_db(self):
        d = SqliteDict(util.get_db('leetcode.sqlite'), autocommit=True)
        return d

    def close_db(self):
        self.dict.close()

    def save_problem(self, id, content):
        self.dict[leetcode_key(id)] = content
        self.dict.commit()

    def get_problem(self, id):
        v = self.dict.get(leetcode_key(id))
        return v

    def get_title(self, id):
        content = self.get_problem(id)
        if content == None:
            print("title not exist:", id)
            return str(id)
        j = json.loads(content)
        return j['data']['question']['translatedTitle']

    def get_title_with_slug(self, id, slug):
        content = self.get_problem(id)

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
        self.save_problem(id, content)
        return j['data']['question']['translatedTitle']

    def update_db(self):
        url = withUrl("api/problems/all/")
        f = urllib.request.urlopen(url)
        content = f.read().decode('utf-8')
        qlist = json.loads(content)

        for q in qlist['stat_status_pairs']:
            id = q['stat']['question_id']
            level = q['difficulty']['level']
            slug = q['stat']['question__title_slug']
            title = self.get_title_with_slug(id, slug)
            print("id:", id, level, title)
