# Strings

Strings are sequences of characters. They are written in single or double quotes.

```python
text = "Hello, world!"
print(text[0])        # H
print(text[7:12])     # world
print(text.lower())   # hello, world!
```

Common useful methods:

```python
text.replace("world", "Python")
text.split(",")
text.strip()  # removes surrounding whitespace
```

F-strings make formatting easier:

```python
name = "Alice"
age = 25
print(f"{name} is {age} years old")
```
