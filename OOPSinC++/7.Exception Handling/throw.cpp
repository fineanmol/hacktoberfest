#include <iostream>
using namespace std;

//you can throw in any data type,can also throw classes and corresponding object
// int division(int x, int y) throw(int)
//throw(data_type) is optiona but a good programming practice

int main()
{
    int a = 10, b = 0, z;

    try
    {
        if(b==0){
        throw 1;
    }
    else{
        z= a/b;
    }
        cout << z;
    }
    catch(int e){
        cout<<"Int catch"<<e;
    }
    catch(double e){
        cout<<"Double catch"<<e;
    }
    catch (...) //keep the generic catch at the last,catch all must be at last
    {
        cout << "Catch All";
    }
    return 0;
}

//there is a built in class in c++ caled exception,you can inherit
//from there

//we can have multiple catch blocks for each type of data
///catch(...) -> ... is called ellipsis.
//this means catch for all type of exceptions

//we can have nested try and catch blocks too

//if exception classes are defined in a hierarchy,then child 
//class catch must be written first then parent class catch block