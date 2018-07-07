#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/6 
"""

from utils.base58 import base58encode, base58decode


if __name__ == '__main__':

    data = "0x110966776006953D5567439E5E39F86A0D273BEED61967F6"

    r = base58encode(data)
    print(r)

    s = base58decode(r)

    assert len(s) == len(data)
    assert s.lower() == data.lower()
