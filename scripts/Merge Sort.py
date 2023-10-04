import sys
import time

def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

if len(sys.argv) < 2:
    print("Please input list items as arguments")
    print("Example: ./mergesort.py <item1> [item2] [item3] [item4] ...")
    sys.exit(1)

input_array = [int(arg) for arg in sys.argv[1:]]
sorted_array = mergeSort(input_array)

print("Sorted:")
for item in sorted_array:
    print(item)

print("---")
print("Overall Time:", time.process_time(), "seconds")
