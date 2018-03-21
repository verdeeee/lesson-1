# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 12:06:46 2018

@author: CUIBing
"""

#给一个语料，做个wordlist，并取出频率最高前10和频率最低的前10个word分别将其与频数打印出来
#去掉标点，转换大小写





#所有文件写到了data文件里
import codecs
f1 = open('1.txt')
f = open('data.txt', 'w')
for line in f1:
    f.write(line)  
f1.close() 
f.close()


f2 = open('2.txt',encoding='utf-8')
f = open('data.txt', 'a')
for line in f2:
    f.write(line)  
f2.close() 
f.close()


f3 = open('3.txt',encoding='utf-8')
f = open('data.txt', 'a')
for line in f3:
    f.write(line)  
f3.close() 
f.close()


f4 = open('4.txt',encoding='utf-8')
f = open('data.txt', 'a')
for line in f4:
    f.write(line)  
f4.close() 
f.close()


f5 = open('5.txt',encoding='utf-8')
f = open('data.txt', 'a')
for line in f5:
    f.write(line)  
f5.close() 
f.close()

ff = open('data.txt')
fi=[]
for line in ff:
    for fields in line:
        fields = line.split()
    fi+=fields
#print(fi)
#print(type(fields))是个list
#上述操作已经把所有word放到一个列表中了


#下面把list转换成只出现一次的集合
a = set(fi)
#print(a)

n=0
time=0
zidian={}
for x in a:
    while n<len(fi):
        if fi[n]==x:
            time+=1
        else:
            time+=0
        n+=1
    zidian[x]=time
    n=0
    time=0
#print(zidian)
#字典如何按照values排序？
#zidian_sort=sorted(zidian.items(),key = lambda x:x[1],reverse = True)
z_sort = sorted(zidian.items(), key=lambda d: d[1], reverse=True)
#print(z_sort)

    
h=0
while h<50:
    print(z_sort[h])
    h+=1


ff.close()









