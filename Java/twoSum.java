import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target){
        int[] ans = new int[2];
        for(int i = 0; i < nums.length; i++){
            for(int j = 0; j < nums.length; j++){
                if(i != j){
                    if(nums[i] + nums[j] == target){
                        ans[0] = j;
                        ans[1] = i;
                        break;
                    }
                }
            }
        }
        return ans;
    }
}