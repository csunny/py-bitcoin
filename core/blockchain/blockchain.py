#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/6/29

- 该模块用于生成区块链，区块形式格式如下

block = {
    "Timestamp": datetime.now(),
    "Transactions": {
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
from core.blockchain.block import Block
from storage.redis_storage import Redis
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
        self.current_hash = None

    def add_block(self, new_block):
        """
        添加block到链上
        :param new_block:
        :return:
        """

        # there we should mark last block hash to create a new block.
        # in the redis the l is the last block hash value key.

        pow = ProofOfWork(new_block, new_block["Nonce"])
        if pow.validate():
            # self.blocks.append(new_block)
            if not self.blocks.get(new_block["Hash"]):
                # 不存在的加入
                self.blocks.set(new_block["Hash"], new_block)
                self.blocks.set("l", new_block["Hash"])

    def get_height(self):
        last_hash = self.blocks.get("l")
        last_block = self.blocks.get(last_hash).decode()

        return eval(last_block)["Height"]

    def iterator(self):

        if not self.current_hash:
            self.current_hash = self.blocks.get("l")

        last_block = self.blocks.get(self.current_hash).decode()

        if eval(last_block)["PrevBlockHash"]:
            self.current_hash = eval(last_block)["PrevBlockHash"]
            return last_block

    def get_block(self, block_hash):
        block = self.blocks.get(block_hash)
        if block:
            return eval(block.decode)

        else:
            return "区块不存在"

    def find_tx(self, tid):
        """
        根据交易id找到交易信息
        :param tid:
        :return:
        """
        pass

    def all_hashes(self):

        return [b for b in self.blocks.keys() if b != 'l']

    def mine_block(self, transactions):

        """
        根据链上的最后一个区块的hash值，生成一个新的block
        :param transactions:
        :return:
        """
        lash_hash = self.blocks.get("l").decode()
        height = self.get_height()
        b = Block()
        new_block = b.new_block(transactions, lash_hash, height + 1)
        return new_block

    def sign_transaction(self, tx):
        """
        交易信息加密
        :return:
        """
        pass

    def verify_transaction(self, tx):
        """
        交易信息解密
        :return:
        """
        pass

    def print_blockchain(self):
        """
        输出blockchain

        :return:
        """
        # for b in self.blocks:
        #     print(b)

        blocks = []

        for b in self.blocks.keys():

            if b.decode() != 'l':
                v = self.blocks.get(b).decode()
                blocks.append(eval(v))
        return blocks
