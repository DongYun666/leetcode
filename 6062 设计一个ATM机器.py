# -*- codeing = utf-8 -*-
# @Time : 2022/4/17 18:52
# @Author : DongYun
# @File : 6062 设计一个ATM机器.py
# @Software : PyCharm
from typing import List
class ATM:

    def __init__(self):
        self.money_count= {500:0,200:0,100:0,50:0,20:0}

    def deposit(self, banknotesCount: List[int]) -> None:
        banknotesCount.reverse()
        for index in range(len(banknotesCount)):
            self.money_count[list(self.money_count.keys())[index]] +=banknotesCount[index]
        # print(self.money_count)

    def withdraw(self, amount: int) -> List[int]:
        res = [0,0,0,0,0]
        index= 0
        for money,count in self.money_count.items():
            if count == 0:
                index+=1
                continue
            else:
                if amount-money>=0:
                    while amount-money>=0 and self.money_count[money]>0:
                        amount-=money
                        res[index]+=1
                        self.money_count[money]-=1
                    index+=1
                else:
                    index+=1
        if amount == 0:
            res.reverse()
            return res
        else:
            for i in range(len(res)):
                self.money_count[list(self.money_count.keys())[i]]+=res[i]
            return [-1]


if __name__ == '__main__':
    s = ATM()
    # print(s.deposit([0,0,1,2,1]))
    # print(s.money_count)
    # print("------------------------")
    # print(s.withdraw(600))
    # print(s.money_count)
    # print("------------------------")
    #
    # print(s.deposit([0,1,0,1,1]))
    # print(s.money_count)
    # print("------------------------")
    s.deposit([0,1,0,3,1])
    # print(s.withdraw(600))
    # print(s.money_count)
    # print("------------------------")

    print(s.withdraw(550))
    print(s.money_count)
    print("------------------------")


