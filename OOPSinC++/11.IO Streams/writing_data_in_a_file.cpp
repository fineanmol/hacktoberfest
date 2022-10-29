#include<iostream>
//for file handling ,must include the header fstream
#include<fstream>
//file is created in same directory
using namespace std;
int main()
{
    //if file already exists then np,if no then automatically new file created
    //for writing to a file,a class ,ofstream is alreay available
    //outfile is the object of that class
    ofstream outfile("My.txt",ios::trunc);
    outfile<<"Hello there"<<endl;
    outfile<<25<<endl;
    outfile.close();//once done ,close the file..the file is now free from file
    //good practice to close file once done
    return 0;
}
//ios::app for append content, ios::trunc for truncate contents
//by default truncate is taken

//streams are used for accessing the data outside the program
//getting or sending the data from program ,we use mechanism of streams
//in c++,there are built in classes for streams ,called ios
//ios-> istream and ostream
//for file access-> ifstream and ofstream
//input stream from keyboard ,already bult in object in iostream header file called "cin" and an overloaded extraction operator
//"cout" is object of ostream with overloaded insertion operator
