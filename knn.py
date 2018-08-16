# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import csv
import math
from collections import Counter

def manhattan_distance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += (instance1[x] - instance2[x])
        distance = abs(distance)
    return (distance,instance1[-1])

def euclidean_distance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return (round(math.sqrt(distance),3),instance1[-1])

def main():
    k = 1
    instances = []
    new_instance = ['nova',0.3,0.7]
    d = []

    with open('base-knn.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            instances.append(row[1:])

    instances.pop(0)

    for x in instances:
        x = [float(x[0]),float(x[1]),x[2]]
        d.append(euclidean_distance(x,new_instance[1:],2))
        #d.append(manhattan_distance(x,new_instance[1:],2))

    d.sort(key=lambda tup: tup[0])

    get_k = d[:k]
    c = Counter(elem[1] for elem in get_k)
    print(c.most_common(1)[0][0])

if __name__ == '__main__':
    main()
