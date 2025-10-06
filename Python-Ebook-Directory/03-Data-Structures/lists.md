# Lists

Lists hold ordered collections of items and are mutable (you can change them).

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # apple
fruits.append("orange")
fruits[1] = "blueberry"
print(len(fruits))    # 4
```

Common operations:

```python
fruits.pop()          # remove last
fruits.insert(1, "kiwi")
"apple" in fruits    # membership test
```

Exercise: Create `shopping.py` that stores 5 items, removes one, and prints the final list.
