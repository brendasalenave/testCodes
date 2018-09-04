from collections import Counter, defaultdict
from functools import partial
import math, random
import csv
import sys
import pandas as pd

def entropy(class_probabilities):
    """given a list of class probabilities, compute the entropy"""
    return sum(-p * math.log(p, 2) for p in class_probabilities if p)

def class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count
            for count in Counter(labels).values()]

def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets):
    """find the entropy from this partition of data into subsets"""
    total_count = sum(len(subset) for subset in subsets)

    return sum( data_entropy(subset) * len(subset) / total_count
                for subset in subsets )

def group_by(items, key_fn):
    """returns a defaultdict(list), where each input item
    is in the list whose key is key_fn(item)"""
    groups = defaultdict(list)
    for item in items:
        key = key_fn(item)
        groups[key].append(item)
    return groups

def partition_by(inputs, attribute):
    """returns a dict of inputs partitioned by the attribute
    each input is a pair (attribute_dict, label)"""
    return group_by(inputs, lambda x: x[0][attribute])

def partition_entropy_by(inputs,attribute):
    """computes the entropy corresponding to the given partition"""
    partitions = partition_by(inputs, attribute)
    return partition_entropy(partitions.values())

def classify(tree, input):
    """classify the input using the given decision tree"""

    # if this is a leaf node, return its value
    if tree in ['Sim', 'Nao']:
        return tree

    # otherwise find the correct subtree
    attribute, subtree_dict = tree

    subtree_key = input.get(attribute)  # None if input is missing attribute

    if subtree_key not in subtree_dict: # if no subtree for key,
        subtree_key = None              # we'll use the None subtree

    subtree = subtree_dict[subtree_key] # choose the appropriate subtree
    return classify(subtree, input)     # and use it to classify the input

def build_tree_id3(inputs, split_candidates=None):

    # if this is our first pass,
    # all keys of the first input are split candidates
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()

    # count Trues and Falses in the inputs
    num_inputs = len(inputs)
    num_trues = len([label for item, label in inputs if label=='Sim'])
    num_falses = num_inputs - num_trues

    if num_trues == 0:                  # if only Falses are left
        return 'Nao'                    # return a "False" leaf

    if num_falses == 0:                 # if only Trues are left
        return 'Sim'                     # return a "True" leaf

    if not split_candidates:            # if no split candidates left
        return num_trues >= num_falses  # return the majority leaf

    # otherwise, split on the best attribute
    best_attribute = min(split_candidates, key=partial(partition_entropy_by, inputs))

    partitions = partition_by(inputs, best_attribute)
    new_candidates = [a for a in split_candidates
                      if a != best_attribute]

    # recursively build the subtrees
    subtrees = { attribute : build_tree_id3(subset, new_candidates)
                 for attribute, subset in partitions.items() }

    subtrees[None] = num_trues > num_falses # default case

    return (best_attribute, subtrees)

def forest_classify(trees, input):
    votes = [classify(tree, input) for tree in trees]
    vote_counts = Counter(votes)
    return vote_counts.most_common(1)[0][0]

def read_dataset(data):
    inst = []

    with open(data) as f:
        headers = []
        line = csv.DictReader(f,delimiter=';')
        line = list(line)

        for feature in line:
            x = list(feature.items())
            inst.append((dict(x[:-1]),x[-1][1]))

        headers = [i[0] for i in x[:-1]]

    return inst, headers

if __name__ == "__main__":
    instances, headers = read_dataset(sys.argv[1])
    #print(instances)
    for x in instances:
        print(x)

    for key in headers:
        print(key, partition_entropy_by(instances, key))
    print()

    #senior_inputs = [(input, label)
    #                 for input, label in inputs if input["level"] == "Senior"]

    #for key in ['lang', 'tweets', 'phd']:
    #    print(key, partition_entropy_by(senior_inputs, key))
    #print()

    print("building the tree")
    tree = build_tree_id3(instances)
    print(tree)
    """
    print("Junior / Java / tweets / no phd", classify(tree,
        { "level" : "Junior",
          "lang" : "Java",
          "tweets" : "yes",
          "phd" : "no"} ))

    print("Junior / Java / tweets / phd", classify(tree,
        { "level" : "Junior",
                 "lang" : "Java",
                 "tweets" : "yes",
                 "phd" : "yes"} ))

    print("Intern", classify(tree, { "level" : "Intern" } ))
    print("Senior", classify(tree, { "level" : "Senior" } ))"""
