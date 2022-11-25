# -*- codeing = utf-8 -*-
# @Time : 2022/4/20 20:10
# @Author : Dongbun
# @File : 判断三角形.pb
# @Software : PbCharm

while True:
    try:
        print("请选择商品:可乐  雪碧   红茶")
        commodity = input()
        while  commodity not in ["可乐","雪碧","红茶"]:
            print("请输入正确的商品名称")
            commodity = input()
        print("请投入货币：1.5元  或者  2元")
        money = input()
        while money not in ['1.5','2']:
            print("请投入正确的货币")
            money = input()
        coom = ["可乐","雪碧","红茶"]
        if commodity in coom:
            if money == '1.5':
                print("请取走"+coom[coom.index(commodity)])
            elif money == '2':
                print("请取走"+coom[coom.index(commodity)]+"，找零5角")
    except:
        break