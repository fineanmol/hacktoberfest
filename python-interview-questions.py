Here are 10 more common Python interview questions that cover a different range of topics, from algorithms and data structures to OOP and core Python features.

##1. Palindrome Check
Problem: Given a string s, return True if it is a palindrome, otherwise return False. A palindrome is a string that reads the same forwards and backward.
code:- 
      def is_palindrome(s):
    """
    Checks if a string is a palindrome using the two-pointer technique.
    This version also cleans the string of non-alphanumeric chars.
    """
    # 1. Clean the string
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    
    # 2. Use two pointers
    left, right = 0, len(cleaned_s) - 1
    
    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left += 1
        right -= 1
        
    return True

# Example
print(f"'A man, a plan, a canal: Panama' is a palindrome: {is_palindrome('A man, a plan, a canal: Panama')}")
print(f"'racecar' is a palindrome: {is_palindrome('racecar')}")
print(f"'hello' is a palindrome: {is_palindrome('hello')}")

# A more "Pythonic" but less efficient way to check
def is_palindrome_simple(s):
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1] # Check against its reverse

print(f"\nSimple check for 'racecar': {is_palindrome_simple('racecar')}")

Concept Tested: This tests string manipulation (cleaning data) and the two-pointer algorithm for an efficient $O(n)$ check. The slice [::-1] is a classic Python trick, but it's $O(n)$ in space (creates a new string), while the two-pointer method is $O(1)$ in space.


## 2. Anagram Check
Problem: Given two strings, s and t, return True if t is an anagram of s, and False otherwise. An anagram is a word formed by rearranging the letters of another.

code:- 
      def is_anagram(s, t):
    """
    Checks if two strings are anagrams using a hash map (dictionary).
    """
    if len(s) != len(t):
        return False
        
    counts = {}
    
    # Count characters in the first string
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        
    # Decrement counts using the second string
    for char in t:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1
        
    return True

# Example
print(f"anagram, nagaram: {is_anagram('anagram', 'nagaram')}") # True
print(f"rat, car: {is_anagram('rat', 'car')}")             # False

# Alternative "Pythonic" way (less efficient but clever)
def is_anagram_sorted(s, t):
    return sorted(s) == sorted(t)

print(f"Sorted check for 'anagram', 'nagaram': {is_anagram_sorted('anagram', 'nagaram')}")

Concept Tested: This tests hash maps (dictionaries) for frequency counting. The sorted() solution is concise but slower ($O(n \log n)$) than the dictionary method ($O(n)$).


## 3. Binary Search
Problem: Given a sorted list of integers nums and an integer target, write a function to search for target in nums. If target exists, return its index. Otherwise, return -1.

code:- 
      def binary_search(nums, target):
    """
    Performs an iterative binary search on a sorted list.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # Target is in the right half
            left = mid + 1
        else:
            # Target is in the left half
            right = mid - 1
            
    return -1 # Target not found

# Example
nums = [-1, 0, 3, 5, 9, 12]
print(f"Index of 9: {binary_search(nums, 9)}")  # Output: 4
print(f"Index of 2: {binary_search(nums, 2)}")  # Output: -1

Concept Tested: This is a fundamental divide-and-conquer algorithm. It tests your ability to manage pointers (left, right, mid) and understand logarithmic time complexity ($O(\log n)$).

## 4. Find K-th Largest Element
Problem: Given an integer list nums and an integer k, return the $k$-th largest element in the list.

code:- 
      def find_kth_largest(nums, k):
    """
    Finds the k-th largest element by sorting.
    This is the most straightforward, "good enough" solution.
    """
    # Sort the list in descending order
    nums.sort(reverse=True)
    
    # The k-th largest is at index k-1
    return nums[k - 1]

# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"The {k}-nd largest element is: {find_kth_largest(nums, k)}") # Output: 5

# Note: A more optimal O(n log k) solution uses a min-heap,
# but the sorting solution (O(n log n)) is often accepted.

Concept Tested: This tests your knowledge of sorting. While a heap (priority queue) is the optimal solution, simply sorting the list and picking the element at the correct index is a common and clear approach.


## 5. OOP: Define a Class
Problem: Define a Python class called Car. The __init__ method should take make, model, and year, and it should also have a method called get_description that returns a string like "2023 Toyota Camry".

code:- 
      class Car:
    """
    A simple class representing a car.
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"New car created: {self.make} {self.model}")

    def get_description(self):
        """Returns a formatted description of the car."""
        return f"{self.year} {self.make} {self.model}"
        
    def __str__(self):
        """Defines the string representation for print()."""
        return f"<Car: {self.year} {self.make}>"

