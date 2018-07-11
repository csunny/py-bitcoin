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
import json
from storage.redis_storage import Redis
from core.blockchain.block import Block
from consensus.proof_of_work import ProofOfWork


class BlockChain:
    """
    doc New blockchain
    """

    def __init__(self):
        # At first storage blocks in a memory list
        # and then we storage this in redis
        # self.blocks = []

        self.blocks = Redis()

    def add_block(self, data):

        if self.blocks.get('l'):
            # there we should mark last block hash to create a new block.
            # in the redis the l is the last block hash value key.
            last_hash = self.blocks.get('l').decode()
            b = Block()

            new_block = b.new_block(data, last_hash)

            pow = ProofOfWork(new_block, new_block["Nonce"])

            if pow.validate():
                # self.blocks.append(new_block)

                self.blocks.set(new_block["Hash"], new_block)
                self.blocks.set("l", new_block["Hash"])

        else:
            b = Block()
            new_block = b.new_block(data)

            pow = ProofOfWork(new_block, new_block["Nonce"])
            if pow.validate():
                # self.blocks.append(new_block)
                self.blocks.set(new_block["Hash"], new_block)
                self.blocks.set("l", new_block["Hash"])

    def print_blockchain(self):
        """
        输出blockchain

        :return:
        """
        # for b in self.blocks:
        #     print(b)

        for b in self.blocks.keys():
            print(self.blocks.get(b).decode())


