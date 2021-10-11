#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string

# ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
# print(string.ascii_letters)    output：abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)      output：0123456789

i = 0
while(i<200):
    print(''.join(random.sample(string.ascii_letters + string.digits, 10)))
    i+=1