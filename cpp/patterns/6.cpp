#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    int a;
    for(int i=1;i<=n;i++){
        a=i;
        while(a>=1){
            cout << a << " ";
            a--;
        }
        cout << endl;

    }
}