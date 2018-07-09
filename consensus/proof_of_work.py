#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/6/29 
"""
import hashlib
from settings import maxNonce, targetBits


class ProofOfWork:
    """
    工作量证明算法
    """

    def __init__(self, block, nonce=0):
        self.nonce = nonce

        if not isinstance(block, dict):
            raise TypeError

        self.block = block
        self.target = 1 << (256-targetBits)

    def prepare_data(self):
        """
        准备计算的数据
        :return:
        """

        timestamp = hex(self.block["TimeStamp"])[0]

        data = "".join([
            self.block["PrevBlockHash"],
            self.block["Data"],
            timestamp,
            hex(targetBits),
            hex(self.nonce)
        ])

        return data

    def run(self):
        print("Mining  a new block...")

        hash_v = ""
        while self.nonce < maxNonce:
            data = self.prepare_data()

            hash_v = hashlib.sha256(data.encode("utf-8")).hexdigest()

            # print("-----> is mining ... %s" % hash_v)

            if int(hash_v, 16) <= self.target:
                break
            else:
                self.nonce += 1
        print("\n")

        return hash_v, self.nonce

    def validate(self):
        data = self.prepare_data()
        hash_v = hashlib.sha256(data.encode('utf-8')).hexdigest()

        print(int(hash_v, 16), self.target)

        if int(hash_v, 16) <= self.target:
            return True
        return False



