#include<iostream>
using namespace std;

class Test{
    public:
    Test(){
        cout<<"Test created"<<endl;
        //fis.opem("mytest")
    }
    //destructor
    ~Test(){
        cout<<"Test destroyed"<<endl;
        //fis.close();  Destructor used for releasing resources
    }
};

int main()
{
    Test *p=new Test();//constructor called
    delete p; //destructor called when object destoyed
    return 0;
}

//destructor is used for deallocating external things like heap memory ,files,networking
//we cannot have multiple destructors,i.e cannot be overloaded
//destructor can be virtual also
//constructor and destructor both cannot return 
//constructor can be overloaded ,destructor cannot