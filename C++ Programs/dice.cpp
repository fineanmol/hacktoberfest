#include<iostream>

using namespace std;

int main(){
    int k;
    start:
    cout<<"The number of faces on dice : ";
    cin>> k;
    if(k > 0){
        cout <<"The dice shows: "<<(rand() % k) + 1;
    }else{
        cout<<"The number of faces on dice must be greater than 0\n";
        goto start;
    }
}