# Get three integers as input: your floor(a), elevator1 position(b), elevator2 position(c)
a, b, c = map(int, input().split())

# Calculate total distance for elevator 2
# First it goes from c to b, then from b to 1
z = abs(c - b) + (c - 1)

# If you're on floor 1, elevator 1 is always closest
if a == 1:
    print("1")
else:
    # Compare distances:
    # (a-1) is distance for elevator 1 to reach you
    # z is total distance for elevator 2
    if (a - 1) < z:
        print("1")  # Elevator 1 is closer
    elif z < (a - 1):
        print("2")  # Elevator 2 is closer
    else:
        print("3")  # Both elevators take same time