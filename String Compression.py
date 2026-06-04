from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        # Initialize the memoization cache
        @lru_cache(None)
        def dp(index, last, last_count, k):
            # Base case: If we have reached the end of the string
            if index == len(s):
                return 0
            
            # Case 1: Delete the current character
            delete_cost = dp(index + 1, last, last_count, k - 1) if k > 0 else float('inf')
            
            # Case 2: Keep the current character
            if s[index] == last:
                # If the current character is the same as the last one
                # Increase the count and calculate the cost
                # The length might increase by 1 when crossing 1, 9, 99, ...
                keep_cost = dp(index + 1, last, last_count + 1, k) + (last_count in [1, 9, 99])
            else:
                # If the current character is different
                # Start a new sequence with this character
                keep_cost = dp(index + 1, s[index], 1, k) + 1
            
            # Return the minimum cost between deleting or keeping the current character
            return min(delete_cost, keep_cost)
        
        # Start the dynamic programming function with the initial parameters
        return dp(0, "", 0, k)

# Example usage:
sol = Solution()
print(sol.getLengthOfOptimalCompression("aaabcccd", 2))  # Output should be 4 for this input
