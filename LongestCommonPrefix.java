class Solution {
    public String longestCommonPrefix(String[] strs) {
        int n = strs.length;
        if(n == 0) return "";
        String prefix = strs[0];
        for(int i=1; i<n; i++){
            int j = 0;
            while(j<prefix.length() && j<strs[i].length() && prefix.charAt(j) == strs[i].charAt(j)){
                j++;
            }
            prefix = prefix.substring(0, j);
            if(prefix.length() == 0){ 
                return "";
            }    
        }
        return prefix;
    }
}
