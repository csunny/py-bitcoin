#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/6 
"""

from crypto.base58 import base58encode, base58decode


if __name__ == '__main__':

    # data = "0x110966776006953D5567439E5E39F86A0D273BEED61967F6"
    #
    # r = base58encode(data)
    # print(r)
    #
    # s = base58decode(r)
    #
    # assert len(s) == len(data)
    # assert s.lower() == data.lower()


    # data2 = "25gskL8otKZkGauzWoTBG4nfpGeFE8v"


    data3 = "0xa0b50f87ffd489b87b5539879d70a1ca857bc43ce229"

    res = base58encode(data3)
    print(res)

    sv = base58decode(res)
    print(sv)
    print(data3)

