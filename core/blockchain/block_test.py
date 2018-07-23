#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9 
"""

from core.blockchain.block import new_genesis_block
from core.transactions.transaction import new_coinbase_tx


# def test_v0_1_0_version():
#     b = Block()
#
#     b.new_block("Magic", "")
#
#     block = b.block
#
#     new_block = b.new_block("This is a test block", b.block["Hash"])
#
#     assert new_block["PrevBlockHash"] == block["Hash"]


def test_genesis_block():
    coinbase = new_coinbase_tx("7AgP8z7XYyZ2sdnVJ6HCiE5X2reJDf")

    genesis_block = new_genesis_block(coinbase)
    print(genesis_block)

    # we will get the genesis block like this, but there many work need to do, just
    '''
        {
            "TimeStamp":1531800034,
            "Transactions":[
                {
                    "ID":"aaf1cf4ab2675df2df75ce9828f719568aadaec61de1b8cb1217b92ce9e19e2e",
                    "Vin":[
                        {
                            "txid":"",
                            "vout":-1,
                            "signature":null,
                            "pubkey":"Base Info, Magic"
                        }
                    ],
                    "Vout":Array[1]
                },
                {
                    "ID":"aaf1cf4ab2675df2df75ce9828f719568aadaec61de1b8cb1217b92ce9e19e2e",
                    "Vin":[
                        {
                            "txid":"",
                            "vout":-1,
                            "signature":null,
                            "pubkey":"Base Info, Magic"
                        }
                    ],
                    "Vout":[
                        Object{...}
                    ]
                }
            ],
            "PrevBlockHash":"",
            "Nonce":60137,
            "Height":0,
            "Hash":"00004c593701710e45c81238fd9f034f14f1fe523f5760f2e085b4a384e53d66"
        }
    
    '''


if __name__ == '__main__':
    test_genesis_block()
