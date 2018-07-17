#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/7 
"""

import time
import hashlib
from consensus.proof_of_work import ProofOfWork
from utils.merkletree import MerkleTree
from core.transactions.transaction import Transaction


class Block:
    """

    Todo add index for block.

    doc  区块

    block = {
        "Timestamp": "",
        "Data": "",
        "PrevBlockHash": "",
        "Hash": "",
        "Nonce": ""
    }
    """

    # todo update data to transaction information,  and then the transaction look like
    '''
        block = {
            "Timestamp": datetime.now(),
            "Transactions": [
                {
                    "ID": "",    # 交易ID
                    "Vin": "",    # 交易输入
                    "Vout": ""   # 交易输出
                    },
                {
                    "ID": "",
                    "Vin"" "",
                    "Vout"" "",
                }
            ],
            "PrevBlockHash": "",
            "Hash": "",
            "Nonce": "",
            "Height": ""
        }
    '''

    def __init__(self):
        self.block = dict()

    def new_block(self, transactions, prev_hash, height):
        block = {
            "TimeStamp": int(time.time()),
            "Transactions": transactions,
            "PrevBlockHash": prev_hash,
            "Nonce": 0,
            "Height": height
        }

        pow = ProofOfWork(block)

        b_hash, nonce = pow.run()
        block["Hash"] = b_hash
        block["Nonce"] = nonce

        self.block = block
        return block

    def set_hash(self, block):
        """

        v1
        # timestamp = hex(block["TimeStamp"])[0]
        #
        # data = "".join([block["PrevBlockHash"], block["Data"], timestamp])
        #
        # return hashlib.sha256(data.encode("utf-8")).hexdigest()
        :param block:
        :return:
        """
        # use pow to set the hash value
        timestamp = hex(block["TimeStamp"])[0]

        data = "".join([block["PrevBlockHash"], block["Data"], timestamp])

        return hashlib.sha256(data.encode("utf-8")).hexdigest()


def hash_txs(block):
    """
    将block的transactions 信息hash加密, 并且用merkle tree来存储交易信息。
    :return:
    """

    tree = MerkleTree(block["Transactions"])
    tree.new_tree()

    return tree.root.data


def new_genesis_block(coinbase):
    """
    根据coinbase交易创建一个创世区块
    :param coinbase:
    :return:
    """
    b = Block()

    transaction = Transaction(coinbase.ID, coinbase.Vin, coinbase.Vout)
    genesis_block =  b.new_block(transaction, "", 0)
    return genesis_block
