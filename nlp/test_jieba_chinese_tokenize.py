# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:24544
# datetime:2020-04-06 13:41
# software: PyCharm
import jieba

seg_list = jieba.cut("欢迎来到北京交通大学", cut_all=True)
print("Full mode[全模式]：", "/".join(seg_list))

seg_list = jieba.cut("欢迎来到北京交通大学", cut_all=False)
print("Default mode[精确模式]：", "/".join(seg_list))

seg_list = jieba.cut("欢迎来到北京交通大学")
print("[默认是精确模式]：", "/".join(seg_list))

seg_list = jieba.cut_for_search("欢迎来到北京交通大学")
print("[搜索引擎模式]：", "/".join(seg_list))

"""
正则表达式来处理各种字符、符号等质量不高的文本

"""