#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9 
"""

from crypto.base58 import base58decode


class Output:
    """
    doc  交易输出
    """

    def __init__(self, value, pub_key_hash):
        self.value = value
        self.pub_key_hash = pub_key_hash

    def lock(self, address):
        """

        :param address:
        :return:
        """
        pub_key_hash = base58decode(address)
        pub_key_hash = pub_key_hash[1:len(pub_key_hash) - 4]
        self.pub_key_hash = pub_key_hash

    def is_locked(self, pub_key_hash):
        """
        check if the output can be used by the owner of the pubkey
        :return:
        """
        return self.pub_key_hash == pub_key_hash


class Outputs:
    """
    doc 交易输出的集合
    """

    pass


def new_utxo_outputs(value, address):
    txo = Output(value, None)
    txo.lock(address)
    return txo
