import leetcode
import json
import util

leet = leetcode.Leetcode()

def show_menu():
    print("1 help: show help")
    print("2 leetcode tag 显示所有的tag")
    print("3 leetcode tag [tree|dynamic-programming|...] 显示tag所有题目")
    print("4 leetcode tag [tree|dynamic-programming|...] [easy|medium|hard] 显示tag指定难度所有题目")

def get_problem_id(data):
    id = data['data']['question']['questionId']
    fid = data['data']['question']['questionFrontendId']
    if util.is_int(fid):
        id = fid
    return id

def check_leetcode_tags():
    print("--------------tags begin-------------")
    problems = leet.get_all_problems()
    all_tags = []

    for k in problems:
        j = json.loads(problems[k])
        tags = j['data']['question']['topicTags']
        for t in tags:
            all_tags.append(t['slug'])
    all_tags = list(dict.fromkeys(all_tags))
    all_tags.sort()

    d = {}

    for item in all_tags:
        d[item] = len(leet.get_tag_problems(item))
    sorted(d, key=d.get)

    items = []
    
    for k in sorted(d, key=d.get):
        items.append(str(k)+" "+str(d[k]))

    print('\n'.join(items))
    print("--------------tags end-------------")

def check_leetcode_tag(s):
    if len(s) <= 0:
        check_leetcode_tags()
        return
    tag = s[0].lower()
    level = ""
    if len(s) > 1:
        level = s[1].lower()

    problems = leet.get_all_problems()

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
    # 
    ids = []
    strs = {}
    for k in datas:
        id = get_problem_id(k)
        if int(id) < 100000:
            lv = k['data']['question']['difficulty'].lower()
            if level == lv or level == "":
                ids.append(int(id))
                s = "%s\t%s\t%s" % (id, k['data']['question']['difficulty'], k['data']['question']['translatedTitle'])
                strs[int(id)] = s
    
    ids.sort()
    print(' '.join([str(item) for item in ids ]))

    # 输出详细的题目列表
    print('\n'.join([str(strs[item]) for item in sorted(strs.keys())]))

def check_leetcode(s):
    if s[0] != "leetcode":
        return
    if s[1] == "tag":
        check_leetcode_tag(s[2:])

def main():
    print("This is a query system.")
    show_menu()
    while True:
        s = input().strip()
        if s == "q":
            print('Bye.')
            break
        slist = s.split()
        if s == "help":
            show_menu()
        check_leetcode(slist)

if __name__ == "__main__":
    main()
    leet.close_db()