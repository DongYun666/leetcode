# -*- codeing = utf-8 -*-
# @Time : 2022/4/18 20:42
# @Author : DongYun
# @File : HJ65 查找两个字符串a,b中的最长公共子串.py
# @Software : PyCharm

# while True:
#     try:
#         res = ""
#         a,b = input(),input()
#         if len(a)>len(b):
#             a,b = b,a
#         for i in range(len(a)):
#             for j in range(i+1,len(a)):
#                 if a[i:j+1] in b and j+1-i > len(res):
#                     res = a[i:j+1]
#         print(res)
#     except:
#         break
print(len("nvlrzqcjltmrejybjeshffenvkeqtbsnlocoyaokdpuxutrsmcmoearsgttgyyucgzgcnurfbubgvbwpyslaeykqhaaveqxijc"))
print(len("wkigrnngxehuiwxrextitnmjykimyhcbxildpnmrfgcnevjyvwzwuzrwvlomnlogbptornsybimbtnyhlmfecscmojrxekqmj"))