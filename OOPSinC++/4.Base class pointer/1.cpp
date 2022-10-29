#include<iostream>
using namespace std;

class Base{
    public:
    void fun1(){
        cout<<"fun1 of base"<<endl;
    }
};

class Derived : public Base{
    public:
    void fun2(){
        cout<<"fun2 of derived"<<endl;
    }
};

int main()
{
    Derived d;
    Base *p=&d;
    p->fun1();
    //p->fun2();

    //incorrect..cannot assign object of base to ptr of derived
    Derived *q;
    Base b;
    //q=&b;
    return 0;
}