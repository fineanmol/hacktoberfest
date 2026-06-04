#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    // for(int i=1;i<=n;i++){
    //     for(int j=1;j<=n;j++){
    //         cout << j << " ";
    //     }
    //     cout << endl;
    //  }

    int a=n;

    while(a--){
        int i=1;
        while(i<=n){
            cout << i << " ";
            i++;
        }
        cout << endl;
    }
}