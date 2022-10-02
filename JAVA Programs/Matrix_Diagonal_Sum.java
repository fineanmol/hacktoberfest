// Leetcode- 1572. Matrix Diagonal Sum
// https://leetcode.com/problems/matrix-diagonal-sum/


class Solution {
    public int diagonalSum(int[][] mat) {
         int sum =0;
        int j=0;
        for(int i=0;i<mat.length;i++){
                sum += mat[i][j];
                sum += mat[i][mat[i].length-1-j];
                j++;
        }

        if(mat.length %2 !=0){
           sum -= mat[mat.length/2][mat.length/2];
        }

        return sum;
    }
}