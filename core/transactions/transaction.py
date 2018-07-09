#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9 
"""

import hashlib


class Transaction:
    """
    doc  交易
    """

    def __init__(self, ID, vin, vout):
        """
        ID 交易的hash值
        :param ID:
        :param vin:  vin 所有的交易输入
        :param vout:  vout 所有的交易输出
        """
        self.ID = ID
        self.Vin = vin
        self.Vout = vout

    def is_coinbase(self):
        """
        只有一个输入，并且输入没有任何输出。
        :return:
        """
        return len(self.Vin) == 0 and len(self.Vin[0].txid) == 0 and self.Vin[0].vout == -1

    def serialize(self):
        pass

    def hash(self):
        pass

    def sign(self):
        pass

    def string(self):
        pass

    def trimmed_copy(self):
        pass

    def verify(self):
        pass
