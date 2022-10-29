#include<iostream>
using namespace std;

class Rectangle{
      private:
      int length;
      int breadth;
      public:
      Rectangle();
      Rectangle(int l,int b);
      Rectangle(Rectangle &r);
      void setLength(int l);
      void setBreadth(int b);
      int getLength(){return length;}; //accessor methods are just one
      int getBreadth(){return breadth;};//line so defined them inline
      int area();
      int perimeter();
      bool isSquare();
      ~Rectangle();
    };
//implementing functions outside class using scope resolution
    
    //using this keyword, 'this->length' means the length variable in private
    // 'length' means the variable which is scoped to the function
    // length=length would be absurd and it wont set the private data member
    //hence we need this keyword
    Rectangle :: Rectangle(int length=1,int breadth=1){
        this->length=length;
        this->breadth=breadth;
    }

    //copy constructor
    Rectangle :: Rectangle(Rectangle &r){
        length=r.length;
        breadth=r.breadth;
    }


    int Rectangle :: area(){
        return getLength()*getBreadth();
    }

    
    Rectangle :: ~Rectangle(){
        cout<<"Rectangle Destroyed"<<"\n";
    }
int main()
{
    Rectangle r1(10,6);
    cout<<r1.area()<<"\n";
    return 0;
}