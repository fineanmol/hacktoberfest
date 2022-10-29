#include <iostream>
using namespace std;

class Complex
{
private:
    int real;
    int img;

public:

    Complex(int real=0,int img=0){
        this->real=real;
        this->img=img;
    }

    //vimp...friend function has to be written outside
    //class without scope resolution
    friend Complex operator+(Complex c1, Complex c2);

//need a display function as cannot access private members
//inside main func
    void display()
    {
        cout << real << "+i" << img << endl;
    }
};

//no scope resolution for friend func,its actually a global func
//as it is declared as friend inside class,it is able to use
//private data members

//global functions acting as overloaded operators
//here operator+ is func
Complex operator+(Complex c1, Complex c2)
{
    Complex temp;
    temp.real = c1.real + c2.real;
    temp.img = c1.img + c2.img;
    return temp;
}

int main()
{
    Complex c1(5,5),c2(3,3),c3,c4;
    c3=c1+c2;
    c4=operator+(c1,c3); //can also use operator+ directly
    //here it means c1 +c3,c1 and c3 are parameters
    c3.display();
    c4.display();
    return 0;
}