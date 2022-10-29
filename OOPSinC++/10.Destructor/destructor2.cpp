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

class Derived: Base{
    public:
    Derived(){
        cout<<"Derived Constructor"<<endl;
    }
    ~Derived(){
        cout<<"Derived Destructor"<<endl;
    }
};


int main()
{
    Derived d;
    //here we are not explicitly deleting memory..so 
    //automatically destructor is called after main 
    //program finishes
    return 0;
}

//first constructor of base is called then derived class
//first destructor of derived class is called then of base class