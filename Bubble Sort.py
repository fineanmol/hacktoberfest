import sys
import time

def bubbleSort(array):
    length = len(array)
    count = 0
    for i in range(length):
        swapped = False
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
            count += 1
        if not swapped:
            break
    return array, count

if len(sys.argv) < 2:
    print("Please input list items as arguments")
    print("Example: ./bubblesort.py <item1> [item2] [item3] [item4] ...")
    sys.exit(1)

input_array = [int(arg) for arg in sys.argv[1:]]
sorted_array, count = bubbleSort(input_array)

print("Sorted after", count, "tries.")
print("Sorted:", sorted_array)
print("---")
print("Overall Time:", time.process_time(), "seconds")
