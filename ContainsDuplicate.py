# Contains Duplicate

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                return True
        return False


# alternative (worse) o(nlogn) time complexity due to Timsort 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=sorted(nums)
        if len(nums)<1:
            return False

        for i in range(0,len(s)):
            if i+1<len(s) and s[i]==s[i+1]:
                return True
            
        return False
