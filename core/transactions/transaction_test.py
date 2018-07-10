#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/10 
"""

from core.transactions.transaction import Transaction, new_coinbase_tx


if __name__ == '__main__':
    to = "1KX2LcZeMf4v4JB5KNFD6HKjzckj4n1BhE"

    tx = new_coinbase_tx(to)

    print(tx.serialize())
