# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import csv
from collections import Counter

def main():
    instances = []
    new_instance = ['xt','sol','frio','normal','sim']

    with open('base-nb.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            instances.append(row[1:])
    instances.pop(0)

    for x in instances:
        pass
        #print(x)
    l = ['a','b','b']
    print([x for *_,x in instances])
    #print(l)
    print(Counter([x for *_,x in instances]))

if __name__ == '__main__':
    main()
