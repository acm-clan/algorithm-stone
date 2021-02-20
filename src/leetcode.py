import urllib.request
import urllib.parse
import json
import requests

db_path = 'leetcode.db'
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

def withUrl(u):
    return "https://leetcode-cn.com/"+u

class Leetcode:
    def __init__(self):
        self.db = ""

    def get_title(self, slug):
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
        content = resp.json()
        return content['data']['question']['questionTitle']

    def update_db(self):
        url = withUrl("api/problems/all/")
        f = urllib.request.urlopen(url)
        content = f.read().decode('utf-8')
        qlist = json.loads(content)

        for q in qlist['stat_status_pairs']:
            id = q['stat']['question_id']
            level = q['difficulty']['level']
            slug = q['stat']['question__title_slug']
            title = self.get_title(slug)
            print("id:", id, level, title)
