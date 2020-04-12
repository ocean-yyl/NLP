# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-12 15:34
# software: PyCharm

def save(file, line):
	with open(file, "a", encoding="utf-8") as f:
		f.write(line)


def cut_toutiao():
	with open("toutiao_cat_data.tsv", encoding="utf-8") as f:
		for line in f:
			if "news_sports" in line:
				save("sports.txt", line.split("_!_", 4)[-1])
			elif "news_car" in line:
				save("car.txt", line.split("_!_", 4)[-1])
			else:
				continue


def cut_car_or_sports(path):
	counter = 0
	with open(path, encoding="utf-8") as f:
		for line in f:
			counter += 1
			save(path + str(counter % 10), line)


if __name__ == '__main__':
	cut_car_or_sports("./car/car.txt0")
	cut_car_or_sports("./sports/sports.txt0")
