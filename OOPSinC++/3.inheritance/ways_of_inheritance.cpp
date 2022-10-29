#include<iostream>
using namespace std;

//program for behaviour of different access specifiers on 
//subsequent child classes

class Parent{
    private:int a;
    protected:int b;
    public:int c;
      
      void funParent(){
          a=1;
          b=2;
          c=3;
      }
};

class Child : private Parent{
    public:
    void funChild(){
       // a=10;
        b=20;
        c=30;
    }
};

class GrandChild : public Child{
    public:
    void funGrandChild(){
        //a=100;
       // b=200;
        //c=300;
    }
};

int main()
{
    //Child c;
    //c.a=4;
    //c.b=5;
    //cout<<c.c;
    return 0;
}