#!/usr/bin/env python3
# -*- coding:utf-8

"""
This file is created By magic at 18-8-5

"""


# todo need to impletement dag

def build_dag():
    graph = dict()

    graph["start"] = {
        "a": 6,
        "b": 2
    }

    graph["a"] = {
        "fin": 1
    }

    graph["b"] = {
        "a": 3,
        "fin": 5
    }

    graph["fin"] = {}
    return graph


def dag(graph):
    infinity = float('inf')

    costs = {
        "a": 6,
        "b": 2,
        "fin": infinity
    }

    parents = {
        "a": "start",
        "b": "start",
        "fin": None
    }

    processed = []

    node = find_lowest_cost_node(costs, processed)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return costs


def find_lowest_cost_node(costs, processed):
    """

    :param costs:
    :return:
    """
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def main():
    pass


if __name__ == '__main__':
    g = build_dag()
    costs = dag(g)
    print(costs)

