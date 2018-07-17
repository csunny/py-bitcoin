#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9 
"""

from core.blockchain.block import new_genesis_block
from core.transactions.transaction import new_coinbase_tx


# def test_v0_1_0_version():
#     b = Block()
#
#     b.new_block("Magic", "")
#
#     block = b.block
#
#     new_block = b.new_block("This is a test block", b.block["Hash"])
#
#     assert new_block["PrevBlockHash"] == block["Hash"]


def test_genesis_block():
    coinbase = new_coinbase_tx("7AgP8z7XYyZ2sdnVJ6HCiE5X2reJDf")

    genesis_block = new_genesis_block(coinbase)
    print(genesis_block)


if __name__ == '__main__':
    test_genesis_block()
