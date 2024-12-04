#!/usr/bin/env python3


with open("input", "r") as fh:
    lines = [line.strip() for line in fh.readlines()]

def are_numbers_inc_or_dec(lst):
    inc = None
    def check_list(a, b):
        if inc:
            return a < b
        return a > b

    if lst[0] < lst[1]:
        inc = True
        return all(map(lambda x, y: check_list(x, y), lst, lst[1:]))
    inc = False
    return all(map(lambda x, y: check_list(x, y), lst, lst[1:]))


def are_numbers_safe(lst):
    def check_distance(a,b):
        return abs(a - b) <= 3

    return all(map(lambda x, y: check_distance(x, y), lst, lst[1:]))

safe_reports = 0 

for line in lines:
    list_line = list(map(lambda y: int(y), line.split()))
    if are_numbers_inc_or_dec(list_line) and are_numbers_safe(list_line):
        safe_reports += 1

print(safe_reports)
