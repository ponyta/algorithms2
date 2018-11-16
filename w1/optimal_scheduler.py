#!/usr/bin/env python

class Job:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        self.value = weight/float(length)

    def __str__(self):
        return "w: {}, l: {}, val: {}".format(self.weight, self.length, self.value)

    def __lt__(self, other):
        return self.value < other.value

f = open("jobs.txt", "r")
numJobs = int(f.readline())
jobs = []
for line in f:
    [weight, length] = line.split(" ")
    weight = int(weight)
    length = int(length)
    jobs.append(Job(weight, length))

jobs.sort(reverse=True) # our schedule!

time = 0
cost = 0
for j in jobs:
    time += j.length
    cost += time * j.weight

print "The cost is:", cost
