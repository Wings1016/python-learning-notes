#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib
from email.parser import Parser
from email.utils import parseaddr
from email.header import decode_header

# 2.POP3收取邮件：
'''
收取邮件分两步：

第一步：用poplib把邮件的原始文本下载到本地；

第二部：用email解析原始文本，还原为邮件对象。
'''

# 2.1 POP3下载邮件
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')
# 连接pop3服务器
server = poplib.POP3_SSL(pop3_server,port=995)
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))

# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')

# 2.2 解析出邮件:
# 邮件的Subject或者Email中包含的名字都是经过编码后的str,要正常显示就必须decode
def decode_str(s):
    # 在不转换字符集的情况下解码消息头值,返回一个list
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# 文本邮件的内容也是str,还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示：
def guess_charset(msg):
    print('msg::%s' % msg)
    # 得到字符集
    charset = msg.get_charset()
    print('charset::%s' % charset)
    if charset is None:
        # lower:所有大写字符为小写
        content_type = msg.get('Content-Type', '').lower()
        print('content_type::%s' % content_type)
        # find:检测字符串中是否包含子字符串,返回charset=头字符的位置
        pos = content_type.find('charset=')
        print('pos::', pos)
        if pos >= 0:
            # strip:移除字符串头尾指定的字符(默认为空格)
            charset = content_type[pos + 8:].strip()
    print('charset::%s' % charset)
    return charset


# indent用于缩进显示：
def print_info(msg, indent=0):
    # 初始分析
    if indent == 0:
        # 遍历获取 发件人，收件人，主题
        for header in ['From', 'To', 'Subject']:
            # 获得对应的内容
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    # parseaddr：解析字符串中的email地址
                    hdr, addr = parseaddr(value)
                    # 解码主题
                    name = decode_str(hdr)
                    # 合成内容
                    value = u'%s <%s>' % (name, addr)
            print('%s%s：%s' % (' ' * indent, header, value))
    # 如果消息由多个部分组成，则返回True。
    if msg.is_multipart():
        # 返回list,包含所有的子对象
        parts = msg.get_payload()
        # enumerate将其组成一个索引序列，利用它可以同时获得索引和值
        for n, part in enumerate(parts):
            # 打印消息模块编号
            print('%s part %s' % (' ' * indent, n))
            print('%s--------------------' % (' ' * indent))
            # 递归打印
            print_info(part, indent + 1)
    else:
        # 递归结束条件，打印最基本模块,返回消息的内容类型。
        content_type = msg.get_content_type()
        # 如果是text类型或者是html类型
        if content_type == 'text/plain' or content_type == 'text/html':
            # 返回list,包含所有的子对象，开启解码
            content = msg.get_payload(decode=True)
            # 猜测字符集
            charset = guess_charset(msg)
            if charset:
                # 解密
                content = content.decode(charset)
            print('%s Text: %s' % (' ' * indent, content + '...'))
        else:
            print('%s Attachment: %s' % (' ' * indent, content_type))

msg = Parser().parsestr(msg_content)
print_info(msg)

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()
