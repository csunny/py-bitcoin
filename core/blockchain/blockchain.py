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

        # 这里没有迭代创世区块
        if not self.current_hash:
            self.current_hash = self.blocks.get("l")

        last_block = self.blocks.get(self.current_hash).decode()

        if eval(last_block)["PrevBlockHash"]:
            self.current_hash = eval(last_block)["PrevBlockHash"]
            yield eval(last_block)

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
        while True:
            try:
                block = next(self.iterator())
            except StopIteration:

                genesis_hash = self.blocks.get(self.current_hash).decode()
                last_block = eval(genesis_hash)

                coinbase_tx = last_block["Transactions"]
                for tx in coinbase_tx:
                    tx_obj = json.loads(tx.decode())
                    if tx_obj["ID"] == tid:
                        return tx
                break

            for tx in block["Transactions"]:
                tx_obj = json.loads(tx.decode())

                if tx_obj["ID"] == tid:
                    return tx

            return "未找到交易信息"

    def find_utxo(self):
        """
        找出所有的utxo
        :return:
        """
        utxo = dict()  # 存储utxo的信息
        spent_tx = dict()
        while True:
            try:
                last_block = next(self.iterator())
            except StopIteration:
                genesis_hash = self.blocks.get(self.current_hash).decode()
                last_block = eval(genesis_hash)

                coinbase_tx = last_block["Transactions"]
                for tx in coinbase_tx:

                    tx_json = json.loads(tx.decode())

                    utxo[tx_json["ID"]] = []

                    for out in tx_json["Vout"]:
                        if not spent_tx[tx_json["ID"]]:
                            utxo[tx_json["ID"]].append(out)

                break     # 程序退出边界条件

            for tx in last_block["Transactions"]:
                tx_json = json.loads(tx.decode())
                utxo[tx_json["ID"]] = []

                for out in tx_json["Vout"]:
                    if not spent_tx[tx_json["ID"]]:
                        utxo[tx_json["ID"]].append(out)

                for vin in tx_json["Vin"]:
                    spent_tx[vin["txid"]] = []

                for vin in tx_json["Vin"]:
                    spent_tx[vin["txid"]].append(vin)

        return utxo

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
