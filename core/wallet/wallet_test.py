#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/8
"""
from core.wallet.wallet import Wallet

if __name__ == "__main__":
    w = Wallet()

    # todo need to test
    # there is something error in th test,
    # sometime the assert is ok, but others not.
    # so,maybe something need to do to find the bug.
    # Mark .
    address = w.get_address()
    valid = w.validate_addr(address)

    print(address)
    assert valid is True





