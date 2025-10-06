# Practice - Control Flow

Exercise: Find primes under N.

Task:

- Ask the user for a positive integer N.
- Print all prime numbers less than or equal to N.

Hints:

- Use loops and conditionals.
- Consider the simple trial division algorithm for primes.

Stretch:

- Improve performance by checking up to the square root of each candidate.

---

# Solution

```python
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
primes = [x for x in range(2, n + 1) if is_prime(x)]

print(f"Prime numbers less than or equal to {n}: {primes}")
```
