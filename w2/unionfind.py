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
    f = open("clustering1.txt", "r")
    numNodes = int(f.readline())
    # create union find for each vertex
    nodes = [Node(str(i)) for i in range(1, numNodes+1)]

    edges = []
    for l in f:
        [u, v, cost] = l.split(" ")
        u = int(u)
        v = int(v)
        cost = int(cost)
        edges.append(Edge(u, v, cost))
    edges.sort()
    numClusters = numNodes
    for e in edges:
        node1 = nodes[e.u-1]
        node2 = nodes[e.v-1]
        if numClusters <= 4: # we are done
            if node1.find() is not node2.find():
                largestDist = e.cost
                print largestDist
                break
        if node1.find() is not node2.find(): # if they are not in the same cluster
            numClusters -= 1
            node1.union(node2) # union them together

    clusters = set()
    for n in nodes:
        clusters.add(n.find())
    print clusters


main()

nodes = ["sonja", "chun", "max", "michelle"]
nodes = map(lambda x: Node(x), nodes)
nodes[0].union(nodes[1])
nodes[1].union(nodes[2])

for n in nodes:
    print n.find()

print nodes[0].find() is nodes[1].find()
print nodes[2].find() is not nodes[3].find()
