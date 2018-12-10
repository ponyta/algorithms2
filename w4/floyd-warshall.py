#!/usr/local/env python3

import math
import time

file = 'g3.txt'

def main():
    with open(file , 'r') as f:
        V, E = f.readline().split(" ")
        V = int(V)
        E = int(E)


        edges = {}
        for line in f:
            u, v, cost = line.split(" ")
            u = int(u)
            v = int(v)
            cost = int(cost)

            if (u, v) in edges:
                edges[(u,v)] = min(edges[(u,v)], cost)
            else:
                edges[(u,v)] = cost

    answer = getShortestShortestPaths(edges, V)
    print(answer)


def getShortestShortestPaths(edges, V):

    shortestPaths = {}

    for v in range(1, V + 1):
        for w in range(1, V + 1):
            if v == w:
                shortestPaths[(v, w)] = 0
            elif (v, w) in edges:
                shortestPaths[(v, w)] = edges[(v,w)]
            else:
                shortestPaths[(v, w)] = math.inf

    time_start = time.time()
    shortestShortestPath = math.inf
    shortestPathsUpdate = {}

    for k in range(1, V + 1):
        print(f'{ 100/V*(k-1) }% of the triple for-loops is done after { (time.time() - time_start)/60 } minutes.')
        for v in range(1, V + 1):
            for w in range(1, V + 1):
                tempShortest = min(shortestPaths[(v,w)], shortestPaths[(v,k)] + shortestPaths[(k,w)])
                if v == w and tempShortest < 0 :
                    return f'Negative cycle in {file}!'
                shortestPathsUpdate[(v,w)] = tempShortest
                shortestShortestPath = min(shortestShortestPath, tempShortest)
        (shortestPaths, shortestPathsUpdate) = (shortestPathsUpdate, {})

    return f'The shortest shortest path in {file} has length {shortestShortestPath}'



if __name__ == "__main__":
    main()

