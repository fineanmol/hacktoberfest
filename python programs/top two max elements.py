import array
arr = []
n = int(input("enter size of array : "))
for x in range(n):
    x=int(input("enter element of array : "))
    arr.append(x)
sorted_array = sorted(array.array('i', arr))
for i in range(len(arr)-1, 0, -1):
    if sorted_array[i]!=sorted_array[i-1]:
        print(f"First two largest element of array is {sorted_array[i-1]} and {sorted_array[i]}")
        break 
