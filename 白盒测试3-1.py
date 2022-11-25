# -*- codeing = utf-8 -*-
# @Time : 2022/5/4 21:05
# @Author : DongYun
# @File : 白盒测试3-1.py
# @Software : PyCharm
import unittestreport
import unittest
# 1、加载测试用例到套件中
suite = unittest.defaultTestLoader.discover('F:\fork\leetcode\白盒测试3.py')

# 2、创建一个用例运行程序
runner = unittestreport.TestRunner(suite,
                                   tester='董赟',
                                   filename="F:\\",
                                   report_dir=".",
                                   title='软件测试',
                                   desc='测试生成的报告',
                                   templates=2
                                   )

# 3、运行测试用例
runner.run()