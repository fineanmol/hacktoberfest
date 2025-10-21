class Solution {
    public int rob(int[] nums) {
        int prev1 = 0; // max till previous house
        int prev2 = 0; // max till the house before previous

        for (int num : nums) {
            int temp = Math.max(prev1, prev2 + num);
            prev2 = prev1;
            prev1 = temp;
        }

        return prev1;
    }
}
