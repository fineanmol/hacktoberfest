#include<iostream>
using namespace std;

float fun(){
    return 2.34f;
}
int main()
{
    //we use auto keyword when we are unsure of the datatype,
    //c++ automatically gives variable appropriate data type
    auto x=2*9.8 +'a'+10;
    cout<<x;

    auto y=fun();

    //you need not know type of variable,can use auto
    return 0;
}