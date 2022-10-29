#include<iostream>
using namespace std;
  
class Base
{
public:
    virtual void show() { cout<<" In Base \n"; }
};
  
class Derived: public Base
{
public:
    void show() { cout<<"In Derived \n"; }
};
  
int main(void)
{
    Base *bp = new Derived; //base class ptr to derived object
    bp->show();
  
    Base &br = *bp; //basically a reference to Derived object
    br.show();

    Derived d; //directly calling derived object
    d.show();
  
    return 0;
}