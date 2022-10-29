#include<iostream>
using namespace std;

//namespaces are used for removing name conflict
//eg.multiple classes /functions with same name..not function overloading
//u need same name as its requirement of program

//we define a namespace and keep function in that..we have encapsulated functions within them
namespace First{
    void fun(){
        cout<<"First"<<endl;
    }
}

namespace Second{
    void fun(){
        cout<<"Second"<<endl;
    }
}
//by using namespaces we have given unique identity to function with same names

using namespace First;
int main()
{
    //use scope resolution to call them
    //First :: fun();
    //so instead of writing First:: everytime for calling functions in it
    //we can write 'using namespace First'
    fun(); //directly fun of first called
    Second::fun();
    return 0;
}

//you can keep namespaces in separate header files and then include them to use