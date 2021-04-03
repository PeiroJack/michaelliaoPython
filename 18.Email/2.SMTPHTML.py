#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
HIKVNQIMSVUHZNVA
'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

# 编写了一个函数_format_addr()来格式化一个邮件地址。
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'm13430348404@163.com'
password = 'HIKVNQIMSVUHZNVA'
to_addr = '997408138@qq.com'
smtp_server = 'smtp.163.com'

# 注意到构造MIMEText对象时，
# 第一个参数就是邮件正文，
# 第二个参数是MIME的subtype，传入'plain'表示纯文本，
# 最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="https://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
#msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
'''
From: =?utf-8?b?UHl0aG9u54ix5aW96ICF?= <m13430348404@163.com>
To: =?utf-8?b?566h55CG5ZGY?= <997408138@qq.com>
Subject: =?utf-8?b?5p2l6IeqU01UUOeahOmXruWAmeKApuKApg==?=
'''

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()