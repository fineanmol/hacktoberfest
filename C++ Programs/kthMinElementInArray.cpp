#include<iostream>
#include<queue>
using namespace std ;

int Q1(int arr[] , int n , int k){

    priority_queue<int> q ;
    for(int i=0 ; i<k ; i++){
        q.push(arr[i]) ;
    }

    for (int j = k; j < n; j++)
    {
        if( arr[j] < q.top() ){
            q.pop() ;
            q.push(arr[j]) ;
        }
    }

    return q.top() ;
}

int main(){
 
int arr[5] = {7,10,4,20,15} ;
cout<<"QUESTION 1 ANSWER -> "<<Q1(arr,5,4)<<endl ;

 
return 0 ;
}