# Example
my_car = Car("Toyota", "Camry", 2023)
print(my_car.get_description()) # Output: 2023 Toyota Camry
print(my_car)                   # Output: <Car: 2023 Toyota>


Concept Tested: This tests fundamental Object-Oriented Programming (OOP):

. class keyword: Defining a class.

. __init__: The constructor method.

. self: The instance variable.

. Instance methods: get_description.

. Magic methods: __str__ (what print() uses).


## 6. Lambda Function for Sorting
Problem: You have a list of tuples, where each tuple is (name, age). Sort this list of people by their age (from youngest to oldest).

code:-
     people = [('Alice', 30), ('Bob', 25), ('Charlie', 35), ('David', 22)]

# Use the 'key' argument in sorted() with a lambda function
sorted_people = sorted(people, key=lambda person: person[1])

print(f"Original: {people}")
print(f"Sorted by age: {sorted_people}")
# Output: [('David', 22), ('Bob', 25), ('Alice', 30), ('Charlie', 35)]

Concept Tested: This tests your understanding of lambda functions (small, anonymous functions) and how they are used as key functions in sorted() or .sort().


## 7. Factorial (Recursive)
Problem: Write a recursive function to calculate the factorial of a non-negative integer n. The factorial (n!) is the product of all positive integers less than or equal to n. (e.g., $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$).

code:-
      def factorial(n):
    """
    Calculates the factorial of n using recursion.
    """
    # Base case: 0! = 1
    if n == 0:
        return 1
    # Recursive step: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example
print(f"5! is: {factorial(5)}") # Output: 120
print(f"0! is: {factorial(0)}") # Output: 1

Concept Tested: This is a classic recursion problem. It tests your ability to define a base case (to stop the recursion) and a recursive step (the function calling itself).


## 8. FizzBuzz
Problem: Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number. For multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

code:- 
     def fizzbuzz():
    """
    Prints the FizzBuzz sequence from 1 to 100.
    """
    for num in range(1, 101):
        # Must check for both first!
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Example (calling the function)
# fizzbuzz() # This will print all 100 lines
print("Running FizzBuzz for 1 to 15:")
for num in range(1, 16): # Just to show a sample
    if num % 15 == 0: print("FizzBuzz")
    elif num % 3 == 0: print("Fizz")
    elif num % 5 == 0: print("Buzz")
    else: print(num)

Concept Tested: This is a "filter" question. It looks simple, but it quickly tests your grasp of if/elif/else logic and order of operations. The trick is to check for the "FizzBuzz" (divisible by 15) condition first.

Here are 10 more common Python interview questions that cover a different range of topics, from algorithms and data structures to OOP and core Python features.## 1. Palindrome CheckProblem: Given a string s, return True if it is a palindrome, otherwise return False. A palindrome is a string that reads the same forwards and backward.Python Code:Pythondef is_palindrome(s):
    """
    Checks if a string is a palindrome using the two-pointer technique.
    This version also cleans the string of non-alphanumeric chars.
    """
    # 1. Clean the string
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    
    # 2. Use two pointers
    left, right = 0, len(cleaned_s) - 1
    
    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left += 1
        right -= 1
        
    return True

# Example
print(f"'A man, a plan, a canal: Panama' is a palindrome: {is_palindrome('A man, a plan, a canal: Panama')}")
print(f"'racecar' is a palindrome: {is_palindrome('racecar')}")
print(f"'hello' is a palindrome: {is_palindrome('hello')}")

# A more "Pythonic" but less efficient way to check
def is_palindrome_simple(s):
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1] # Check against its reverse

