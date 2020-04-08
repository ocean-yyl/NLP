# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:24544
# datetime:2020-04-06 13:33
# software: PyCharm
"""
nltk.sent_tokenize(text) #对文本按照句子进行分割
nltk.word_tokenize(sent) #对句子进行分词
nltk.pos_tag(tokens)#tokens是句子分词后的结果，同样是句子级的标注
"""
import nltk
# nltk.download('punkt')

sentence = "how old are you ?"
tokens = nltk.word_tokenize(sentence)
print(tokens)

# 明显：若要使用nltk处理中文，则需要提前以空格断开分词。
chinese_sentence = "我感觉 用nltk 处理中文 是完全可用的。其重点在于中文分词和文本表达的形式。 中文和英文主要的不同之处是中文需要分词。"
tokens2 = nltk.word_tokenize(chinese_sentence)
print(tokens2)