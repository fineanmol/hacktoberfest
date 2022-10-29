#include<iostream>
using namespace std;
int main()
{
    //read from right to left

    //int const x and const int x are both same, x is not a ptr
    int x=10;
    const int *p=&x; //ptr to a constant integer
    //not allowed to be modified  ++ *p;
    cout<<x<<endl;
    cout<<*p<<endl;

    //ptr to a constant integer
    int const *q=&x;
    cout<<*q<<endl;
    int y=20;
    p=&y; //you can make the ptr point on sme other data,but u cannot modify that
    // ++(*p); not alloweed

    //constant ptr of type integer
    int * const ptr=&x; //here data is not constant but pointer ptr is constant
    //ptr u cannot modify,once pointing on x u cannot change it to point on something else
    //ptr =&y; not aallowed
    //pointer is locked and not the data

    //const pointer to integer constant
    const int *const k=&x;
    //this ptr cannot be modified to point to any other data member and also cannot modify contents of that member
    //lock on both ,data as well as pointer
    // k=&y; gives error
    //*k=6; gives error
    return 0;
}