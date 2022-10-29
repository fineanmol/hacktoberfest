#include<iostream>
using namespace std;

class Test{
    private:
    int a;
    protected:
    int b;
    public:
    int c;

    friend void func();
};

//friend function is outside/global function
//not a member function which can access
//all the members of a class upon 
//object ,but not directly

//this is useful in operator overloading

//similar concept is for a friend class

void func(){
    Test t;
    t.a=10;
    t.b=5;
    t.c=1;
}

int main()
{
    return 0;
}