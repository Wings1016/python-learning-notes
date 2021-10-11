#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')    # 主线程实例的名字叫MainThread，子线程的名字在创建时指定
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)