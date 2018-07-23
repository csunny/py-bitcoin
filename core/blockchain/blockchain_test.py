#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9 
"""
from core.blockchain.block import new_genesis_block, Block
from core.transactions.transaction import new_coinbase_tx, Input, Output
from core.blockchain.blockchain import BlockChain


def test_create_bc():
    bc = BlockChain()

    # 创世区块
    coinbase = new_coinbase_tx("7AgP8z7XYyZ2sdnVJ6HCiE5X2reJDf")
    genesis_block = new_genesis_block(coinbase)
    bc.add_block(genesis_block)

    b = Block()
    # 自定义几个block
    for i in range(5):
        transactions = [b'Node1', b"Node2", b"Node3", b"Node4"]
        last_hash = bc.blocks.get("l").decode()
        height = bc.get_height()
        new_block = b.new_block(transactions, last_hash, height+1)
        bc.add_block(new_block)


def iter_blockchain(last_hash=None):
    bc = BlockChain()

    if not last_hash:
        last_hash = bc.blocks.get("l")

    last_block = bc.blocks.get(last_hash).decode()

    print(last_block)
    if eval(last_block)["PrevBlockHash"]:
        return iter_blockchain(eval(last_block)["PrevBlockHash"])

    # ### the way to itertor.
    # for i in range(bc.get_height()):
    #     print(bc.iterator())

    print(next(bc.iterator()))
    print(next(bc.iterator()))
    print(next(bc.iterator()))

if __name__ == '__main__':
    # test_create_bc()
    # s = iter_blockchain()
    bc = BlockChain()




