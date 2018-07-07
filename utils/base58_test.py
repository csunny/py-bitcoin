#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/6 
"""

from utils.base58 import base58encode, reverse


if __name__ == '__main__':

    data = "00010966776006953D5567439E5E39F86A0D273BEED61967F6"
    r = base58encode(data)


    res = reverse(r)
    print(res)