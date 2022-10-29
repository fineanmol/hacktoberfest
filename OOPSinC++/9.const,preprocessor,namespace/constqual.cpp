#include<iostream>
using namespace std;
int main()
{
    //int x=10; this is variable
    const int x=10; //this is now a constant identifier,not a variable
   // x++;once set constant then cannot modify
    //const is used for holding unchanging values
    //const is part of compiler
    cout<<x<<endl;
    return 0;
}

//note:-  #def x 10 is a preprocessor director,it is perforemed before compilation process starts
// # def x 10 will not occupy space ,and is not part of compiler
//is globally usefull 