#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/6 
"""
from utils.merkletree import MerkleNode, MerkleTree

if __name__ == "__main__":
    m1 = MerkleNode(None, None, b"Node1")
    m1.new_node()

    m2 = MerkleNode(None, None, b"Node2")
    m2.new_node()

    m3 = MerkleNode(None, None, b"Node3")
    m3.new_node()

    m4 = MerkleNode(None, None, b"Node3")
    m4.new_node()

    m5 = MerkleNode(m1, m2, b'')
    m5.new_node()

    print(m5.Left, m5.Right, m5.data)

    tree = MerkleTree([b'Node1', b'Node2', b'Node3'])
    tree.new_tree()

    print(tree.root.data)




