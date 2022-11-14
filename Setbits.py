def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

num = int(input("Enter a number: "))
print(f"Setbits of {num} is {countSetBits(num)}")
