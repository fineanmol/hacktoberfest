//Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change?

def count_coins(coins, target):
	memo = {}

	def helper(amount, idx):
		# Check if the solution for this subproblem already exists
		if (amount, idx) in memo:
			return memo[(amount, idx)]
		
		# Base case: If the target sum is reached
		if amount == 0:
			return 1
		
		# Base case: If the target sum cannot be reached using remaining coins
		if amount < 0 or idx >= len(coins):
			return 0
		
		# Recursively calculate the number of possible ways using the current coin or skipping it
		memo[(amount, idx)] = helper(amount - coins[idx], idx) + helper(amount, idx + 1)
		return memo[(amount, idx)]
	
	# Call the recursive function with the initial parameters
	return helper(target, 0)

# Test the function
arr = [1, 2, 3]
n = 4
x = count_coins(arr, n)
print(x)
