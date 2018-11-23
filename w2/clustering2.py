#!/usr/bin/env python

# node for union find
class Node:
    def __init__(self, data):
        self.parent = self
        self.data = data
        self.rank = 1

    def find(self):
        itr = self
        # no path compression yet
        if itr.parent == itr:
            return itr
        # set your parent directly to the root
        root = itr.parent.find()
        self.parent = root
        return root

    # union two nodes self and other together
    def union(self, other):
        p1 = self.find()
        p2 = other.find()
        if p1.rank < p2.rank:
            p1.parent = p2
            p2.rank += p1.rank
        else:
            p2.parent = p1
            p1.rank += p2.rank

    def __str__(self):
        return "(" + str(self.data) + ", " + str(self.rank) + ")"

    def __repr__(self):
        return "(" + str(self.data) + ", " + str(self.rank) + ")"

class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return "(" + str(self.u) + "-" + str(self.v) + ": " + str(self.cost) + ")"

    def __str__(self):
        return "(" + str(self.u) + "-" + str(self.v) + ": " + str(self.cost) + ")"

def main():
    f = open("clustering_big.txt", "r")
    numNodes, numDigits = f.readline().split(" ")
    numNodes = int(numNodes)
    numDigits = int(numDigits)
    nodes = {}
    k = numNodes # num of clusters
    for l in f:
        bits = "".join(l.split(" ")[:-1])
        if bits in nodes:
            # we have a node with distance 0
            # might as well "union" (eliminate) it now
            k -= 1
        nodes[bits] = Node(bits)

    # eliminate all 1-distance edges
    for attribute in [one_distance, two_distance]:
        for bitstr, node in nodes.iteritems():
            for bitstr2 in attribute(bitstr):
                if bitstr2 in nodes:
                    node2 = nodes[bitstr2]
                    if node.find() != node2.find():
                        node.union(node2)
                        k -= 1
    print k



def two_distance(bitstr):
    lst = []
    for i in range(len(bitstr)-1):
        for j in range(i+1, len(bitstr)):
            newstr = (bitstr[0:i] + "{}" + bitstr[i+1:j] + "{}" + bitstr[j+1:]).format(str((int(bitstr[i]) + 1)%2), str((int(bitstr[j]) + 1)%2))
            lst.append(newstr)
    return lst

def one_distance(bitstr):
    lst = []
    for i in range(len(bitstr)):
        newstr = (bitstr[0:i] + "{}" + bitstr[i+1:]).format(str((int(bitstr[i]) + 1)%2))
        lst.append(newstr)
    return lst

main()
