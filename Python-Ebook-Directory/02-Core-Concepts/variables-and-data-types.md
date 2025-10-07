# Variables and Data Types 📊

> Learn to store and work with different types of information in Python

## 🎯 What are Variables?

Variables are like **labeled boxes** that store information. You can put data in them, change the data, and use it later.

Creating variables (like labeling boxes)
name = "Alice"
age = 25
height = 5.6
is_student = True

text

## 📝 Basic Data Types

### 1. Strings (Text) 📝
Strings hold text - always in quotes
first_name = "John"
last_name = 'Smith' # Single or double quotes both work
message = "Hello, World!"

You can combine strings
full_name = first_name + " " + last_name
print(full_name) # Output: John Smith

text

### 2. Integers (Whole Numbers) 🔢
Integers are whole numbers
age = 18
students_in_class = 30
temperature = -5

Math with integers
total = 10 + 5 # 15
difference = 10 - 3 # 7

text

### 3. Floats (Decimal Numbers) 🔢
Floats have decimal points
price = 19.99
weight = 65.5
pi = 3.14159

Math with floats
total_cost = price * 2 # 39.98

text

### 4. Booleans (True/False) ✅
Booleans are either True or False
is_raining = True
is_sunny = False
has_homework = True

Used for decisions
if is_raining:
print("Take an umbrella!")

text

## 🔍 Checking Data Types

name = "Alice"
age = 25
height = 5.6
is_student = True

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(height)) # <class 'float'>
print(type(is_student)) # <class 'bool'>

text

## 🎮 Try This: Personal Info Program

Get user information
print("📝 Tell me about yourself!")
name = input("What's your name? ")
age = int(input("How old are you? "))
# Variables and Data Types 📊

> Learn to store and work with different types of information in Python

## 🔍 What are Variables?

Variables are like **labeled boxes** that store information. You can put data in them, change the data, and use it later.

Creating variables (like labeling boxes)

```python
name = "Alice"
age = 25
height = 5.6
is_student = True
```

## 🔍 Basic Data Types

### 1. Strings (Text) ✍️
Strings hold text - always in quotes

```python
first_name = "John"
last_name = 'Smith' # Single or double quotes both work
message = "Hello, World!"
```

You can combine strings

```python
full_name = first_name + " " + last_name
print(full_name) # Output: John Smith
```

### 2. Integers (Whole Numbers) 🔢
Integers are whole numbers

```python
age = 18
students_in_class = 30
temperature = -5
```

Math with integers

```python
total = 10 + 5 # 15
difference = 10 - 3 # 7
```

### 3. Floats (Decimal Numbers) 🔢
Floats have decimal points

```python
price = 19.99
weight = 65.5
pi = 3.14159
```

Math with floats

```python
total_cost = price * 2 # 39.98
```

### 4. Booleans (True/False) ✅
Booleans are either True or False

```python
is_raining = True
is_sunny = False
has_homework = True
```

Used for decisions

```python
if is_raining:
	print("Take an umbrella!")
```

## 🔍 Checking Data Types

```python
name = "Alice"
age = 25
height = 5.6
is_student = True

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(height)) # <class 'float'>
print(type(is_student)) # <class 'bool'>
```

## 🎮 Try This: Personal Info Program

Get user information

```python
print("📝 Tell me about yourself!")
name = input("What's your name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you (in feet)? "))
likes_python = input("Do you like Python? (yes/no): ").lower() == "yes"
```

Display the information

```python
print(f"\n👋 Hi {name}!")
print(f"Age: {age} years old")
print(f"Height: {height} feet")
print(f"Likes Python: {likes_python}")
```

Check data types

```python
print(f"\nData types:")
print(f"Name type: {type(name)}")
print(f"Age type: {type(age)}")
print(f"Height type: {type(height)}")
print(f"Likes Python type: {type(likes_python)}")
```

## � Converting Between Types

Converting strings to numbers

```python
age_text = "25"
age_number = int(age_text) # Convert to integer
price_text = "19.99"
price_number = float(price_text) # Convert to float
```

Converting numbers to strings

```python
score = 95
score_text = str(score) # Convert to string
```

Be careful - this will cause an error!

```python
age = int("hello") # Can't convert "hello" to a number
```

## 💡 Variable Naming Rules

** ✅ Good variable names:**
- `user_name` (descriptive)
- `total_score` (clear meaning)
- `is_valid` (boolean naming)

** ❌ Bad variable names:**
- `x` (not descriptive)
- `2name` (can't start with number)
- `user-name` (no dashes allowed)

## 🎯 Key Takeaways

- **Variables store data** for later use
- **Strings** hold text (in quotes)
- **Integers** are whole numbers
- **Floats** are decimal numbers
- **Booleans** are True/False
- Use `type()` to check data types
- Choose **descriptive variable names**

## 🔗 What's Next?

Ready to do math and compare values? Continue to `operators.md` to learn about calculations and comparisons!
``` 