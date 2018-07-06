#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/6/30 
This module is merkletree implement
"""

import hashlib


class MerkleTree:
    """
    - doc  Merkle tree
    """

    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("data must be a bytes list")

        self.data = data
        self.nodes = []
        self.root = None

    def new_tree(self):

        if len(self.data) % 2 != 0:
            self.data.append(self.data[-1])

        for d in self.data:

            if isinstance(d, bytes) or isinstance(d, bytearray):

                node = MerkleNode(None, None, d)
                node.new_node()
                self.nodes.append(node)
            else:
                raise TypeError("数据类型错误！")

        for i in range(int(len(self.data)/2)):
            new_level = []

            for j in range(0, len(self.nodes), 2):
                node = MerkleNode(self.nodes[j], self.nodes[j + 1], b'')
                node.new_node()
                new_level.append(node)
            self.nodes = new_level

        self.root = self.nodes[0]


class MerkleNode:
    """
    - doc
    """

    def __init__(self, left, right, data):
        self.Left = left
        self.Right = right

        if isinstance(data, bytes) or isinstance(data, bytearray):
            self.data = data
        else:
            raise TypeError("data 不是byte类型!")

    def new_node(self):
        if not self.Left and not self.Right:
            hash_value = hashlib.sha256(bytes(self.data)).hexdigest()
            self.data = hash_value
        else:
            prehash = self.Left.data + self.Right.data
            hash_value = hashlib.sha256(prehash.encode()).hexdigest()
            self.data = hash_value
