#include<iostream>
using namespace std;

// in struct all data memmbers
// and functions are public
struct Rectangle{
    int x;
    int y;

    void Display(){
        cout<<x<<" "<<y;
    }
};

//in class by default everything is
//private,need to explicitly assign public or protected
class Recta{
 
};

int main()
{
    Rectangle r;
    r.x=10;
    r.y=20;
    r.Display();
    return 0;
}