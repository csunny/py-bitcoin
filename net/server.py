#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/11 
"""
import json
from flask import Flask

app = Flask(__name__)

from core.blockchain.block import Block
from core.blockchain.blockchain import BlockChain


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/add/block')
def add_block():
    b = Block()
    b.new_block("Magic", "")
    block = b.block
    return json.dumps(block)


@app.route('/blockchain')
def blockchain():
    bc = BlockChain()

    blocks = bc.print_blockchain()

    return json.dumps(blocks)


if __name__ == "__main__":
    app.run(port=8888, debug=True)
