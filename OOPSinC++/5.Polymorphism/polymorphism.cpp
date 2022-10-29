#include<iostream>
using namespace std;

class Car{
    public:
    virtual void start(){
        cout<<"Car started"<<endl;
    }
};

class Innova:public Car{
    public:
    void start(){
        cout<<"Innova started"<<endl;
    }
};

class BMW:public Car{
    public:
    void start(){
        cout<<"BMW started"<<endl;
    }
};

int main()
{
    Car *ptr=new Innova();
    ptr->start();
    ptr=new BMW;
    ptr->start();
    return 0;
}

//line 28 and 30 are same ,but output is different 
//this is polymorphism,here we have achieved run time polymorphism
//same mechanism in java is called as dynamic method dispatch