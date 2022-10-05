my_string=input("Enter the string : ")

# defining strings in Python and printing them
my_string = "Hello"
print(my_string)


# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

#Accessing string characters in Python
str = 'hactoberfest'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

# Strings are immutable. This means that elements of a string cannot be changed once they have been assigned.

# Python String Operations:
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)

# Iterating through a string
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))

# .lower() is used to convert all the charachters in string to lower
"Hello".lower()

# .upper() is used to convert all the charachters in string to capital
"Hello".upper()

 #.split() is used to split a string in each word
"This will split all words into a list".split()

# .join() joins to form a string
' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])

# Finds the index of 'oc' in the given string
str.find('oc')