#include<iostream>
using namespace std;

class Parent //if write class Parent final ,then it blocks inheritance of parent class
{
    virtual void show() final 
    // only virtual function can be marked with keyword final
    //final functions of parent class cannot be overrided in chid class

//final keyword used for restricting inheritance and 
//restrict overriding of functions
//final keyword is there in java too
    {

    }

};

class Child:Parent
{
    void show() //cannot override
    {
        
    }
};

int main()
{
    return 0;
}