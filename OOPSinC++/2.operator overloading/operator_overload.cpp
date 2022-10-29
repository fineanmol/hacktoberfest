#include <iostream>
using namespace std;

class Complex
{
private:
    int real;
    int img;

public:
    Complex(int real = 0, int img = 0)
    {
        this->real = real;
        this->img = img;
    }

    //operator overloading with +
    Complex operator+(Complex x)
    {
        Complex temp;
        temp.real = this->real + x.real;
        temp.img = this->img + x.img;
        return temp;
    }

    Complex operator-(Complex x){
        Complex temp;
        temp.real = this->real - x.real;
        temp.img = this->img - x.img;
        return temp;
    }
    //you need a display function as you can't directly write c3.real etc..loses the essence of abstraction
    void display()
    {
        cout << real << "+i" << img << endl;
        cout<<real<<"-i"<<img<<endl;
    }
};

int main()
{
    Complex c1(5, 7);
    Complex c2(9, 6);
    Complex c3;
    c3 = c1 + c2;
    c3.display();

    return 0;
}