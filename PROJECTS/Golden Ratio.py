def fibonacci_with_golden_ratio(n):
    if n <= 0:
        return []

    # Define the starting values for F(0) and F(1)
    fibonacci_sequence = [0, 1]

    # Calculate Fibonacci numbers using the golden ratio approximation
    while len(fibonacci_sequence) < n:
        # Calculate the next Fibonacci number using the golden ratio
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)

    return fibonacci_sequence

n = 10  

# Generate and print the Fibonacci sequence
fib_sequence = fibonacci_with_golden_ratio(n)
print(fib_sequence)
