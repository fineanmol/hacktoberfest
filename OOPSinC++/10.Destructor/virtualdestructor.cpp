#include<iostream>
using namespace std;

class Base{
    public:
    Base(){
        cout<<"Base Constructor"<<endl;
    }
    ~Base(){
        cout<<"Base Destructor"<<endl;
    }
};

class Derived:public Base{
    public:
    Derived(){
        cout<<"Derived Constructor"<<endl;
    }
    virtual ~Derived(){
        cout<<"Derived Destructor"<<endl;
    }
};

int main(){
    Base *p=new Derived(); //base class pointer to derived object
    delete p;
    return 0;
}

//if you want to achieve run time polymorphism,you need to make base class functions as virtual
//same thing is done in case of a virtual destructor
//if not done then partial destruction is done,i.e base destructor willbe called and not derived destructor