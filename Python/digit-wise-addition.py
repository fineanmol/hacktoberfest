def add_two_numbers(num1, num2):
    result = 0
    carry = 0
    place = 1

    # Continue until both numbers and carry are 0
    while num1 > 0 or num2 > 0 or carry > 0:
        # Extract last digit from each number
        d1 = num1 % 10
        d2 = num2 % 10

        # Add digits and carry
        total = d1 + d2 + carry

        # Compute new digit and carry
        carry = total // 10
        digit = total % 10

        # Add the digit to result at the correct place
        result = result + digit * place

        # Move to next digits
        place *= 10
        num1 //= 10
        num2 //= 10

    return result
