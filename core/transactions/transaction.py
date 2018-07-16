#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9

1. 输出可以不指向另一个输入
2. 一次交易中，一个输入往往对应与多个输出
3. 一个输入必须来自一个输出

If the data is correct, the output can be unlocked, and its value can be used to generate new outputs;
 if it’s not correct, the output cannot be referenced in the input.
  This is the mechanism that guarantees that users cannot spend coins belonging to other people.

"""
import hashlib
import json
from core.transactions.input import Input
from core.transactions.output import Output
from fastecdsa import ecdsa

subsidy = 10   # 交易额


class Transaction:
    """
    doc  交易

    # todo
    """

    def __init__(self, ID, vin, vout):
        """
        ID 交易的hash值
        :param ID:
        :param vin:  vin 所有的交易输入
        :param vout:  vout 所有的交易输出
        """
        self.ID = ID
        self.Vin = vin
        self.Vout = vout

    def is_coinbase(self):
        """
        只有一个输入，并且输入没有任何输出。
        :return:
        """
        return len(self.Vin) == 0 and len(self.Vin[0].txid) == 0 and self.Vin[0].vout == -1

    def serialize(self):

        vins = []
        for vin in self.Vin:
            k = dict()
            k['txid'] = vin.txid
            k['vout'] = vin.vout
            k['signature'] = vin.signature
            k['pubkey'] = vin.pubkey

            vins.append(k)

        vouts = []
        for vout in self.Vout:
            k = dict()
            k['value'] = vout.value
            k['pub_key_hash'] = vout.pub_key_hash
            vouts.append(k)

        data = {
            "ID": self.ID,
            "Vin": vins,
            "Vout": vouts
        }

        return json.dumps(data)

    def hash(self):

        hv = hashlib.sha256(self.serialize().encode('utf-8')).hexdigest()

        self.ID = hv
        return hv

    def sign(self, priv_key, prev_txs):
        """
        sign each input of transaction

        :param priv_key: 私钥
        :param prev_txs: 之前的所有交易
        :return:
        """
        if self.is_coinbase():
            return
        for vin in self.Vin:
            if not prev_txs[vin.txid].ID:
                raise ValueError(
                    "Error: previous transaction is not correct."
                )

        tx_copy = self.trimmed_copy()
        for inId, vin in enumerate(tx_copy.Vin):
            prev_tx = prev_txs[vin.txid]
            tx_copy.Vin[inId].signature = ""
            tx_copy.Vin[inId].pubkey = prev_tx.Vout[vin.vout].pub_key_hash

            r, s = ecdsa.sign(tx_copy, priv_key)
            signature = "".join([str(r), str(s)])
            self.Vin[inId].signature = signature
            tx_copy.Vin[inId].pubkey = ""

    def string(self):
        """
        打印交易的输入和输出
        :return:
        """
        pass

    def trimmed_copy(self):
        inputs = []
        outputs = []

        for vin in self.Vin:
            inpt = Input(vin.txid, vin.vout, "", "")
            inputs.append(inpt)

        for vout in self.Vout:
            opt = Output(vout.value, vout.pub_key_hash)
            outputs.append(opt)

        tx_copy = Transaction(self.ID, inputs, outputs)
        return tx_copy

    def verify(self, prev_txs):
        """
        校验先前的所有输入是否合法
        :param prev_txs:
        :return:
        """
        if self.is_coinbase():
            return True

        for vin in self.Vin:
            if not prev_txs[vin.txid].ID:
                raise ValueError(
                    "Error: previous transaction is not correct."
                )

        tx_copy = self.trimmed_copy()
        for inId, vin in enumerate(tx_copy.Vin):
            prev_tx = prev_txs[vin.txid]
            tx_copy.Vin[inId].signature = ""
            tx_copy.Vin[inId].pubkey = prev_tx.Vout[vin.vout].pub_key_hash

            sign_len = len(vin.signature)
            # x = vin.pubkey[:(sign_len/2)]
            # y = vin.pubkey[(sign_len/2):]
            #
            # raw_pub_key = ecdsa.verify()
            pass

        return True


def new_coinbase_tx(to, data="Base Info, Magic"):
    txin = Input("", -1, None, data)
    txout = Output(subsidy, to)

    tx = Transaction(None, [txin], [txout])
    tx.hash()

    return tx


def new_utxo_transaction(wallet, to, amount, utxoset):
    inputs = []   #
    outputs = []

    pass


