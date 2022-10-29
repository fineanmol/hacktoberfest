#include<iostream>
using namespace std;

class Base{
public:

//Two constructors in parent class,
//so by default the non parameter constructor will be executed
Base(){
    cout<<"Default of base "<<endl;
}

Base(int x){
    cout<<"Parameter of Base : "<<x<<endl;
}
};

class Derived : public Base{
public:
Derived(){
    cout<<"Default of Derived"<<endl;
}

Derived(int a){
    cout<<"Parameter of Derived : "<<a<<endl;
}
Derived(int x,int a):Base(x){ //calls parameterized constructor
//of base class from parameterized constructor of derived class
    cout<<"Param of derived II: "<<a<<endl;
}
};

int main()
{
    Derived d; //VVVImp first base class constructor executed then derived class ka constructor
    cout<<endl;

    Derived d1(10);//non parameterized Constructor of base class executed,then parameterized constructor of Derived
    cout<<endl;
    //for calling parameterized constructor of base,I must have special constructor in derived
   
    Derived d2(20,10);
    return 0;
};

//constructor of derived is called first but not executed,
//the call then goes to the constructor of base class

//called:derived to base
//execution:base to derived