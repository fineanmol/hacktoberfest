#include<iostream>
#include<vector>
using namespace std;
void ratinmaze(int row, int col, int n, vector<vector<int> > &m, string ans,vector<string> &res)
{
    if(row < 0 || row>=n ||col < 0 || col>=n || m[row][col]==0)
    {
        return;
    }//Condition
    if(row==n-1 && col==n-1)
    {
        res.push_back(ans); //Base Case
    }
    m[row][col]=0;
    ratinmaze(row+1, col, n, m, ans+"D", res);
    ratinmaze(row-1, col, n, m, ans+"U", res);
    ratinmaze(row, col-1, n, m, ans+"L", res);
    ratinmaze(row, col+1, n, m, ans+"R", res);
    m[row][col]=1;

}
vector<string> findpath(vector<vector<int> > &m, int n)
{
    string ans = "";
    vector<string> res;
    ratinmaze(0,0,n,m,ans,res);
    sort(res.begin(), res.end());
    return res;
}
/*
Input:
N = 4 N*N (Matrix)
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.
*/
