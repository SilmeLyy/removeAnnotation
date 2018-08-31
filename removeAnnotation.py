#!/usr/bin/python
#encoding:   utf-8
#  author:   未央生
#    date:   2018-08-30 15:34:21
# 删除OC的注释

import os
import re

#项目路径
basePath = '/Users/mihisao/Desktop/screenshots'

# 遍历文件
def traverseDir(path):
	for parent, dirName, fileName in os.walk(path):
		# 判断是否是.h 或者.m文件
		for i in range(0,len(fileName)):
			if fileName[i].endswith('.h') or fileName[i].endswith('.m'):
				removeAnnotation(parent + '/' + fileName[i])


# 删除注释
def removeAnnotation(path):
	#不删除pods文件夹下的注释
	if re.search(r'/Pods/',path):
		return
	
	print(path)
	# 打开文件
	f = open(path)
	text = f.read()
	# 匹配到注释(只能匹配/* */单行或者多行)，替换成空字符串
	search = re.sub(r'/\*(\s|\S)*?\*/','',text,0)
	f.close()

	# 重新以w的方式打开文件
	f = open(path,'w')
	f.write(search)
	f.close()


	# 匹配//类型的注释  顶部文件注释 默认有10行  前面10行默认 文件注释，不管
	f = open(path)
	i = 0
	text = ''
	for line in f.readlines():
		if i > 10:
			ss = re.sub(r'(//((?!").)*$)|(#pragma mark.*?$)','',line,0)
			text += ss
		else:
			text += line
		i += 1
	f.close()

	# 重新以w的方式打开文件
	f = open(path,'w')
	f.write(text)
	f.close()


if __name__ == '__main__':
	traverseDir(basePath)