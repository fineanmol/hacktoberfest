public class Solution {
    public boolean canJump(int[] nums) {
        int i = 0;
        while(i<nums.length)
        {
            if(nums[i] == 0&&i!=nums.length-1)
            {
                return false;
            }
            int max = Integer.MIN_VALUE;
            int next = i+1;
            for(int j = 1;j<nums[i]+1;j++)
            {
                if(i+j>nums.length-1)
                {
                    return true;
                }
                if(nums[i+j]+j-1>max)
                {
                    max = nums[i+j]+j-1;
                    next = i+j;
                }
            }
            i = next;
        }
        return true;
    }
}