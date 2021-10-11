#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 子进程要执行的代码
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('Child process end.')