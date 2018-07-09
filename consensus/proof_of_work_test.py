#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9 
"""

from consensus.proof_of_work import ProofOfWork
from core.blockchain.block import Block


if __name__ == '__main__':
    b = Block()

    genesis_block = b.new_block("Magic test", "")

    pow = ProofOfWork(genesis_block)
    pow.run()