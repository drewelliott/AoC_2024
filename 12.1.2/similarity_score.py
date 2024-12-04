#!/usr/bin/env python3

list1 = []
list2 = []

with open("input", "r") as fh:
    lines = [line.strip() for line in fh.readlines()]

for line in lines:
    split_line = line.split()
    list1.append(int(split_line[0]))
    list2.append(int(split_line[1]))

list1_counts = {element: len([x for x in list1 if x == element]) for element in set(list1)}
list2_counts = {element: len([x for x in list2 if x == element]) for element in set(list2)}

def get_sim_score(num_list, num_counts):
    sim_score = 0
    for num in num_list:
        if num in num_counts:
            sim_score += (num * num_counts[num])

    return sim_score

list1_score = get_sim_score(list1, list2_counts)

print(list1_score)
