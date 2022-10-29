#include<iostream>
using namespace std;


//Here both base and derived classes have data members as public
//just to give an overview of working of inheritance..private data
//members are dealt differently.


//we cannot access private members directly,need to use help of setter and getter functions.

class Base{

public:
int x;

void display(){
    cout<<x<<endl;
}
};

class Derived : public Base{

public:
int y;

void show(){
    cout<<x<<" "<<y<<endl;
}
};

int main()
{
    Base b;
    b.x=5;
    b.display(); //Display is ffrom base
    Derived d;
    d.y=10;
    d.x=6;
    d.display();
    d.show(); //show func is from Derived
    return 0;
}