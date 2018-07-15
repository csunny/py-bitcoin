#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/14 
"""


class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    """
        实现一个二叉搜索树。
    """

    def __init__(self, root=None):
        self.root = root

    def insert(self, key, value):
        """
        插入元素
        :param key:
        :param value:
        :return:
        """
        n = Node(key, value)

        if not self.root:
            self.root = n
        else:
            self._insert_node(self.root, n)

    def _insert_node(self, node, new_node):
        if new_node.key < node.key:
            if not node.left:
                node.left = new_node
            else:
                self._insert_node(node.left, new_node)
        else:
            if not node.right:
                node.right = new_node
            else:
                self._insert_node(node.right, new_node)

    def search(self, key):
        """
        查找元素
        :param key:
        :return:
        """
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return False
        if key < node.key:
            return self._search(node.left, key)

        if key > node.key:
            return self._search(node.right, key)

        return True

    def string(self):
        print("=======================================")
        self._stringify(self.root, 0)
        print("=======================================")

    def _stringify(self, node, level):
        if node:
            format = ""
            for i in range(level):
                format += "                     "

            format += "----["
            level += 1
            self._stringify(node.left, level)

            print(format + "%s\n" % node.key)
            self._stringify(node.right, level)


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(8, "8")
    bst.insert(3, "3")
    bst.insert(1, "1")
    bst.insert(10, "10")
    bst.insert(6, "6")
    bst.insert(4, "4")
    bst.insert(7, "7")
    bst.insert(13, "13")
    bst.insert(14, "14")

    bst.string()
