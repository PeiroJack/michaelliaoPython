#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
#最简单也是最有效的生成XML的方法是拼接字符串：
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(encode('some & data'))
L.append(r'</root>')
return ''.join(L)
'''



from xml.parsers.expat import ParserCreate
#利用SAX解析XML文档牵涉到两个部分: 解析器和事件处理器
#解析器负责读取XML文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
#而事件处理器则负责对事件作出响应，对传递的XML数据进行处理

class DefualtSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_elment: %s,attrs: %s'%(name,str(attrs)))
        #name表示节点名称，attrs表示节点属性（字典）
    def end_element(self,name):
        print('sax:end_element: %s'%name)

    def char_data(self,text):
        print('sax:char_data: %s'%text)
        #text表示节点数据
xml=r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

#处理器实例
handler=DefualtSaxHandler()
#解析器实例
parser=ParserCreate()

#下面3为解析器设置自定义的回调函数
#回调函数的概念，请搜索知乎，见1.9K赞的答案
parser.StartElementHandler=handler.start_element
parser.EndElementHandler=handler.end_element
parser.CharacterDataHandler=handler.char_data
#开始解析XML
parser.Parse(xml)
#然后就是等待expat解析，
#一旦expat解析器遇到xml的 元素开始，元素结束，元素值 事件时
#会回分别调用start_element, end_element, char_data函数

#关于XMLParser Objects的方法介绍下
#详见python文档：xml.parsers.expat
#xmlparser.StartElementHandler(name, attributes)
#遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典
#xmlparser.EndElementHandler(name)
#遇到XML结束标签时调用。
#xmlparser.CharacterDataHandler(data) 
#调用时机：
#从行开始，遇到标签之前，存在字符，content 的值为这些字符串。
#从一个标签，遇到下一个标签之前， 存在字符，content 的值为这些字符串。
#从一个标签，遇到行结束符之前，存在字符，content 的值为这些字符串。
#标签可以是开始标签，也可以是结束标签。

#为了方便理解，我已经在下面还原来解析过程，
#标出何时调用，分别用S：表示开始；E：表示结束；D：表示data

'''
如果看不明白，请配合脚本输出结果一起看
S<ol>C
C   S<li>S<a href="/python">CPython</a>E</li>EC
C   S<li>S<a href="/ruby">CRuby</a>E</li>EC
S</ol>E
'''

