#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from html.parser import HTMLParser
import re


def get_content(url):
    with request.urlopen(url) as f:
        data = f.read()
        print("Status:", f.status, f.reason)
    return data.decode("utf-8")


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__flag = ""  # 设置一个空的标志为
        self.info = []  # main()输出

    def handle_starttag(self, tag, attrs):
        if ("class", "event-title") in attrs:
            self.__flag = "name"
        if tag == "time":
            self.__flag = "time"
        if ("class", "say-no-more") in attrs:
            self.__flag = "year"
        if ("class", "event-location") in attrs:
            self.__flag = "localtion"

    def handle_endtag(self, tag):
        self.__flag = ""

    def handle_data(self, data):
        if self.__flag == "name":
            self.info.append("会议名称：" + data)
            # self.info.append(f'会议名称:{data}')
        if self.__flag == "time":
            self.info.append("会议时间：" + data)
        if self.__flag == "year":
            # self.info.append('会议年份：'+data)
            if re.match(r"\s\d{4}", data):  # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                self.info.append(f"会议年份:{data.strip()}")
        if self.__flag == "localtion":
            self.info.append("会议地点：" + data + "\n")


def main():
    url = "https://www.python.org/events/python-events/"
    # 获取html页面
    data = get_content(url)
    # 解析html页面
    parser = MyHTMLParser()
    parser.feed(data)
    for i in parser.info:
        print(i)


if __name__ == "__main__":
    main()