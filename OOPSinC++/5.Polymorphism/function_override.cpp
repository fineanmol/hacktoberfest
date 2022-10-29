#include<iostream>
using namespace std;

//Function overriding is used for achieving runtime polymorphism
//Prototype of a overrides function must be exactly same as base class function
class Parent{
    public:
    void display(){
        cout<<"Display of Parent"<<endl;
    }

    void print(){
        cout<<"Printing parent"<<endl;
    }

};

class Child : public Parent{
    public:
    //already Parent had display()func,we are overriding
    //or redefining it..writing itt once again
    void display(){
        cout<<"Display of Child"<<endl;
    }

    void print(int x){
        cout<<"Print child"<<endl;
    }
};

int main()
{
    Child c;
    //overriding
    c.display();


    //c.print(); 
    //gives error as child ka print had argument

    //using scope resolution to use Parent ka print()
    //this is not overriding function but called function overloaading
    c. Parent :: print();

    c.print(10); //this is correct as argument passed
    return 0;
}