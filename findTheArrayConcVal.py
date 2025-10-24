class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l , r = 0 , len(nums)-1
        K = 0 
        while l < r:
            K += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1

        if l == r:
            K += nums[l]

        return K
