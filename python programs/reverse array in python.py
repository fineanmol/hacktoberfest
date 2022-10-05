#using reverse() method

import array
 
#The original array
new_arr=array.array('i',[2,4,6,8,10,12])
print("Original Array is :",new_arr)
 
#reversing using reverse()
new_arr.reverse()
print("Reversed Array:",new_arr)



#using reversed() method

import array
 
#The original array
new_arr=array.array('i',[10,20,30,40])
print("Original Array is :",new_arr)
 
#reversing using reversed()
res_arr=array.array('i',reversed(new_arr))
print("Resultant Reversed Array:",res_arr



#using flip() method

import numpy as np
 
#The original NumPy array
new_arr=np.array(['A','s','k','P','y','t','h','o','n'])
print("Original Array is :",new_arr)
 
#reversing using flip() Method
res_arr=np.flip(new_arr)
print("Resultant Reversed Array:",res_arr)



#using flipud() method

import numpy as np
 
#The original NumPy array
new_arr=np.array(['A','s','k','P','y','t','h','o','n'])
print("Original Array is :",new_arr)
 
#reversing using flipud() Method
res_arr=np.flipud(new_arr)
print("Resultant Reversed Array:",res_arr)



#using simple slicing

import numpy as np
 
#The original NumPy array
new_arr=np.array([1,3,5,7,9])
print("Original Array is :",new_arr)
 
#reversing using array slicing
res_arr=new_arr[::-1]
print("Resultant Reversed Array:",res_arr)      



      
      
