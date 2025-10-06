def is_armstrong_number(num):
    num_str = str(num)
    n = len(num_str)
    
    sum_of_powers = 0
    for digit_char in num_str:
        digit = int(digit_char)
        sum_of_powers += digit ** n
        
    return num == sum_of_powers