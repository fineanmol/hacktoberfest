class Solution {
    public int maxSubArray(int[] nums) {
        //base case
        if(nums.length == 1){
            return nums[0];
        }
        
        //comparing sums of an element and the next element
        int f = nums[0];
        int max = nums[0];
        
        //max = max of all largest numbers
        for(int i=1 ; i<nums.length ; i++){
            f = Math.max(f + nums[i], nums[i]);
            max = Math.max(max, f);
        }
        
        return max;
    }
}
