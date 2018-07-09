#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/6/29

- 该模块用于生成区块链，区块形式格式如下

block = {
    "Timestamp": datetime.now(),
    "Transaction": {
        "ID": "",    # 交易ID
        "Vin": "",    # 交易输入
        "Vout": ""   # 交易输出
    },
    "PrevBlockHash": "",
    "Hash": "",
    "Nonce": "",
    "Height": ""
}

"""
from core.blockchain.block import Block
from consensus.proof_of_work import ProofOfWork


class BlockChain:
    """
    doc New blockchain
    """

    def __init__(self):
        self.blocks = []

    def add_block(self, data):

        if self.blocks:

            last_block = self.blocks[-1]
            b = Block()
            new_block = b.new_block(data, last_block["Hash"])

            pow = ProofOfWork(new_block, new_block["Nonce"])

            if pow.validate():
                self.blocks.append(new_block)
        else:
            b = Block()
            new_block = b.new_block(data)

            pow = ProofOfWork(new_block, new_block["Nonce"])
            if pow.validate():
                self.blocks.append(new_block)

    def print_blockchain(self):
        """
        输出blockchain

        :return:
        """
        for b in self.blocks:
            print(b)
