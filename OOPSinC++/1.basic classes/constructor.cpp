#include <iostream>
using namespace std;

class Rectangle
{
private:
  int length;
  int breadth;

public:

//defaults arguments to l=1 and b=1 if not given as parameter.
//constructor
Rectangle(int l=1,int b=1){
  setLength(l);
  setBreadth(b);
}

//shallow copy constructor
Rectangle(Rectangle &r1){
  length=r1.length;
  breadth=r1.breadth;
}

//setter functions... mutators
//set length function..involves validation
void setLength(int l){
  if(l<0){
    length=1;
  }else{
  length=l;
  }
}

void setBreadth(int b){
  if(b<0){
    breadth=1;
  }else{
  breadth=b;
  }
}

//getter functions ...accessors
int getLength(){
    return length;
  }

  int getBreadth(){
    return breadth;
  }

  int area()
  {
    return getLength()* getBreadth();
  }

  int perimeter()
  {
    return 2 * (getLength() + getBreadth());
  }
};

int main()
{
  Rectangle r1(10,5);
  cout<<r1.area()<<endl;
  Rectangle r2(r1);
  cout<<r2.area();

  return 0;
}