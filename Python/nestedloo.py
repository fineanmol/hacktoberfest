rows = 3
columns = 4

# Nested loop to iterate over rows and columns
for i in range(rows):
    for j in range(columns):
        print(f"({i}, {j})", end=" ")
    print()  # Move to the next line after each row
