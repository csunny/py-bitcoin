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


class Kruskal:
    """
    kruskal 算法python 实现  (最小生成树)
    """

    def __init__(self):
        self.parent = dict()
        self.rank = dict()

    def make_set(self, vertice):
        self.parent[vertice] = vertice
        self.rank[vertice] = 0

    def find(self, vertice):
        if self.parent[vertice] != vertice:
            self.parent[vertice] = self.find(self.parent[vertice])
        return self.parent[vertice]

    def union(self, vertive_one, vertive_two):
        root_one = self.find(vertive_one)
        root_two = self.find(vertive_two)

        if root_one != root_two:
            if self.rank[root_one] > self.rank[root_two]:
                self.parent[root_two] = root_one
            else:
                self.parent[root_one] = root_two
            if self.rank[root_one] == self.rank[root_two]:
                self.rank[root_two] += 1

    def kruskal(self, g):
        for vertive in g['vertices']:
            self.make_set(vertive)
            minimum_spinning_tree = set()

            edges = sorted(g["edges"])

        for edge in edges:
            weight, vertice_one, vertice_two = edge
            if self.find(vertice_one) != self.find(vertice_two):
                self.union(vertice_one, vertice_two)
                minimum_spinning_tree.add(edge)

        print(sum(i[0] for i in minimum_spinning_tree))
        return sorted(minimum_spinning_tree)


if __name__ == '__main__':
    # graph = dict()
    #
    # graph["A"] = ['B', 'C', 'D']
    # graph["B"] = ['A', 'E']
    # graph["C"] = ['A', 'E']
    # graph['D'] = ["A"]
    # graph["E"] = ['B', 'C', 'F']
    # graph['F'] = ['E']
    #
    # # for k, v in graph.items():
    # #     print(k, '->', v)
    #
    # dfs('A', graph)

    g = {
        "vertices": ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        "edges": [
            (7, 'A', 'B'),
            (5, 'A', 'D'),
            (7, 'B', 'A'),
            (8, 'B', 'C'),
            (9, 'B', 'D'),
            (7, 'B', 'E'),
            (8, 'C', 'B'),
            (5, 'C', 'E'),
            (5, 'D', 'A'),
            (9, 'D', 'B'),
            (7, 'D', 'E'),
            (6, 'D', 'F'),
            (7, 'E', 'B'),
            (5, 'E', 'C'),
            (15, 'E', 'D'),
            (8, 'E', 'F'),
            (9, 'E', 'G'),
            (6, 'F', 'D'),
            (8, 'F', 'E'),
            (11, 'F', 'G'),
            (9, 'G', 'E'),
            (11, 'G', 'F')
        ]
    }

    k = Kruskal()
    print(k.kruskal(g))
