#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/6 
"""

Base58Alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58decode(data):
    pass


def base58encode(data):

    result = []
    # 首先将字符串转换成十六进制数
    x = int(data, 16)
    base = 58

    zero = 0

    while x != zero:
        x, mod = divmod(x, base)
        result.append(Base58Alphabet[mod])

    if data[0] == 0x00:
        result.append(base58encode([0]))

    # 利用自己实现的reverse算法，当然实际工作中直接调用python标准库中的函数
    return "".join(reverse(result))


def reverse(res):
    """
    反转列表
    :param res:
    :return:
    """

    if len(res) <= 1:
        return res

    length_half = int(len(res) / 2)
    length = len(res) - 1

    for i in range(length_half):
        tmp = res[i]
        res[i] = res[length-i]
        res[length-i] = tmp

    return res






