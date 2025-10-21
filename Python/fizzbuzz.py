def fizzbuzz(n):
    """
    Print numbers from 1 to n, replacing:
    - multiples of 3 with "Fizz"
    - multiples of 5 with "Buzz"
    - multiples of both 3 and 5 with "FizzBuzz"
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    # Run FizzBuzz up to 100
    fizzbuzz(100)
