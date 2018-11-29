#!/usr/bin/env python
import sys

f = open("knapsack_big.txt", "r")
knapsack_size, num_items = f.readline().split(" ")
knapsack_size = int(knapsack_size)
num_items = int(num_items)

values = []
weights = []
for line in f:
    value, weight = line.split(" ")
    values.append(int(value))
    weights.append(int(weight))

cache = {}
sys.setrecursionlimit(2010)

def knapsack(x, i):
    if (x, i) in cache:
        return cache[(x, i)]

    if i == 0: # if theres only one item for you to take, then just take it if you can
        return values[i] if weights[i] <= x else 0

    best = knapsack(x, i-1)
    if weights[i] <= x:
        best = max(best, knapsack(x - weights[i], i-1) + values[i])
    cache[(x, i)] = best
    return best

print knapsack(knapsack_size, num_items-1)
f.close()
