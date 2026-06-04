def knapsack(weights, values, capacity):
    n = len(weights)
    # Initialize a 2D list to store the maximum values for different capacities
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight exceeds the current capacity, skip it
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Calculate the maximum value either by excluding the item or including it
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # The maximum value is stored in dp[n][capacity]
    max_value = dp[n][capacity]

    # Reconstruct the selected items
    selected_items = []
    w, v = capacity, max_value
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    selected_items.reverse()
    return max_value, selected_items

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, selected_items = knapsack(weights, values, capacity)
print("Maximum Value:", max_value)
print("Selected Items:", selected_items)
