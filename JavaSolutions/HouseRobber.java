class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        return Math.max(robLinear(nums, 0, n - 2), robLinear(nums, 1, n - 1));
    }

    private int robLinear(int[] nums, int start, int end) {
        int prev1 = 0, prev2 = 0;
        for (int i = start; i <= end; i++) {
            int temp = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = temp;
        }
        return prev1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums1 = {2, 7, 9, 3, 1};
        int[] nums2 = {1, 2, 3, 1};
        int[] nums3 = {2, 3, 2};
        System.out.println(s.rob(nums1));
        System.out.println(s.rob(nums2));
        System.out.println(s.rob(nums3));
    }
}
