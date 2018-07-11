#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/11 
"""


from storage.redis_storage import Redis


if __name__ == '__main__':
    r = Redis()

    r.set('magic', {"index": 1, "sex": "男", "age": 18})

    # print(r.get("magic").decode())
    #
    # print(r.rds.keys())

    for k in r.keys():
        print(r.get(k).decode())

    # r.remove("magic")
    # print(r.get("magic"))

