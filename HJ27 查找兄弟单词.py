# -*- codeing = utf-8 -*-
# @Time : 2022/4/12 20:42
# @Author : DongYun
# @File : HJ27 查找兄弟单词.py
# @Software : PyCharm
from collections import Counter


def equals(s1,s2):
    s1 = Counter(s1)
    s2 = Counter(s2)
    return s1 == s2
def pandaun(dict_word,find_word):
    res = []
    for word in dict_word:
        if word == find_word or len(word)!= len(find_word):
            continue
        if equals(word,find_word):
            res.append(word)
    return res
while True:
    try:
        k = list(map(str, input().split()))
        N = int(k[0])
        dict_word = k[1:N+1]
        find_word = str(k[-2])
        find_index = int(k[-1])
        res = pandaun(dict_word,find_word)
        res = sorted(res,key=str.upper)
        print(len(res))
        print(res[find_index-1])
    except:
        break

# 3 abc bca cab abc 1