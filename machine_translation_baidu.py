#!/usr/bin/env python    
# -*- coding: utf-8 -*

"""
作者：易可可
注释：易可可
创建日期：2018年6月21日
最近更新：2018年6月26日 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
代码功能：
本文件是一段 python 3 代码，调用百度翻译api实现了多语言翻译，
用户可根据需求输入百度翻译api所支持的源语言和目标语言，
程序将执行对本文件同目录下“fanyi.txt”文件里内容的翻译，翻译结果将写入同目录下文件“result_baidu.txt”中。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import http.client
import hashlib
from urllib import parse
import random

class BaiduFanyi:
     # @description: 该类的主功能函数为translate()，可向百度翻译api发送GET请求，得到翻译的结果。
     def __init__(self, ToLanguage, FromLanguage):
        # @param string ToLanguage 目标语言相应代码
        # @param string FromLanguage 源语言相应代码
        self.httpClient = None
        self.myurl = '/api/trans/vip/translate'
        self.appid = '20170608000055366'               #应用id，失效请自行申请更换
        self.secretKey = 'ChiaqzXuOMwL8StWn4ZV'        #应用密钥，失效请自行申请更换
        self.ToLanguage = ToLanguage 
        self.FromLanguage = FromLanguage  
        self.supported_languages = {                   #百度翻译api支持语言
            'zh' : '中文',
            'en' : '英语',
            'kor' : '韩语',
            'jp' : '日语',
            'spa' : '西班牙语',
            'fra': '法语',
            'th' : '泰语',
            'ara' : '阿拉伯语',
            'ru' : '俄语',
            'pt' : '葡萄牙语',
            'yue' : '粤语',
            'wyw' : '文言文',
            'auto' : '自动检测',
         }
     
     def print_supported_languages (self):
        # @description:用户输入的源语言或目标语言不支持时，打印出api支持语言代码及相应意义的列表。
        # @return:百度翻译api支持语言代码及相应意义的列表。
        codes = []
        for k,v in self.supported_languages.items():
            codes.append('\t'.join([k, '=', v]))
        return '\n'.join(codes)
    
     def judge_from_languages (self):
        # @description:检验源语是否支持。
        # @return:源语支持时返回结果1，不支持时返回结果0。
        if self.FromLanguage not in self.supported_languages.keys():                  
            print ('对不起，此API不支持该语言作为源语：', self.FromLanguage)
            print ('请在下列的这些语言中选择您想要的源语：')
            return 0
        else:
            return 1
    
     def judge_to_languages (self):
        # @description:检验译语是否支持。
        # @return:译语支持时返回结果1，不支持时返回结果0。
        if self.ToLanguage not in self.supported_languages.keys():          
            print ('对不起，此API无法翻译成该种语言：', self.ToLanguage)
            print ('请在下列的这些语言中选择您想要的译语：')
            return 0
        else:
            return 1
            
    
     def translate (self, queryText):
	   
        # @description:向api服务器发送请求，得到翻译结果，并写入result_baidu.txt文件中。
        # @param string queryText 待翻译内容
        
        #拼接传入api服务器的url
        salt = random.randint(32768, 65536)
        sign = self.appid+queryText+str(salt)+self.secretKey
        m1 = hashlib.md5()
        m1.update(sign.encode(encoding='utf-8'))
        sign = m1.hexdigest()
        myurl = self.myurl+'?appid='+self.appid+'&q='+parse.quote(queryText)+'&from='+self.FromLanguage+'&to='+self.ToLanguage+'&salt='+str(salt)+'&sign='+sign 
        
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)
            response = httpClient.getresponse()
            string = response.read().decode('utf-8')
            string = eval(string)                   #eval()函数用来执行一个字符串表达式，并返回表达式的值。
            #return string['trans_result']     #str['trans_result']里有百度api返回的翻译结果
            for line in string['trans_result']:     #str['trans_result']里有百度api返回的翻译结果
                return line['dst']      #将返回结果写入打开的result_baidu.txt文件
        except Exception as e:
            #print("请求百度api服务器失败，未得到翻译结果！\n错误原因：{0}".format(e))
            return ''#返回一个空字符串 以方便把翻译结果替换回去
        
        finally:
            if httpClient:
                httpClient.close()