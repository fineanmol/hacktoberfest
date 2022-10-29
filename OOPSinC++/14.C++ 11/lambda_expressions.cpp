#include<iostream>
using namespace std;

//lambda expressions are useful for defining unnamed functions
//more like inline functions

//syntax:
//[capture_list](parameter_list)return_type{body}



int main()
{
    [](){cout<<"Hello"<<endl;}(); //this will define as well as callthe function
    //the final () is calling function

    auto k=[](int x,int y){cout<<"Sum: "<<x+y<<endl;};
    k(10,3);

    int x=[](int x,int y){return x+y;}(10,5);//even if we dont mention return type its fine

    //this function is given name f..The function is unnamed,f is a reference to it
    auto f=[](){cout<<"Hello"<<endl;};
    f();

    //we can acceess local variables of a function inside unnamed function
    int s=[](int x,int y)->int{return x+y;}(10,5);
    
    //write a,b in[] as we cant directly write ,need to first capture in []
    int a=10;
    int b=5;
    
    //we cannot modify the captured variables,i.e ++a not allowed
    [a,b](){cout<<a<<" "<<b<<endl;}();
    
    
    //for modyfing of captured variables we need  reference
    [&a,&b](){cout<<++a<<" "<<++b;}();
    return 0;
}