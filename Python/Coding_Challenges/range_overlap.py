from time import time


# Given an input list of integer ranges, find and output the ranges that overlap with at least 1 other range.
# Two ranges are considered overlapping even if they only touch on the boundaries.
# For instance, (40, 52) and (52, 60) are considered overlapping because "52" is shared.

# The order of ranges in the output is not important.

# If a range appears more than once in the list, then it is considered an overlap with other instances of the
# same range, hence the range must appear in the output as many times as it does in the input.
# Input 3 illustrates such a case.

# Feel free to define your own data structures.

# The code should be maintainable, reusable and well tested.

# Examples

Input1 = [(1, 10), (15, 20), (101, 110),]

# Output 1: []

Input2 =  [(1, 10), (15, 20), (101, 110), (18, 22), ]

# Output 2: [(15, 20),(18, 22),]

Input3 = [(1, 10), (15, 20), (101, 110),(1, 10), (105, 120),]


# Output 3:[   (1, 10), (1, 10), (1, 10),  (101, 110),  (105, 120),]

Input4= [(1, 10), (15, 20),  (101, 110),  (18, 30), (27, 35), ]

# Output 4: [ (15, 20), (18, 30),  (27, 35), ]

Input5= [ (5, 10), (301, 400), (180, 200), (100, 300), (120, 150), (160, 170),(195, 220),]

#Output 5:
# [ (180, 200), (100, 300), (120, 150), (160, 170), (195, 220),]


def main(t1, t2):
    rs = t1[0] <= t2[1] and t2[0] <= t1[1]
    return rs

def old_approach(lst):
    length = len(lst)
    rs = []
    for i in range(0, length):
        for j in range(i+1, length):
            if main(lst[i], lst[j]):
                if lst[i] not in rs:
                    rs.append(lst[i])
                if lst[j] not in rs:
                    rs.append(lst[j])
    print(rs)

old_approach(Input5)
old_approach(Input2)
old_approach(Input1)

#Below is new approach::
from itertools import combinations


def new_approach(lst):
    rs = []
    for i, j in combinations(range(0, len(lst)), 2):
        if main(lst[i], lst[j]):
            if lst[i] not in rs:
                rs.append(lst[i])
            if lst[j] not in rs:
                rs.append(lst[j])
    print(rs)

new_approach(Input5)
new_approach(Input1)
new_approach(Input2)