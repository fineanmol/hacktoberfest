#include<iostream>
#include<vector>
using namespace std;
int main()
{
    vector<int> v={10,20,40,90};//if size not mentioned,then it creates a vector of size 16
    v.push_back(25);
    v.push_back(70);
    v.pop_back();

    //iterating through a vector
     for(int x:v){
    cout<<x<<endl;
    }
    //method 1:for each loop
  
    //method 2:using inbuilt iteratir classes
    vector<int> :: iterator itr;
    for(itr=v.begin();itr!=v.end();itr++){
        cout<<++*itr<<endl; //*itr coz itr is a pointer to elements inside collection
    }
    //iterator class belongs to class vector ,as we used scope resolution
    //created an object itr of iterator class
    //begin() is a function in all containers
    //iterator is a pointer
    return 0;
}