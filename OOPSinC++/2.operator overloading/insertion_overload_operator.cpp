#include <iostream>
using namespace std;


//Input stream cin >> (extraction) operator can be 
//overloaded upon a classoutput stream cout << (insertion) 
//operator can be overloaded upon a class


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

    //calling this display() function
    //seems absurd,can use operator overloading
    //want to display like cout<<c1
    //hence insertion overload

    /*void display()
    {
        cout << real << " + " << img << "i" << endl;
    }
    */

//takes two operators as parameters i.e output stream object 
// and complex number object

//operator function is taking two different parameters 
//from two different types of objects,so it cannot belong to 
//type complex,hence it is a friend function
//as friend function,it cannot be implemented inside class
friend ostream & operator<<(ostream &out,Complex &c1);
 //return type is ostream
 //complex c1 can and cannot be taken as a reference
};

//passing o and c1 by reference
ostream & operator<<(ostream &out,Complex &c1)
    {
        //write o<< and not cout<< 
        out<<c1.real << " + " <<c1.img << "i" << endl;
        return out;
    }

int main()
{
    Complex c1(5, 9), c2(8, 13);
    cout<<c2;
    operator<<(cout,c2); //operator here is a function name
    //both statements are correct
    return 0;
}