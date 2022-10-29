#include<iostream>
using namespace std;

class Test{
    private:
    int a;
    int b;

    public:
    static int count;
    Test(){
        a=10;
        b=10;
        count++;
    }

//you cannot use non static members inside statuc function
    //static functions can be called upon  a class and upon an object
    static int getCount(){
        //a++; incorrect
        return count;
    }
};
//static members belong to a class ,but are
//common for all subsequent objecs

//shareable membersof a class

//when you have a static variable in a class
//you must declare it outside

int Test::count =0; //actually a global variable which is available
//only inside test class

int main()
{
    Test t1;
    Test t2;
    cout<<t1.count<<endl;
    cout<<t2.count<<endl;
   
    cout<<t2.count<<endl;
    cout<<Test::count<<endl; //this implies that there is a single
    //count variable which can be accesssed by  scope resolution and objects
    cout<<Test::getCount();
    cout<<t1.getCount();
    return 0;
}

//note..you can access static function without creating object
//classname :: functionname()

//can obviously access with object too

//the static function or variable effectively belongs to a 
//class not an obect..

//static members are like shared memory..they also provide info abt the class