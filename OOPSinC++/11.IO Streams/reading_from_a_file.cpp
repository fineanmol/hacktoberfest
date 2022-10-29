#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    //ifstream is inbuilt class,infile is the object we are calling,can give any name
    ifstream infile;
    infile.open("My.txt");
    string str;
    int x;
    if(!infile.is_open()){
        cout<<"file not open";
    }
    //first it will extract the string
    infile>>str;
    //next it will extract the integer
    infile>>x;
    infile.close();
    cout<<str<<" "<<x;
    //we must always check whether we have reached end of file or not
    if(infile.eof())cout<<"End of file reached"<<endl;
   
    //if we are opening a file,we can use it for read or write purpose
    //ios::in-> for reading, ios::out->for writing...these are actually files
    //when you are reading from a file,it must be exoisting
    //hence use a conditional infile
    return 0;
}