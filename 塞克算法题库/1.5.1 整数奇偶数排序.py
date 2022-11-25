# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 21:08
# @Author : DongYun
# @File : 1.5.1 整数奇偶数排序.py
# @Software : PyCharm
num = list(map(int,input().split()))
# def quick_sort(lists,i,j):
#     if i >= j:
#         return list
#     pivot = lists[i]
#     low = i
#     high = j
#     while i < j:
#         if pivot % 2 == 0:
#             while i < j:
#                 if lists[j] %2 ==1:
#                     break
#                 else:
#                     if lists[j]>= pivot:
#                         j -= 1
#                     else:
#                         break
#             lists[i]=lists[j]
#             while i < j:
#                 if lists[i] %2 == 1:
#                     i+=1
#                 else:
#                     if lists[i] <=pivot:
#                         i += 1
#                     else:
#                         break
#             lists[j]=lists[i]
#         else:
#             while i < j:
#                 if lists[j] % 2 == 0:
#                     break
#                 else:
#                     if lists[j] <= pivot:
#                         j -= 1
#                     else:
#                         break
#             lists[i] = lists[j]
#             while i < j:
#                 if lists[i] % 2 == 0:
#                     i += 1
#                 else:
#                     if lists[i] >= pivot:
#                         i += 1
#                     else:
#                         break
#             lists[j] = lists[i]
#     lists[j] = pivot
#     quick_sort(lists,low,i-1)
#     quick_sort(lists,i+1,high)
#     return lists

# for i in quick_sort(num,0,len(num)-1):
#     print(i,end=" ")
odd = []
even = []
for i in num:
    if i%2 == 1 :
        odd.append(i)
    else:
        even.append(i)
odd.sort(reverse=True)
even.sort()
for i in odd+even:
    print(i,end=" ")

# odd_sorted = quick_sort(odd,0,len(odd)-1)
# odd_sorted.reverse()
# even_sorted = quick_sort(even,0,len(even)-1)
# for i in odd_sorted+even_sorted:
#     print(i,end=" ")

