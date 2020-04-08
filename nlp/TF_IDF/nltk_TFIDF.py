# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-06 15:41
# software: PyCharm
# nltk实现TF-IDF
from nltk.text import TextCollection
# 首先，将所有的文档放进TextCollection类中，这个类会自动断句、做统计、做计算
with open("./text.txt",encoding="utf-8") as f:
	texts = f.readlines()
corpus = TextCollection(texts)

print(corpus.tf_idf('my','my girl is a good girl')) # hello在 hello my girl这句话中的tf-idf值

# 同理，怎么得到一个标准长度的vector来表示所有的句子？
# 对于每一个新句子
new_sentence = "hello my good girl"
# 遍历一遍所有的vocabulary中的词
standard_freq_vector = ['word','yes','my']
for word in standard_freq_vector:
	print(corpus.tf_idf(word,new_sentence))
	# 我们会得到一个巨长(=所有的vocab长度)的向量
