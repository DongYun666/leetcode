# -*- codeing = utf-8 -*-
# @Time : 2022/7/17 16:36
# @Author : DongYun
# @File : 1.6.5 算24.py
# @Software : PyCharm
from itertools import permutations
num = [1,0,0,0]
res = []
while num[0]!=0:
    num = list(map(int,input().split()))
    temp = [c for c in permutations(num)]
    symbols = ["+", "-", "*", "/"]
    flag = False
    if not flag:
        for n in temp:
            one, two, three, four = n
            if not flag:
                for s1 in symbols:
                    if not flag:
                        for s2 in symbols:
                            if not flag:
                                for s3 in symbols:
                                    if not flag:
                                        if s1 + s2 + s3 == "+++" or s1 + s2 + s3 == "***":
                                            express = [
                                                "{0} {1} {2} {3} {4} {5} {6}".format(one, s1, two, s2, three, s3, four)]  # 全加或者乘时，括号已经没有意义。
                                        else:
                                            express = ["(({0} {1} {2}) {3} {4}) {5} {6}".format(one, s1, two, s2, three, s3, four),
                                                       "({0} {1} {2}) {3} ({4} {5} {6})".format(one, s1, two, s2, three, s3, four),
                                                       "(({0} {1} ({2} {3} {4})) {5} {6})".format(one, s1, two, s2, three, s3, four),
                                                       "{0} {1} (({2} {3} {4}) {5} {6})".format(one, s1, two, s2, three, s3, four),
                                                       "{0} {1} ({2} {3} ({4} {5} {6}))".format(one, s1, two, s2, three, s3, four)]
                                        for e in express:
                                            try:
                                                if abs(eval(e) - 24) < 0.01:
                                                    flag = True
                                            except ZeroDivisionError:
                                                pass
    res.append('Yes' if flag else 'No')
for i in res[:-1]:
    print(i)
