#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9
This module is order to manage wallet and store wallet to a file.
"""
import json
from core.wallet.wallet import Wallet

walletFile = "wallet.txt"


class Wallets:
    """
    doc

    wallets = {
        "address1": wallet1,
        "address2": wallet2,
    }
    """

    def __init__(self):
        self.wallets = self.load_from_file()
        # self.wallets = dict()

    def create_wallet(self):
        wallet = Wallet()

        address = wallet.get_address()

        self.wallets[address] = wallet
        return address

    def get_addresses(self):
        return [
            address for address, v in self.wallets.items()
        ]

    def get_wallet(self, address):
        return self.wallets[address]

    def load_from_file(self):
        wallets = dict()
        with open(walletFile, 'r') as f:
            for line in f.readlines():
                line_dict = json.loads(line)
                for k, v in line_dict.items():
                    wallets[k] = v

        return wallets

    def save_to_file(self):
        with open(walletFile, 'a+') as f:
            # json.dump(self.wallets, f)
            for k, v in self.wallets.items():
                new_dict = {
                    k: str(v)
                }
                f.write(json.dumps(new_dict) + '\n')

