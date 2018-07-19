# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:04:04 2018

@author: CUIBing
"""
'''
思路：
1. 按行读文件
2. 用正则表达式提取文件中需要翻译的内容（“=”后的内容）
3. 保留了所有“目录”不被翻译
4. 调用百度翻译api
5. 翻译后的内容替换原内容
6. 写入新文件中（这里为了跟原文件进行区分，重新将文件命名）

跑完这个程序大约需要23分钟
'''
import re
import machine_translation_baidu as mtbaidu
# 待翻译文件读入
f = open("LocaleResource_en_US.properties", "r")  # 打开此文件，方式为只读
lines = f.readlines()     # 按行读
f.close()   # 关闭文件

# 调用了百度翻译api
def source_en(content):
    baidu = mtbaidu.BaiduFanyi("zh","en")  # 创建BaiduFanyi类的实例
    translation_baidu = baidu.translate(content)
    return translation_baidu #返回翻译结果
  
# 正则表达式提取待翻译文本
# r= (.*)|=(.*)' ：匹配“=”或“= "后所有内容

a = re.compile(r'= (.*)|=(.*)')

f1 = open("./out.properties", "a")#将翻译好的文本写入新的文件
for line in lines:
    ar = []
    a1 = re.search(a, line)

    if a1:
        b = a1.group()#得到的结果b：匹配“=”或“= "后《所有内容》
       
        # b1:去掉了“=”
        b1 = re.sub(r'=', '', b)
        #print(b1)
        if("/") in b:#等号后的内容有“/”目录不翻
            if ("<") in b:#如果有标签
                bbb = line.replace(b1, source_en(b1))#翻译这句话并将翻译的部分替换
                ar.append(bbb)
                print(ar)
            else:#目录不翻译，直接写入文件
                ar.append(line)
                print(ar)
        else:#除上述情况之外，把等号后的内容经过b1的修改后进行翻译，并替换
            bb = line.replace(b1, source_en(b1))
            ar.append(bb)
            print(ar)
    for x in ar:
        f1.write(x)
f1.close()



