#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    int a = n-1;
    int b = 1;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(j<=a){
                cout << " " ;
            }
            else{
                cout << b;
                b++;
            }
        }
        cout << endl;
        a--;
        
    }
}