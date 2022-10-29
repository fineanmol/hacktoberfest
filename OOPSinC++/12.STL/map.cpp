#include<iostream>
#include<map>
using namespace std;
int main()
{
    map<int,string> m; //key is int and value is string
    m.insert(pair<int,string>(1,"Utkarsh"));
    m.insert(pair<int,string>(2,"Mann"));
    m.insert(pair<int,string>(3,"Vader"));

    //iteration through map 
    //iterator is of class map and itr is the object
    map<int,string>::iterator itr;
    for(itr=m.begin();itr!=m.end();itr++){
        cout<<itr->first<<" "<<itr->second<<endl;
        //since we want to display both key and value
        // using itr pointer,there is inbulit first and 
        //second to indicate key and value
    }
cout<<endl;
    //finding value by using key
    //to find we will use inbuilt find and iterator of map class
    map<int,string>::iterator itr1;
    itr1=m.find(2);
    cout<<itr1->first<<" "<<itr1->second<<endl;
    cout<<"Value found";
    return 0;
}