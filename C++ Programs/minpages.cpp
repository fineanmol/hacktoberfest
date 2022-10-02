#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function template in C++

class Solution 
{
    public:
    int isvalid(int A[],int N,int M,int mid){
        int stu=1,sum=0;
        for(int i=0;i<N;i++){
            sum+=A[i];
            if(sum>mid){stu++; sum=A[i];}
            if(stu>M)return 0;
        }
        return 1;
    }
    //Function to find minimum number of pages.
    int findPages(int A[], int N, int M) 
    {
        //code here
        int l=*max_element(A,A+N),h=0,mid,res=-1;
        for(int i=0;i<N;i++)h+=A[i];
        while(l<=h){
            mid=l+(h-l)/2;
            if(isvalid(A,N,M,mid)){res=mid; h=mid-1;}
            else l=mid+1;
        }
        return res;
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int A[n];
        for(int i=0;i<n;i++){
            cin>>A[i];
        }
        int m;
        cin>>m;
        Solution ob;
        cout << ob.findPages(A, n, m) << endl;
    }
    return 0;
}
