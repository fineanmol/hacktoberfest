class Solution {
    public int longestValidParentheses(String s) {
        //base case
        if(s.length() <= 1){
            return 0;
        }
        //using dp for longest parenthesis
        int a = 0;
        int dp[] = new int[s.length()];
        
        for (int i=1 ; i<s.length() ; i++) {
            if (s.charAt(i) == ')') {
                if (s.charAt(i-1) == '(') {
                    if(i >= 2){
                        dp[i] = dp[i-2] + 2;
                    }
                    else{
                        dp[i] = 2;
                    }
                } 
                else if (i - dp[i-1] > 0 && s.charAt(i - dp[i-1] - 1) == '(') {
                    if(i-dp[i-1] >= 2){
                        dp[i] = dp[i-1] + dp[i - dp[i-1] -2] + 2;
                    }
                    else{
                        dp[i] = dp[i-1] + 2;
                    }
                }
                a = Math.max(a, dp[i]);
            }
        }
        return a;
    }
}
