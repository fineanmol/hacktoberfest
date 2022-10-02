# Write a Python program which takes a list as input and then changes the position of every
# nth value with the (n+1)th in a list.
def position_swap(lst):
    ele1 = 0
    ele2 = ele1 + 1
    while ele2 < len(lst):
        lst[ele1], lst[ele2] = lst[ele2], lst[ele1]
        ele1 = ele2 + 1
        ele2 = ele2 + 2
    return lst


l1 = [10, 20, 30, 40, 50, 60, 70, 110, 222]
l2 = []
print(position_swap(l1))
print(position_swap(l2))
