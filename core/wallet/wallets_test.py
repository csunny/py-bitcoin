#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9 
"""
from core.wallet.wallets import Wallets


if __name__ == '__main__':
    ws = Wallets()

    # ws.create_wallet()

    print(ws.wallets)

    # ws.save_to_file()
    #
    # ws.load_from_file()