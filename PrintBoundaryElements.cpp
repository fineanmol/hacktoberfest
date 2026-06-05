#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,m;
    n=4;
    m=4;
    vector<vector<int>> arr(n);
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            int temp;
            cin>>temp;
            arr[i].push_back(temp);
            //cin>>arr[i][j];
        }
    }

    for(int i=0;i<(m/2);i++){
        int firstRow = i;
        for(int h=i;h<m-i;h++){
            cout<<arr[firstRow][h]<<" ";
        }
        cout<<endl;
        
        int lastColumn = m-i-1;
        for(int k=i+1;k<n-i;k++){
            cout<<arr[k][lastColumn]<<" ";
        }
        cout<<endl;

        int lastRow = n-i;
        for(int g=m-i-2;g>=i;g--){
            cout<<arr[lastRow-1][g]<<" ";
        }
        cout<<endl;

        int firstColumn = i;
        for(int l=n-i-2;l>i;l--){
            cout<<arr[l][firstColumn]<<" ";
        }
        cout<<endl;

    }
}