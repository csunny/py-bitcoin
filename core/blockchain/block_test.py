#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9 
"""

from core.blockchain.block import Block

if __name__ == '__main__':
    b = Block()

    b.new_block("Magic", "")

    block = b.block

    new_block = b.new_block("This is a test block", b.block["Hash"])

    assert new_block["PrevBlockHash"] == block["Hash"]
