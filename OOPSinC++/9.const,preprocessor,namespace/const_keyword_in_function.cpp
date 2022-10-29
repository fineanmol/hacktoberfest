#include<iostream>
using namespace std;

class Demo{
    public:
    int x=10;
    int y=20;

    void Display(){
        x++;
        cout<<x<<" "<<y<<endl;
    }

//if you dont want the member function of class to modify 
//the data member,just allow reading values..then write const keyword after function name
    void Show() const {
          x++; //not allowed
        cout<<x<<" "<<y<<endl;
    }
};

int main()
{
    Demo d;
    d.Display();
    return 0;
}

//function parameters can also be made as constant