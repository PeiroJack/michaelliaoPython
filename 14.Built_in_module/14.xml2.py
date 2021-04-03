#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：

https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml

参数woeid是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。
'''

from xml.parsers.expat import ParserCreate            # 引入xml解析模块
from urllib import request                            # 引入URL请求模块

class WeatherSaxHandler(object):                      # 定义一个天气事件处理器

    weather ={'city':1,'cityname':[], 'forecast':[]}               # 初始化城市city和预报信息forecast

    def start_element(self, name, attrs):             # 定义开始标签处理事件
        if name=='beijing':
            self.weather['city']='北京'
        if name == 'city':               # 获取location信息
            self.weather['cityname'].append(attrs['cityname'])          #获取地区名
            # 获取forecast信息
            self.weather['forecast'].append({
                'state':attrs['stateDetailed'], 
                'high':attrs['tem2'], 
                'low':attrs['tem1']
            })

def parseXml(xml_str):                                # 定义xml解析器

    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml_str)                             # 解析xml文本
    print('City'+handler.weather['city'])
    for (x,y) in zip(handler.weather['cityname'],handler.weather['forecast']):             # 打印天气信息
        print('Region:'+x)
        print(y)
       
    return handler.weather
    

# 测试:
URL = 'http://flash.weather.com.cn/wmaps/xml/beijing.xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

m = data.decode('utf-8')
print(m)
result = parseXml(m)

'''结果
City北京
Region:延庆
{'state': '晴', 'high': '7', 'low': '-7'}
Region:密云
{'state': '晴', 'high': '9', 'low': '-6'}
Region:怀柔
{'state': '晴', 'high': '10', 'low': '-6'}
Region:昌平
{'state': '晴', 'high': '9', 'low': '-1'}
Region:平谷
{'state': '晴', 'high': '8', 'low': '-5'}
Region:顺义
{'state': '晴', 'high': '10', 'low': '0'}
Region:门头沟
{'state': '晴', 'high': '10', 'low': '-2'}
Region:海淀
{'state': '晴', 'high': '11', 'low': '-2'}
Region:朝阳
{'state': '晴', 'high': '10', 'low': '-1'}
Region:石景山
{'state': '晴', 'high': '11', 'low': '-2'}
Region:市中心
{'state': '晴', 'high': '9', 'low': '-2'}
Region:丰台
{'state': '晴', 'high': '10', 'low': '-2'}
Region:房山
{'state': '晴', 'high': '9', 'low': '-4'}
Region:大兴
{'state': '晴', 'high': '9', 'low': '-4'}
Region:通州
{'state': '晴', 'high': '9', 'low': '-2'}
'''