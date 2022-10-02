# Write a Python program to print all sub-lists of a list.
def sub_lists(lst):
    sublists = [[]]
    for i in range(len(lst) + 1):
        for j in range(i):
            sublists.append(lst[j: i])
    return sublists


l1 = [1, 2, 3]
l2 = []
print(sub_lists(l1))
print(sub_lists(l2))
