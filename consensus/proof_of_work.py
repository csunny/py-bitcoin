#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/6/29 
"""
import copy
from settings import maxNonce


class ProofOfWork:
    """
    工作量证明算法
    """

    def __init__(self, block, nonce=0):
        self.nonce = nonce

        if not isinstance(block, dict):
            raise TypeError

        self.block = block

    def prepare_data(self):
        """
        准备计算的数据
        :return:
        """
        pre_data = copy.deepcopy(self.block)
        pre_data.pop('Hash')

        data = ""

        return data

    def run(self):
        print("Mining  a new block...")
        while self.nonce < maxNonce:
            data = self.prepare_data()
            print(data)

    def validate(self):
        pass
