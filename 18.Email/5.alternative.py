#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
HIKVNQIMSVUHZNVA
'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

# 编写了一个函数_format_addr()来格式化一个邮件地址。
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'm13430348404@163.com'
password = 'HIKVNQIMSVUHZNVA'
to_addr = 'huangpeirong2021@sina.com'
smtp_server = 'smtp.163.com'

# 邮件对象：
msg = MIMEMultipart('alternative')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText：
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
msg.attach(MIMEText('hello', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open(r'18.Email\test.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型：
    mime = MIMEBase('image', 'jpg', filename='test.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>') # 给附件起个id值，说白了就是唯一标识
    mime.add_header('X-Attachment-Id', '0') # 这行跟网络连接有关，如果不加会报socket.gaierror
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64 编码：
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()