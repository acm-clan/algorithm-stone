import numpy as np
import random
import string

def compute_prefix_function(p, back=False):
    n = len(p)
    next = np.zeros(n, dtype=int)
    k = -1
    j = 0
    next[0] = -1
    while j < n-1:
        if k == -1 or p[j] == p[k]:
            k+=1
            j+=1
            next[j] = k
            if back:
                print("next[%s]=%s"%(str(j), str(k)))
        else:
            if back:
                print("back:", p[j], p[k], k, "->", next[k])
            k = next[k]
    return next

def check_next(next):
    last = -2
    for i in next:
        if last == -2:
            last = i
        else:
            if i < last and i >=2:
                print(next)
                return True
            last = i
    return False

def run():
    random.seed(1)
    for _ in range(100000):
        p = ''.join(random.choices("abc", k=10))
        next = compute_prefix_function(p)
        if check_next(next):
            print(p)

def run2():
    p = "ababbcaababac"
    print(p)
    next = compute_prefix_function(p, back=True)
    print(next)

# ababbcaababaccc
# ababa 内部的状态
# b的内部状态是2
# 状态的嵌套
# 塌缩：在当前前缀中寻找新的较小的状态值
# 很像动态规划利用已有的信息
# 自底向上进行计算
# next里面的值是表示
# 

if __name__ == "__main__":
    run()
