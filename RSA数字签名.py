# -*- codeing = utf-8 -*-
# @Time : 2022/5/11 14:55
# @Author : DongYun
# @File : RSA数字签名.py
# @Software : PyCharm
# -*-coding:utf-8-*-

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


# 求最大公因子.欧几里得算法
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# 求逆元，扩展欧几里得算法
def Ex_Euclid(x, n):
    r0 = n
    r1 = x % n
    if r1 == 1:
        y = 1
    else:
        s0 = 1
        s1 = 0
        t0 = 0
        t1 = 1
        while r0 % r1 != 0:
            q = r0 // r1
            r = r0 % r1
            r0 = r1
            r1 = r
            s = s0 - q * s1
            s0 = s1
            s1 = s
            t = t0 - q * t1
            t0 = t1
            t1 = t
            if r == 1:
                y = (t + n) % n
    return y


# 产生公私钥
def Build_key():
    p = generate_prime(16)
    print("生成大素数p: "+ str(p))
    q = generate_prime(16)
    print("生成大素数q: "+ str(q))

    n = p * q
    print("生成的n: "+str(n))
    fn = (p - 1) * (q - 1)
    print("生成的fn: "+str(fn))
    while True:
        e = random.randint(2, fn-1)  # 随机选择一个与_n互质的整数，一般选择65537。
        if gcd(e, fn) == 1:        # 模拟计算
            break
    d = Ex_Euclid(e, fn)           # 计算e对_n的模反元素

    return n,e, d                  # 返回公私钥，公钥（n,e）,私钥（n,d）


def sign(m, n, d):
    s = [Mod_P(ord(i), d, n) for i in m]
    return s

def verify(s, n, e):
    return ''.join([chr(Mod_P(i, e, n)) for i in s])


if __name__ == '__main__':

    message = input("请输入加密的内容").encode('utf-8')
    print("message: ")
    print(message)
    m = hashlib.sha512(message).hexdigest()
    n, public_key, selfkey = Build_key()
    print("生成的e: "+str(public_key))
    print("生成的d: "+str(selfkey))
    # 签名
    s = sign(m, n, selfkey)
    # 验证
    v = verify(s, n, public_key)
    if v == m:
        print("解密后的内容：",end='')
        print(str(message)[2:-1])
    print("签名验证成功" if v == m else "签名验证失败")


