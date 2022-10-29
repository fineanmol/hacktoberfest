#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

//serialiazation is a process of storing and retrieving the state of an object
class Student{
    public:
    string name;
    string branch;
    int roll;
//overload operator and using friend function
//for serialization ,must overload >>and<< operators
    friend ofstream & operator <<(ofstream &ofs,Student &s);
    friend ifstream & operator >>(ifstream &ifs,Student &s);
};
ofstream & operator<<(ofstream &ofs,Student &s){
    ofs<<s.name<<endl;
    ofs<<s.roll<<endl;
    ofs<<s.branch<<endl;

    return ofs;
};

ifstream & operator >>(ifstream &ifs,Student &s){
ifs>>s.name>>s.roll>>s.branch;
return ifs;
};

int main()
{
    Student s1;
    
    //now, we want to store this object in a file..we dont want to store individual values but as an object
    ifstream ifs("Student.txt");
    ifs>>s1; //retrieving the state of an object from a file
    cout<<"name "<<s1.name<<endl;
    cout<<"roll "<<s1.roll<<endl;
    cout<<"branch "<<s1.branch<<endl;
    ifs.close();
    
    return 0;
}