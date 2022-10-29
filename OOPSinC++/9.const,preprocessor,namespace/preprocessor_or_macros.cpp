#include<iostream>
using namespace std;

//preprocessor directives are also called macros
//these are instructions given to the compiler
//we can give instructions to compiler before it starts compiling so that it can follow those instuctions beforehand
//these are actually commands to the compiler,eg like #include iostream etc
//replacing contents before compilation process starts
#define PI 3.145 
#define c cout

//these are usually used to define constants like 3.145,
//these are called symbolic constants
#define max(x,y) (x>y?x:y) //enclose in brackets
#define SQR(x) (x*x)
#define msg(x)  #x //this # with x means that parameter after compilation will be enclosed in double quotes 
//i,e will return a string
int main()
{
    cout<<PI<<endl;
    c<<10<<endl;

    cout<<SQR(5)<<endl;
    cout<<msg(hello)<<endl;
    cout<<max(10,25);
    return 0;
}