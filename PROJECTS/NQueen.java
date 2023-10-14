package PROJECTS;

import java.util.ArrayList;
import java.util.List;

public class NQueen {

    public void solve(int c,int n,int lC[],int lB[],int uB[],char board[][],List<List<String>> ans){

        if(c==n){
            ans.add(create(board));
            return;
        }

        for(int r = 0;r<n;r++){

            if(lC[r]==0 && lB[c+r]==0 && uB[n-1+c-r]==0){

                lC[r] = 1;
                lB[c+r] = 1;
                uB[n-1+c-r] = 1;

                board[r][c] = 'Q';
                solve(c+1,n,lC,lB,uB,board,ans);
                board[r][c] = '.';

                lC[r] = 0;
                lB[c+r] = 0;
                uB[n-1+c-r] = 0;

            }

        }
    }

    public List<String> create(char board[][]){

        List<String> ds = new ArrayList<>();

        for(char r[] : board){
            String s = "";
           for(char c : r) s+=c;
           ds.add(s);
        }

        return ds;
    }
    public List<List<String>> solveNQueens(int n) {
        
        List<List<String>> ans = new ArrayList<>();

        char board[][] = new char[n][n];

        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++) board[i][j] = '.';
        }
        
        int lC[] =  new int[n];
        int lB[] = new int[2*n-1];
        int uB[] = new int[2*n-1];

        solve(0,n,lC,lB,uB,board,ans);

        return ans;
    }
}
    

