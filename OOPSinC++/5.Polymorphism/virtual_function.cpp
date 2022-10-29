#include<iostream>
using namespace std;

//to achieve runtime polymorphism,we need:
//1.virtual functiion
//2.overrided function
//3.base class pointer and derived class object


//by using virtual functions,we imply that existence
//of that class is virtual,the base/parent class will
//have no functional effect on child.

class Parent{
    public:
    //virtual keyword is to be used in base/parent class
    //this is actually run time polymorphism
    virtual void display(){ //note ..virtual keyword
    //when Parent class function is declared as virtual
    //and if function is overiden in Child class
    //then child ka overridden function is executed
    //i.e function call will not be based on pointer but
    //on object ,if virtual mentioned..
        cout<<"Display of Parent"<<endl;
    }
};

//if virtual not mentioned then function of Parent/Base will 
//be called due to static linkage..The call to function is 
//getting set only once by the compiler which is in the base class.

class Child : public Parent{
    public:
    void display(){
        cout<<"Display of Child"<<endl;
    }
};

int main()
{
    Parent *p=new Child();
     //or Child d;
     // Parent *q=&d;
     //using pointer calling function
    p->display(); 

    Child d;
    d.display();
    return 0;
}

//in java , it directly calls child ka function ,virtualka jhanjhat nahi
//Virtual functions are so useful that later languages 
//like Java keep all methods as virtual by default.