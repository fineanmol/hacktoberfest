#include<iostream>
using namespace std;

//if reqd,can use multiple data types in templates
template<class T,class R>

void add(T x,R y){
    cout<<x+y;
}
int main()
{
    add(10,12.9);
    return 0;
}