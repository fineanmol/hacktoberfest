//Program to convert decimal to binary and vise versa
//By D3Falt
#include <bits/stdc++.h>
using namespace std;
int main(){
    cout<<"Enter a Decimal value:";
    int a;
    cin>>a;
    cout<<"The value in Binary would be :"<<bitset<8>(a).to_string()<<endl;
}