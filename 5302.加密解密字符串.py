# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 21:02
# @Author : DongYun
# @File : 5302.加密解密字符串.py
# @Software : PyCharm
import itertools
from typing import List
class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keys = keys
        self.values = values
        self.dictionary = dictionary

    def encrypt(self, word1: str) -> str:
        res = []
        def find_index_in_keys(w):
            for index in range(len(self.keys)):
                if self.keys[index] == w:
                    return index
        for w in list(word1):
            print(w)
            res.append(self.values[find_index_in_keys(w)])
        return "".join(res)

    def decrypt(self, word2: str) -> int:
        res = []
        for i in range(0,len(word2),2):
            decrypt_pair = word2[i]+word2[i+1]
            def find_keys_in_values(w):
                keys_list = []
                for index in range(len(self.values)):
                    if self.values[index] == w:
                        keys_list.append(self.keys[index])
                return keys_list
            res.append(find_keys_in_values(decrypt_pair))
        print(res)
        res = itertools.product(res)
        print(res)

    # print(decrypt_pair_list)
if __name__ == '__main__':
    e = Encrypter(['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"])
    res = e.encrypt("abcd")
    e.decrypt("eizfeiam")
    print(res)