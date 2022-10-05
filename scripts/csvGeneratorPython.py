#This file generates a CSV file with integer values, you can use it for eg. input for testing your sroting algorithms.

import random as rd; 

minNum = 0;
maxNum = 1000; #maximum number in array
lengthOfItems= 500; #this will generate 500 random numbers. 

file = open("newFile.csv", "a")

for i in range(lengthOfItems):
    file.write(str(str(rd.randint(minNum,maxNum)) + ","))

file.close()
#note - you will have to split first line at "," and convert to int 



