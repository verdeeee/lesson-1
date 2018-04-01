# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 19:25:23 2018

@author: CUIBing
"""

import os
import string

#os.getcwd() 方法用于返回当前工作目录
filedir = os.getcwd()+'/corpara'
#获取当前文件夹中的文件名称列表  
filenames=os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
f=open('result.txt','w')
#遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
    for line in open(filepath,encoding='UTF-8'):
        f.writelines(line)
        f.write('\n')
f.close()
#分词放入列表
'''    
    str.lower()：str中的字母都变成小写
    string.punctuation：找出字符串中的所有的标点
    string.digits：找出字符串中所有数字
    Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）
'''
with open('result.txt','r') as text:
    delStr = string.punctuation + ' ' + string.digits
    words = [word.strip(delStr).lower() for word in text.read().split()]
    #print(words)
#转换成集合形式，去除重复词语
words_index = set(words)

#使用字典统计词频，count() 方法用于统计某个元素在列表中出现的次数
counts_dict = {index:words.count(index) for index in words_index}
#print(counts_dict)
#按照词频从高到低排序
for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):
    if counts_dict[word] > 0:
        print('{} - {}'.format(word,counts_dict[word]))
        
        
        
        
        