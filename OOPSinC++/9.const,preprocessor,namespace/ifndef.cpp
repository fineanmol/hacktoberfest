#include<iostream>
using namespace std;

#define PI 3.1425 //if i comment this line then 3 printed
#ifndef PI //if not defined then only define
 #define PI 3
#endif

int main()
{
    cout<<PI; //output is 3.1425 not 3 as PI already defined above
    //the defn of pi wont be written as it is enclosed in conditional of ifndef
    
    return 0;
}