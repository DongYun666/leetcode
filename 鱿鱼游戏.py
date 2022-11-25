# -*- codeing = utf-8 -*-
# @Time : 2021/11/20 21:22
# @Author : DongYun
# @File : 鱿鱼游戏.py
# @Software : PyCharm
import numpy as np
class gamer:
    def __init__(self):
        # 表示该游戏者已经走过了x块玻璃
        self.x = 0
    def choose(self):
        # 表示该游戏者做出选择，0表示选择左边，1表示选择右边
        self.choice = np.random.randint(0, 2)
    def go(self, glass):
        for i in range(0, glass.n):
            if glass.walked[i] == 1:
                self.x += 1
            else:
                glass.walked[i] = 1
                self.choose()
                if self.choice == glass.which[i]:
                    self.x += 1
                else:
                    break
        self.final = self.x  # 该玩家最终通过了的玻璃数量
        return glass


class glass:
    def __init__(self, n):
        self.n = n
        # 生成n个0或1的随机数，0表示左边为安全的玻璃，1则表示右边
        self.which = np.random.randint(0, 2, size=n)
        # 该序列表示每一块玻璃是否被走过，初始置0表示未被走过
        self.walked = np.zeros(n)
n = 18
k = 16

# %%
p = np.zeros(k)
sim = 1000000
for s in range(0, sim):
    if s % 10000 == 0:
        print(s)
    g = glass(n)
    gamers = [gamer() for _ in range(0, k)]
    for i in range(0, k):
        g = gamers[i].go(g)
    for i in range(0, k):
        if gamers[i].final == n:
            p[i] += 1


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.bar(range(1, k + 1), p / sim)
for a, b in zip(range(1, k + 1), p / sim):
    plt.text(a, b, '%.2f%%' % (b * 100), ha='center', va='bottom', fontsize=8)
plt.show()