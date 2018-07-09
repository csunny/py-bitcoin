#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9 
"""

from core.blockchain.blockchain import  BlockChain


if __name__ == '__main__':
    bc = BlockChain()

    for i in range(10):
        bc.add_block("Magic Test %d" %i)

    bc.print_blockchain()

