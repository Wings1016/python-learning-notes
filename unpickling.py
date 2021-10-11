#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

file = open('/Users/herry/Documents/python/test2.txt','rb')
d = pickle.load(file)
file.close()
print(d)