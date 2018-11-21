#!/usr/bin/env python
import math

# a heap is represented by a n+1 length array, where the first element starts at 1
class Heap:
    # allows an initialization of O(n) time given n elements
    def __init__(self, arr):
        self.heap = [0] + arr # first el is dummy el
        for i in range(len(arr)-1, 0, -1):
            self.heapify(i)

    def heapify(self, i):
        # is it a leaf node?
        if i*2 >= len(self.heap):
            return
        root = self.heap[i]
        left = i*2
        right = (i*2) + 1

        leftVal = self.heap[left].val
        if right > len(self.heap)-1:
            rightVal = float('inf')
        else:
            rightVal = self.heap[right].val
        if root.val > min(leftVal, rightVal):
            # we need to to a swap
            if leftVal < rightVal:
                # swap with left
                self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
                self.heapify(i*2)
            else:
                # swap with right
                self.heap[i], self.heap[i*2 + 1] = self.heap[i*2 + 1], self.heap[i]
                self.heapify((i*2)+1)

    def heapifyUp(self, i):
        if i == 1:
            return
        if self.heap[i/2] > self.heap[i]:
            self.heap[i], self.heap[i/2] = self.heap[i/2], self.heap[i]
            self.heapifyUp(i/2)

    def insert(self, edge):
        self.heap.append(edge)
        self.heapifyUp(len(self.heap)-1)

    # pops off the top and reheaps
    def extractMin(self):
        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.heapify(1)
        return root

    def __str__(self):
        output = ""
        for a in self.heap[1:]:
            output += str(a.val) + ","
        return output

# undirected edge
class Edge:
    def __init__(self, u, v, val):
        self.u = u
        self.v = v
        self.val = val

    def __str__(self):
        return "({}, {}) cost: {}".format(self.u, self.v, self.val)

    def __lt__(self, other):
        return self.val < other.val

    def key(self):
        return self.val


# preliminary parsing
f = open("edges.txt", "r")
numV = int(f.readline().split(" ")[0])

edges = []
for line in f:
    [u, v, cost] = line.split(" ")
    u = int(u)
    v = int(v)
    cost = int(cost)
    edge = Edge(u, v, cost)
    edges.append(edge)


# X[v] true if vertex v has been selected, false otherwise.
X = [False]*(numV+1)

heap = Heap(edges) # n time

X_card = 2 # how many verticies are in X?
e = heap.extractMin()
min_span_tree_cost = e.val
X[e.u] = True
X[e.v] = True
tmp_edges = []
while X_card < numV:
    e = heap.extractMin() # extract the next minimal edge
    if X[e.u] != X[e.v]:
        X[e.u] = True
        X[e.v] = True
        X_card += 1
        min_span_tree_cost += e.val
        for edge in tmp_edges:
            heap.insert(edge)
        tmp_edges = []
    else:
        tmp_edges.append(e)

print "The minimum spanning tree cost is:", min_span_tree_cost
