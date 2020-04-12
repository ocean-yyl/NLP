# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-12 15:13
# software: PyCharm
"""简单文本分类器"""
import os

import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


# 预处理文本
def preprocess(path):
	text_with_space = ""
	with open(path, encoding="utf-8", errors="ignore") as f:
		textfile = f.read()
		textcuts = jieba.cut(textfile)
		for word in textcuts:
			text_with_space += word + " "
	return text_with_space


# 分类加载文本路径与分类标签信息
def load_train_set(path, classtag):
	allfiles = os.listdir(path)
	processed_textset = []
	class_tags = []
	for file in allfiles:
		pathname = os.path.join(path, file)
		processed_textset.append(preprocess(pathname))
		class_tags.append(classtag)

	return processed_textset, class_tags


def run():
	processed_textset1, class_tags1 = load_train_set("./car", "汽车")
	processed_textset2, class_tags2 = load_train_set("./sports", "运动")
	train_data = processed_textset1 + processed_textset2
	classtags_list = class_tags1 + class_tags2

	count_vector = CountVectorizer()
	vect_matrix = count_vector.fit_transform(train_data) # 构建向量矩阵,此处若使用transform，会报错sklearn.exceptions.NotFittedError: Vocabulary not fitted or provided
	"""
	CountVectorizer.fit_transform
	Learn the vocabulary dictionary and return term-document matrix.
	This is equivalent to fit followed by transform, but more efficiently implemented.
	
	CountVectorizer.transform
	Transform documents to document-term matrix.
	Extract token counts out of raw text documents using the vocabulary
	fitted with fit or the one provided to the constructor.
	"""

	# tfidf 提取特征
	train_tfidf = TfidfTransformer(use_idf=False).fit_transform(vect_matrix) # 构建模型
	clf = MultinomialNB()
	clf.fit(train_tfidf, classtags_list) # 训练模型


	test_count_vector = count_vector.transform([preprocess("./test/text_news")]) # 加载待预测新文件为向量矩阵
	test_tfidf = TfidfTransformer(use_idf=False).fit_transform(test_count_vector) # 构建新的tfidf模型
	predicted_result = clf.predict(test_tfidf) # 使用之前训练的模型来预测
	print(predicted_result) # 打印预测结果


if __name__ == '__main__':
	run()
