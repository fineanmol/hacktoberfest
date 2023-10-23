import random

# Generate a random integer between a specified range (inclusive)
random_int = random.randint(1, 100)
print(f"Random Integer: {random_int}")

# Generate a random float between 0 and 1
random_float = random.random()
print(f"Random Float: {random_float}")

# Generate a random float within a specified range
random_float_range = random.uniform(1.0, 10.0)
print(f"Random Float within Range: {random_float_range}")

# Generate a random choice from a list
my_list = [1, 2, 3, 4, 5]
random_choice = random.choice(my_list)
print(f"Random Choice from List: {random_choice}")

# Generate a random sequence (shuffling) from a list
random_sequence = random.sample(my_list, len(my_list))
print(f"Random Sequence from List: {random_sequence}")
