#!/usr/bin/env python3

list1 = []
list2 = []

with open("input", "r") as fh:
    lines = [line.strip() for line in fh.readlines()]

for line in lines:
    split_line = line.split()
    list1.append(split_line[0])
    list2.append(split_line[1])

list1.sort()
list2.sort()

total_distance = 0

for i, coord in enumerate(list1, start=0):
    diff = abs(int(list1[i]) - int(list2[i]))
    total_distance += diff

print(total_distance)
