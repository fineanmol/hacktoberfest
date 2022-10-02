# Remove all but the first occurrence of duplicate elements in a list.
def unique_elements(lst):
    start = 0
    slide = start + 1
    length = len(lst)
    while start < length-1:
        if lst[start] == lst[slide]:
            lst.pop(slide)
            start = 0
            slide = start + 1
            length = len(lst)
            continue
        slide += 1
        if slide == length:
            start += 1
            slide = start + 1
    return lst


l1 = [10, 15, 20, 10, 30, 35, 20]
l2 = [40, 40, 40]
l3 = [120, 45, 6, 89, 900, 222, 120, -56, 120]
print(unique_elements(l1))
print(unique_elements(l2))
print(unique_elements(l3))
