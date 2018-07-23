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


=================================
|   遍历所有的区块来查找utxo        |
|   效率太低，                    |
|  is there some useful skill?  |
|                               |
|            chainstate         |
=================================


交易缓存，每次发生交易的时候计算UTXO，然后将其写到database中持久化，下一次交易重新构建utxo,
通过此方法避免每次都要重新计算所有的utxo， 提高计算效率。

"""
from core.blockchain.blockchain import BlockChain
from core.transactions.output import Output, new_utxo_outputs
from crypto.hashripe import hash_pub_key
from core.transactions.input import Input
from core.transactions.transaction import Transaction

utxoBucket = "chainstate"


# utxoset represents utxo set

class UTXO(BlockChain):
    """
    UTXO 通过继承 BlockChain来实现
    """

    def __init__(self):
        super(UTXO, self).__init__()

    def find_spendable_outputs(self, pub_hash, amount):
        """
        找出可以消费的余额
        :param pub_hash:
        :param amount:
        :return:
        """
        unspent_outputs = dict()
        accumulated = 0
        # todo 直接查询utxo use pubkey to find.
        # version_1 don't storage the utxo to database. only
        # 由于不存储utxo的状态，所以每次都需要重新计算。
        # the code need to update
        utxo = self.find_utxo()
        for tix, v in utxo.items():
            unspent_outputs[tix] = []
            for out in v:
                out_obj = Output(out["value"], out["pub_key_hash"])
                if out_obj.is_locked(pub_hash) and accumulated < amount:
                    accumulated += out["value"]
                    unspent_outputs[tix].append(out)

        return accumulated, unspent_outputs

    def utxo(self, pub_key_hash):
        """

        :return:
        """
        utxos = []

        utxo = self.find_utxo()
        for tix, v in utxo.items():
            for out in v:
                out_obj = Output(out["value"], out["pub_key_hash"])
                if out_obj.is_locked(pub_key_hash):
                    utxos.append(out_obj)

        return utxos

    def get_balance(self, pub_key_hash):
        """
        获取账户余额（未交易输出）
        :return:
        """
        balance = 0
        utxos = self.utxo(pub_key_hash)
        for out in utxos:
            balance += out.value

        return balance

    def count_transaction(self):
        """
        计算交易的数量
        :return:
        """
        count = 0

        utxo = self.find_utxo()
        for k, v in utxo.items():
            count += 1

        return count


def new_uxto_transaction(wallet, to, amount, utxo):
    """
    :param f:  发送地址
    :param to: 接收地址
    :param amount: 数量
    :param bc:  blockchain
    :return:
    """
    inputs = []
    outputs = []

    # todo 实现逻辑细节
    pub_key_hash = hash_pub_key(wallet.pub_key)

    acc, valid_outputs = utxo.find_spendable_outputs(pub_key_hash, amount)

    if acc < amount:
        raise ValueError("Not enough money to spend！")

    # 输入
    for txid, outs in valid_outputs.items():
        for out in outs:
            input = Input(txid, out, None, wallet.pub_key)
            inputs.append(input)

    # 输出
    from_addr = wallet.get_address()

    _out = new_utxo_outputs(amount, to)
    outputs.append(_out)

    if acc > amount:
        new_out = new_utxo_outputs(acc - amount, from_addr)
        outputs.append(new_out)

    tx = Transaction("", inputs, outputs)
    tx.ID = tx.hash()
    utxo.sign_transaction(tx, wallet.private_key)

    return tx
