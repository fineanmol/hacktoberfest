def mergeSort(ar_list):
  if len(ar_list) > 1:
  mid = len(ar_list) // 2
  left = ar_list[:mid]
  right = ar_list[mid:]
  # Recursive call on each half
   mergeSort(left)
   mergeSort(right)
  # Two iterators for traversing the left and right half
    i = 0
    j = 0
  # Iterator for the main list
     k = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
    # The value from the left half has been used
    ar_list[k] = left[i]
    # Move the iterator forward
    i += 1
    else:
      ar_list[k] = right[j]
      j += 1
      k += 1
    # For all the remaining values
     while i < len(left):
     ar_list[k] = left[i]
      i += 1
      k +=1
   while j < len(right):
   ar_list[k]=right[j]
   j += 1
   k += 1
ar_list = [12, 7, 2, 9, 4, 15, 5]
mergeSort(ar_list)
print(ar_list)
