#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/11 
"""


def fab(n):
    result = dict()

    result[0] = 0
    result[1] = 1

    for i in range(2, n + 1):
        result[i] = result[i - 1] + result[i - 2]

    return result[n]


def fab_resu(n):
    if n < 2:
        return n
    return fab(n - 1) + fab(n - 2)


if __name__ == '__main__':
    res = fab(100000000)
    print(res)

    # res = fab_resu(10000000)
    # print(res)
