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
    Rectangle :: Rectangle(int l=1,int b=1){
        length=l;
        breadth=b;
    }

    //copy constructor
    Rectangle :: Rectangle(Rectangle &r){
        length=r.length;
        breadth=r.breadth;
    }

    void Rectangle ::setLength(int l){
        if(l<0){
         length=1;
        }else{
         length=l;
        }
    }

    void Rectangle ::setBreadth(int b){
        if(b<0){
         length=1;
        }else{
         length=b;
        }
    }

    int Rectangle :: area(){
        return getLength()*getBreadth();
    }

    bool Rectangle :: isSquare(){
        return length==breadth;
    }

    Rectangle :: ~Rectangle(){
        cout<<"Rectangle Destroyed"<<"\n";
    }

int main()
{
    Rectangle r1(10,5);
    cout<<r1.area()<<'\n';
    
    Rectangle r2(r1);
    cout<<r1.area()<<"\n";

    Rectangle r3(10,10);
    if(r3.isSquare()){
        cout<<"It is a square"<<"\n";
    }else{
        cout<<"It is not a square"<<"\n";
    }
    return 0;
}