#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
import smtplib
from email.utils import formataddr, parseaddr
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# 二十一、电子邮件
# 一封电子邮件的旅程就是：
# 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
# MUA：邮件用户代理     MTA：邮件传输代理       MDA：邮件投递代理
# SMTP：发送邮件，MUA和MTA使用的协议，以及MTA和MTA之间。Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
# IMAP、POP3：MUA和MDA

# 1.SMTP发送邮件
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html','utf-8')       
# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

# 通过此函数格式化MIME信息，使得显示发件人、收件人、主题等,否则可能被outlook列为垃圾邮件
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 添加附件：构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象
msg1 = MIMEMultipart()

# msg1.attach(MIMEText('Hello,attach'+
    # '<html><body><p><img src=""cid:0></p></body></html>','html','utf-8'))       

msg1.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

msg1['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg1['To'] = _format_addr('管理员 <%s>' % to_addr)
msg1['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/herry/Documents/python/test.jpg', 'rb') as f:    # 如果要将图片嵌入正文，在MIMEText中添加img标签，然后img里添加src="cid:0"
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpeg', filename='test.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg1.attach(mime)

server = smtplib.SMTP(smtp_server, 587) # SMTP协议默认端口是25，加密ssl的端口是587,smtp.qq.com的话是587、465
server.starttls()       # 加密连接要加这句
server.set_debuglevel(1)    # set_debuglevel(1)打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)   # 登录smtp服务器
server.sendmail(from_addr, [to_addr], msg1.as_string())      # 发送邮件，as_string()将MIME转为str
server.quit()