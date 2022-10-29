#include<iostream>
using namespace std;

class Rectangle{
    private:
    int length;
    int breadth;

    public:
 //constructors in heritance can be confusing
    Rectangle(int length=1,int breadth=1);
    
    void setLength(int length);
    void setBreadth(int breadth);
    int getLength();
    int getBreadth();
    int area();
    int perimeter();
    bool isSquare();
    ~Rectangle();
};



  Rectangle :: Rectangle(int l,int b){
        this->length=l;
        this->breadth=b;
    }

  void Rectangle :: setLength(int length){
        this->length=length;
    }

    void Rectangle :: setBreadth(int breadth){
        this->breadth=breadth;
    }

    int Rectangle :: getLength(){
        return length;
    }

    int Rectangle :: getBreadth(){
        return breadth;
    }

    int Rectangle :: area(){
        return getLength()*getBreadth();
    }

    int Rectangle ::perimeter(){
        return 2*(getLength()* getBreadth());
    }

    Rectangle :: ~Rectangle(){
        cout<<"Rectangle Destroyed"<<"\n";
    }

class Cuboid : public Rectangle{
    private:
    int height;

    public:
    Cuboid(int h=0){
        height=h;
    }
   
    int getHeight(){
        return height;
    }

    void setHeight(int h){
        height=h;
    }

    int volume(){
        return getLength()*getBreadth()*height;
    }

    int surface_area(){
        return 2*(getLength()*height + getLength()*getBreadth() + getBreadth()*height);
    }
};


int main()
{
    Cuboid c1(8);
    c1.setLength(10);
    c1.setBreadth(5);
    cout<<c1.volume()<<endl;
    
    return 0;
}