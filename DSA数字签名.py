# -*- codeing = utf-8 -*-
# @Time : 2022/5/11 17:01
# @Author : DongYun
# @File : DSA数字签名.py
# @Software : PyCharm

import random
import hashlib


import random

# 产生大素数（w位）
def generate_prime(w):
    while True:
        # 产生一个奇数（）
        num = random.randint(2 ** (w - 1), 2 ** w - 1) | 1
        # 对素数进行50次素性检验, 错误概率为：7.888609052210118e-31， 可以忽略
        for i in range(50):
            if not Miller_Rabin(num):
                break
            if i == 49:
                return num

# Miller-Rabin素性检测
def Miller_Rabin(num):
    m = num - 1
    k = 0
    while m % 2 == 0:
        m = m // 2
        k = k + 1
    a = random.randint(2, num)
    b = Mod_P(a, m, num)
    if b == 1:
        return True
    for i in range(k):
        if b == num - 1:
            return True
        else:
            b = b * b % num
    return False


# 非递归求a^n mod p， 快速幂思想
def Mod_P(a, n, p):
    c = 1
    binstr = bin(n)[2:][::-1]  # 通过切片去掉开头的0b，截取后面，然后反转
    for item in binstr:
        if item == '1':
            c = (c * a) % p
            a = (a ** 2) % p
        elif item == '0':
            a = (a ** 2) % p
    return c


def rabin_miller(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

def get_p(q):
    while True:
        t = random.randint(2**159,2**160)
        p = t *q+1
        if Miller_Rabin(p):
            return p
def get_g(p,q):
    while True:
        h = random.randrange(2, q - 2)
        g = pow(h, (p - 1) // q, p)
        if g > 1:
            return g
def EX_GCD(a,b,arr): #扩展欧几里得
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    g = EX_GCD(b, a % b, arr)
    t = arr[0]
    arr[0] = arr[1] #x before = y
    arr[1] = t - int(a / b) * arr[1]
    return g
def ModReverse(a,n): #ax=1(mod n) 求a模n的乘法逆x
    arr = [0,1,]
    gcd = EX_GCD(a,n,arr)
    if gcd == 1:
        return (arr[0] % n + n) % n
    else:
        return -1

if __name__ == '__main__':
    q= generate_prime(150)
    p = get_p(q)
    g = get_g(p,q)
    x = 5
    # 用户的公开要
    y = pow(g, x, p)
    # 代签消息的秘密数
    k = random.randint(1,q-1)
    h = int(hashlib.sha1("hello".encode('utf-8')).hexdigest(),16)
    # 对信息M的签名
    print("p:"+str(p))
    print("q:"+str(q))
    print("g:"+str(g))
    print("y:"+str(y))
    r = pow(g,k,p)%q
    k_1 = ModReverse(k, q)
    s = k_1 *(h + x * r) % q
    # 验证过程
    print("签名(r,s)为:"+str(r),str(s)) #签名结果
    s_1 = ModReverse(s, q)
    w = s_1 % q
    u1 = h* w % q
    u2 = (r * w )% q
    v = (pow(g, u1, p) * pow(y, u2, p))%p % q
    if v == r:
        print("签名有效")
    else:
        print("签名无效")
