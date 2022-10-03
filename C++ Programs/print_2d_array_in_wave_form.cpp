#include<iostream>
using namespace std;


void wave_print(int arr[][10], int m, int n){
    for(int j=0; j<n; j++){
        if((j+1)%2!=0){
            for(int i=0; i<m; i++){
                cout<< arr[i][j] << " ";
            }
        }
        else{
            for(int i=m-1; i>=0; i--){
                cout<< arr[i][j] << " ";
            }
        }
    }
}

int main()
{
    int arr[10][10];
    int m,n;
    cin>>m>>n;
    for(int i =0; i<m; i++){
        for(int j=0; j<n; j++){
            cin>>arr[i][j];
        }
    }
    wave_print(arr,m,n);

    return 0;
}