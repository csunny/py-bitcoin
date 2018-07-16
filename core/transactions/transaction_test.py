#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/10 
"""

from core.wallet.wallet import Wallet
from core.transactions.transaction import Transaction, new_coinbase_tx


# 首先生成n个备用的地址
def get_address(n):
    wallet = Wallet()

    return [wallet.get_address() for i in range(n)]


# 测试生成coinbase交易
def build_coinbase_tx(to, data=None):
    tx = new_coinbase_tx(to, data) if data else new_coinbase_tx(to)
    return tx


def new_coinbase_test():
    addresses = get_address(10)
    tx = build_coinbase_tx(addresses[0])
    print(tx)


def main():
    new_coinbase_test()


if __name__ == '__main__':
    main()
