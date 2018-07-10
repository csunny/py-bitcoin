#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/10 
"""
from core.blockchain.blockchain import BlockChain

utxoBucket = "chainstate"


# utxoset represents utxo set

class UTXO(BlockChain):
    """
    UTXO 通过继承 BlockChain来实现
    """

    def __init__(self):
        super(UTXO, self).__init__()

    def find_spendable_outputs(self, pub_hash, amount):
        unspent_outputs = dict()

        accumulated = 0
