#include<iostream>
using namespace std;

//write down name of 'desired class',dont put brackets after
//declaration,compiler needs name of class beforehand
class Your;
class My{
    private:
    int a=10;

friend Your;
};

//Your is a container class having objects of My class
//In container clsses ,if u want to access private members
//or protected members then we can declare them as friend inside those classes
class Your{
    public:
    My m;

    void func(){
        cout<<m.a;
    }
};

int main()
{
    Your y;
    y.func();
    //func to be accessed upon object not directly..alert!
    return 0;
}