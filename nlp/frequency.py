# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-06 14:49
# software: PyCharm
# 频率统计

import nltk
import jieba
from nltk import FreqDist

# 英文使用nltk
corpus = "hello，haha,he,you,hello,he,hi,she,it,me,father"
tokens = nltk.word_tokenize(corpus)
print(tokens)
fdlist  =FreqDist(tokens)
print('[he]:',fdlist['he']) # 'he'出现的次数

print("="*20)
# 中文使用jieba
corpus = "你好，我说你是一个大好人，你说对吗？"
tokens = [x for x in jieba.cut_for_search(corpus)]
print(tokens)
fdlist  =FreqDist(tokens)
print('[你]:',fdlist['你']) # ‘你’出现的次数

print(type(fdlist))
standard_freq_vector = fdlist.most_common(5) # 取最常用的3个单词
print(type(standard_freq_vector))
print(len(standard_freq_vector))
print(standard_freq_vector)


def positioin_lookup(v):
	res ={}
	position_counter = 0
	for word in v:
		res[word[0]] = position_counter
		position_counter += 1
	return res
standard_position_dict = positioin_lookup(standard_freq_vector)
print("位置对照表：")
print(standard_position_dict)


# 对于一个新的句子
new_sentence = "我说，你好。你也对我说，你好"
# 新建一个跟我们的标准vector同样大小的向量
freq_vector = [0] * len(standard_position_dict)
new_tokens = [x for x in jieba.cut_for_search(new_sentence)]
# 注意，直接使用jieba.cut_for_search(),而不组成list>>>得到的是一个generator,使用过一次后就会数据清空。


# 对于这个新句子中的每个单词
for word in new_tokens:
	try:
		# 如果我们词库里出现过，那么就在‘标准位置’上加一
		freq_vector[standard_position_dict[word]] += 1
	except KeyError:
		# 如果是个新词，就pass掉
		continue

print(tokens)
print(freq_vector)