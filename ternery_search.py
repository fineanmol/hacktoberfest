import math as mt
  
# Function to perform Ternary Search
def ternarySearch(l, r, key, ar):
  
    if (r >= l):
  
        # Find the mid1 and mid2
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3
  
        # Check if key is present at any mid
        if (ar[mid1] == key): 
            return mid1
          
        if (ar[mid2] == key): 
            return mid2
          
        # Since key is not present at mid,
        # check in which region it is present
        # then repeat the Search operation
        # in that region
        if (key < ar[mid1]): 
  
            # The key lies in between l and mid1
            return ternarySearch(l, mid1 - 1, key, ar)
          
        elif (key > ar[mid2]): 
  
            # The key lies in between mid2 and r
            return ternarySearch(mid2 + 1, r, key, ar)
          
        else: 
  
            # The key lies in between mid1 and mid2
            return ternarySearch(mid1 + 1, 
                                 mid2 - 1, key, ar)
          
    # Key not found
    return -1
  
# Driver code
l, r, p = 0, 9, 5
  
# Get the array
# Sort the array if not sorted
ar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
  
# Starting index
l = 0
  
# length of array
r = 9
  
# Checking for 5
  
# Key to be searched in the array
key = 5
  
# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)
  
# Print the result
print("Index of", key, "is", p)
  
# Checking for 50
  
# Key to be searched in the array
key = 50
  
# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)
  
# Print the result
print("Index of", key, "is", p)
