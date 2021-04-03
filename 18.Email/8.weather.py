#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests
from bs4 import BeautifulSoup
import prettytable as pt
from email.utils import parseaddr, formataddr

# 编写了一个函数_format_addr()来格式化一个邮件地址。
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def get_Data(url):
    data_list = []
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')  # 将html代码自动补全，并按html代码格式返回
    wendu = soup.find('div', class_='temperature').get_text()
    tianqi = soup.find('div', class_='weather-icon-wrap').get_text()
    data_list.append("现在的温度：%s\n现在天气情况：%s" % (wendu, tianqi))
    list = soup.find_all('ul', class_='weather-columns')
    for item in list:
        data_list.append(item.get_text())
    print("列表数据：",data_list)
    a = 1
    tb = pt.PrettyTable() #创建PrettyTable对象
    tb.field_names = ["日期","天气","详情"]
    for item in data_list:
        # print(a)
        if a != 1:
            # print(item.strip())
            # print(item.strip().split()[0]+item.strip().split()[1],item.strip().split()[2],item.strip().split()[3])
            tb.add_row([item.strip().split()[0]+item.strip().split()[1],item.strip().split()[2],item.strip().split()[3]])
        else: print(item.strip())
        a+=1
    print(tb)
    return tb



def send_mail(msg,receiver):
    # 收件人
    receiver = receiver
    mail_title = '天气预报'
    mail_body = str(msg)
    # 创建一个实例
    message = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
    # (plain表示mail_body的内容直接显示，也可以用text，则mail_body的内容在正文中以文本的形式显示，需要下载）
    message['From'] = _format_addr(sender)  # 邮件上显示的发件人
    message['To'] = _format_addr(receiver)  # 邮件上显示的收件人
    message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

    smtp = smtplib.SMTP()  # 创建一个连接
    smtp.connect(smtpserver)  # 连接发送邮件的服务器
    smtp.login(username, password)  # 登录服务器
    smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送

    smtp.quit()

if __name__ == '__main__':
    #sender = '发送者邮箱'
    sender = 'Python爱好者 <%s>' % 'huangpeirong2021@sina.com'
    # 发件人邮箱的SMTP服务器（即sender的SMTP服务器）
    smtpserver = 'smtp.sina.com'
    # 发件人邮箱的用户名和授权码（不是登陆邮箱的密码）
    #username = '发送者登陆邮箱'
    #password = '密码'  # （83xxxx202@qq.com邮箱的授权码或者密码）
    username = 'huangpeirong2021@sina.com'
    password = '412c5be17db0124d'  # （83xxxx202@qq.com邮箱的授权码或者密码）
    #url_list = ['url1','url2']
    url_list = ['https://tianqi.so.com/weather/101280101','https://tianqi.so.com/weather/101140101']
    #receiver_list =['接收者邮箱1','接收者邮箱2']
    receiver_list =['997408138@qq.com','m13430348404@163.com']
    for i in range(len(url_list)):
        tb = get_Data(url_list[i]) #获得每一个用户的数据
        send_mail(tb,receiver_list[i]) #发送邮件