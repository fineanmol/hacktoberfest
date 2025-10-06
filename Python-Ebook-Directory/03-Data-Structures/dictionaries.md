# Dictionaries

Dictionaries store key -> value pairs and are great for representing structured data.

```python
person = {"name": "Alice", "age": 30}
print(person["name"])   # Alice
person["city"] = "New York"
print(person.get("city"))
```

Iterating and useful methods:

```python
for key, value in person.items():
    print(key, value)

person.keys()
person.values()
```
