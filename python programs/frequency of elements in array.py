# Python 3 program to count frequencies
# of array items
def countFreq(arr, n):

   # Mark all array elements as not visited
   visited = [False for i in range(n)]

   # Traverse through array elements
   # and count frequencies
   for i in range(n):

     # Skip this element if already
     # processed
     if (visited[i] == True):
        continue

     # Count frequency
     count = 1
     for j in range(i + 1, n, 1):
        if (arr[i] == arr[j]):
          visited[j] = True
          count += 1

     print(arr[i], count)

# Driver Code
arr = [10, 30, 10, 20, 10, 20, 30, 10]
n = len(arr)
countFreq(arr, n)
