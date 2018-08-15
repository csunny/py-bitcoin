#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/10 
"""


class MQueue:
    """
    实现一个队列
    """

    def __init__(self):
        self.queue = []

    def append(self, q):
        self.queue.append(q)

    def pop(self):
        """
        先进先出
        :return:
        """
        q = self.queue[0]
        self.queue = self.queue[1:]
        return q

    @property
    def empty(self):
        return len(self.queue) == 0


class MStack:
    """
    实现一个栈
    """

    def __init__(self):
        self.stack = []

    def append(self, q):
        self.stack.append(q)

    def pop(self):
        q = self.stack[-1]
        self.stack = self.stack[0:len(self.stack) - 1]

        return q

    @property
    def empty(self):
        return len(self.stack) == 0


def bfs(n, graph):
    """
    从一个顶点出发，对图进行广度优先遍历
    :param n:
    :return:
    """
    visited = {}  # 用来存储被访问过的顶点

    q = MQueue()

    q.append(n)

    while not q.empty:
        node = q.pop()

        if not visited.get(node):
            visited[node] = True

        near = graph[node]

        for i in near:
            if not visited.get(i):
                q.append(i)
                visited[i] = True

        print(node)


def dfs(n, graph):
    """
    从一个顶点出发，对图进行深度优先遍历
    :param n:
    :param graph:
    :return:
    """
    visited = dict()
    s = MStack()
    s.append(n)

    while not s.empty:
        node = s.pop()

        if not visited.get(node):
            visited[node] = True

            print(" dfs visiting ...", node)
            near = graph[node]
            for i in near:
                s.append(i)

                if not visited.get(node):
                    visited[node] = True


if __name__ == '__main__':
    graph = dict()

    graph["A"] = ['B', 'C', 'D']
    graph["B"] = ['A', 'E']
    graph["C"] = ['A', 'E']
    graph['D'] = ["A"]
    graph["E"] = ['B', 'C', 'F']
    graph['F'] = ['E']

    # for k, v in graph.items():
    #     print(k, '->', v)

    dfs('A', graph)
