#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9 
"""

from crypto.hashripe import hash_pub_key


class Input:
    """
    doc  交易输入
    """

    def __init__(self, txid, vout, signature, pub_key):
        self.txid = txid
        self.vout = vout
        self.signature = signature
        self.pubkey = pub_key

    def user_key(self, pub_key_hash):
        locking_hash = hash_pub_key(self.pubkey)

        return locking_hash == pub_key_hash




