#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis
import random,string

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
i = 0   # 计数器
while(i<200):
    ran_code = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    r = redis.Redis(connection_pool=pool)
    r.set(i+1,ran_code)
    i=i+1