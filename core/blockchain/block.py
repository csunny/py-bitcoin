#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/7 
"""

import time
import hashlib
from consensus.proof_of_work import ProofOfWork


class Block:
    """
    doc  区块

    block = {
        "Timestamp": "",
        "Data": "",
        "PrevBlockHash": "",
        "Hash": "",
        "Nonce": ""
    }
    """

    def __init__(self):
        self.block = dict()

    def new_block(self, data, prev_hash=""):
        block = {
            "TimeStamp": int(time.time()),
            "Data": data,
            "PrevBlockHash": prev_hash,
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
