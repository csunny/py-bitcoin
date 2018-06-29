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

from datetime import datetime


def new_genesis_block(coinbase):
    """
    生成创世区块
    :param coinbase:
    :return:
    """
    pass


def new_block(transaction, prev_block, height):
    """
        根据交易生成一个新的创世区块
    :param transaction:
    :param prev_block:
    :param height:
    :return:
    """
    block = {
        "Timestamp": datetime.now(),
        "Transaction": transaction,
        "PrevBlockHash": prev_block,
        "Height": height
    }