print(f"\nSimple check for 'racecar': {is_palindrome_simple('racecar')}")
Concept Tested: This tests string manipulation (cleaning data) and the two-pointer algorithm for an efficient $O(n)$ check. The slice [::-1] is a classic Python trick, but it's $O(n)$ in space (creates a new string), while the two-pointer method is $O(1)$ in space.## 2. Anagram CheckProblem: Given two strings, s and t, return True if t is an anagram of s, and False otherwise. An anagram is a word formed by rearranging the letters of another.Python Code:Pythondef is_anagram(s, t):
    """
    Checks if two strings are anagrams using a hash map (dictionary).
    """
    if len(s) != len(t):
        return False
        
    counts = {}
    
    # Count characters in the first string
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        
    # Decrement counts using the second string
    for char in t:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1
        
    return True

# Example
print(f"anagram, nagaram: {is_anagram('anagram', 'nagaram')}") # True
print(f"rat, car: {is_anagram('rat', 'car')}")             # False

# Alternative "Pythonic" way (less efficient but clever)
def is_anagram_sorted(s, t):
    return sorted(s) == sorted(t)

print(f"Sorted check for 'anagram', 'nagaram': {is_anagram_sorted('anagram', 'nagaram')}")
Concept Tested: This tests hash maps (dictionaries) for frequency counting. The sorted() solution is concise but slower ($O(n \log n)$) than the dictionary method ($O(n)$).## 3. Binary SearchProblem: Given a sorted list of integers nums and an integer target, write a function to search for target in nums. If target exists, return its index. Otherwise, return -1.Python Code:Pythondef binary_search(nums, target):
    """
    Performs an iterative binary search on a sorted list.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # Target is in the right half
            left = mid + 1
        else:
            # Target is in the left half
            right = mid - 1
            
    return -1 # Target not found

# Example
nums = [-1, 0, 3, 5, 9, 12]
print(f"Index of 9: {binary_search(nums, 9)}")  # Output: 4
print(f"Index of 2: {binary_search(nums, 2)}")  # Output: -1
Concept Tested: This is a fundamental divide-and-conquer algorithm. It tests your ability to manage pointers (left, right, mid) and understand logarithmic time complexity ($O(\log n)$).## 4. Find K-th Largest ElementProblem: Given an integer list nums and an integer k, return the $k$-th largest element in the list.Python Code:Pythondef find_kth_largest(nums, k):
    """
    Finds the k-th largest element by sorting.
    This is the most straightforward, "good enough" solution.
    """
    # Sort the list in descending order
    nums.sort(reverse=True)
    
    # The k-th largest is at index k-1
    return nums[k - 1]

# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"The {k}-nd largest element is: {find_kth_largest(nums, k)}") # Output: 5

# Note: A more optimal O(n log k) solution uses a min-heap,
# but the sorting solution (O(n log n)) is often accepted.
Concept Tested: This tests your knowledge of sorting. While a heap (priority queue) is the optimal solution, simply sorting the list and picking the element at the correct index is a common and clear approach.## 5. OOP: Define a ClassProblem: Define a Python class called Car. The __init__ method should take make, model, and year, and it should also have a method called get_description that returns a string like "2023 Toyota Camry".Python Code:Pythonclass Car:
    """
    A simple class representing a car.
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"New car created: {self.make} {self.model}")

    def get_description(self):
        """Returns a formatted description of the car."""
        return f"{self.year} {self.make} {self.model}"
        
    def __str__(self):
        """Defines the string representation for print()."""
        return f"<Car: {self.year} {self.make}>"

# Example
my_car = Car("Toyota", "Camry", 2023)
print(my_car.get_description()) # Output: 2023 Toyota Camry
print(my_car)                   # Output: <Car: 2023 Toyota>
Concept Tested: This tests fundamental Object-Oriented Programming (OOP):class keyword: Defining a class.__init__: The constructor method.self: The instance variable.Instance methods: get_description.Magic methods: __str__ (what print() uses).## 6. Lambda Function for SortingProblem: You have a list of tuples, where each tuple is (name, age). Sort this list of people by their age (from youngest to oldest).Python Code:Pythonpeople = [('Alice', 30), ('Bob', 25), ('Charlie', 35), ('David', 22)]

# Use the 'key' argument in sorted() with a lambda function
sorted_people = sorted(people, key=lambda person: person[1])

