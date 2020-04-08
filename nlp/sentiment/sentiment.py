# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:24544
# datetime:2020-04-06 14:26
# software: PyCharm
# 使用情感词典完成，简单的情感分析

sentiment_dictionary = {}
for line in open("./BosonNLP_sentiment_score.txt",encoding="utf-8"):
	if line.strip() == "":
		continue
	try:
		word,score = line.strip().split(" ")
		sentiment_dictionary[word] = float(score)
	except:
		print("line=",line)

# for k,v in sentiment_dictionary.items():
# 	print(k,v)

words = ['你妹','不开心','垂头丧气','我日']

total_score = sum(sentiment_dictionary.get(word,0) for word in words)
print(total_score)
