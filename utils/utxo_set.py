#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/10

utxo 支付模型是相当重要的概念。
BTC通过UTXO来处理支付的逻辑。
核心概念为，每次交易都包含有输入跟输出。 所有的输出一定refer 输入。

在使用UTXO的过程中，需要找到整条链上的所有的能够被 pubkeyhash 也就是钱包地址所签名认证的所有的输入与输出，
然后从中找到unspent UTXO
最后根据UTXO 计算balance
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