print(f"Original: {people}")
print(f"Sorted by age: {sorted_people}")
# Output: [('David', 22), ('Bob', 25), ('Alice', 30), ('Charlie', 35)]
Concept Tested: This tests your understanding of lambda functions (small, anonymous functions) and how they are used as key functions in sorted() or .sort().## 7. Factorial (Recursive)Problem: Write a recursive function to calculate the factorial of a non-negative integer n. The factorial (n!) is the product of all positive integers less than or equal to n. (e.g., $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$).Python Code:Pythondef factorial(n):
    """
    Calculates the factorial of n using recursion.
    """
    # Base case: 0! = 1
    if n == 0:
        return 1
    # Recursive step: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example
print(f"5! is: {factorial(5)}") # Output: 120
print(f"0! is: {factorial(0)}") # Output: 1
Concept Tested: This is a classic recursion problem. It tests your ability to define a base case (to stop the recursion) and a recursive step (the function calling itself).1## 8. FizzBuzz2Problem: Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number. For multiples of five, print "Buzz". For numbers whic3h are multiples of both three and five, print "FizzBuzz".Python Code:Pythondef fizzbuzz():
    """
    Prints the FizzBuzz sequence from 1 to 100.
    """
    for num in range(1, 101):
        # Must check for both first!
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Example (calling the function)
# fizzbuzz() # This will print all 100 lines
print("Running FizzBuzz for 1 to 15:")
for num in range(1, 16): # Just to show a sample
    if num % 15 == 0: print("FizzBuzz")
    elif num % 3 == 0: print("Fizz")
    elif num % 5 == 0: print("Buzz")
    else: print(num)
Concept Tested: This is a "filter" question. It looks simple, but it quickly tests your grasp of if/elif/else logic and order of operations. The trick is to check for the "FizzBuzz" (divisible by 15) condition first.


## 9. File I/O: Word Count
Problem: Write a function that reads a text file (example.txt) and returns a dictionary where the keys are the words and the values are their frequencies.

code:- def count_words(filename="example.txt"):
    """
    Reads a file, cleans it, and counts word frequencies.
    """
    # First, create a dummy file to read
    with open(filename, "w") as f:
        f.write("hello world\n")
        f.write("this is a test\n")
        f.write("hello again\n")

    word_counts = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                # Basic cleaning: remove punctuation, lower case, split
                cleaned_line = line.strip().lower()
                words = cleaned_line.split()
                
                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1
                    
        return word_counts

    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

# Example
print(f"Word counts: {count_words()}")
# Output: {'hello': 2, 'world': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1, 'again': 1}

Concept Tested: This tests file handling (with open(...)), string manipulation (.strip(), .lower(), .split()), and dictionary manipulation (.get() for safe incrementing).


## 10. Implement a Queue using Stacks
Problem: Implement a Queue class (First-In, First-Out) using only two Stack (Last-In, First-Out) data structures. The queue should support enqueue (add item) and dequeue (remove item).

code:- 
     class QueueWithTwoStacks:
    """
    Implements a FIFO Queue using two LIFO Stacks.
    """
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        """Adds an item to the end of the queue."""
        self.in_stack.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Removes an item from the front of the queue."""
        if not self.out_stack:
            # If out_stack is empty, transfer from in_stack
            if not self.in_stack:
                return "Queue is empty"
            
            while self.in_stack:
                # Pop from in_stack and append to out_stack
                # This reverses the order
                self.out_stack.append(self.in_stack.pop())
                
        # Now, the front of the queue is at the top of out_stack
        item = self.out_stack.pop()
        print(f"Dequeued: {item}")
        return item

# Example
q = QueueWithTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
# in_stack: [1, 2, 3]
# out_stack: []

print(q.dequeue()) # Dequeued: 1
# in_stack: []
# out_stack: [3, 2] (1 is popped)

q.enqueue(4)
# in_stack: [4]
# out_stack: [3, 2]

print(q.dequeue()) # Dequeued: 2
print(q.dequeue()) # Dequeued: 3
print(q.dequeue()) # Dequeued: 4

Concept Tested: This is a classic data structure puzzle. It tests your understanding of how stacks and queues work and your ability to solve problems by moving data between structures. The "trick" is to use the second stack to reverse the order of the first stack.
