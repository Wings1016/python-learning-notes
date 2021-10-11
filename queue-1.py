#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os, time, random


def writeq(q):
    print("Process %s start to write" % os.getpid())
    for value in 'A' 'B' 'C':
        print('正在写 %s' % value)
        q.put(value)
    time.sleep(random.random())

def readq(q):
    print('Process %s start to read' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__' :
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=writeq, args=(q,))
    pr = Process(target=readq, args=(q,))
    # 启动子进程pw，开始写
    pw.start()
    # 启动子进程pr，开始读
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()