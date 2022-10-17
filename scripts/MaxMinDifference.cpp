#include <bits/stdc++.h>
using namespace std;

int main()
{
  int A[5]={-2, 1, -4, 5, 3}, N=5;
  int max=0,min=0;
  for(int i=0;i<N;i++){
      if(A[i]<=min){
          min=A[i];
      }
      if(A[i]>=max){
          max=A[i];
      }
  }
  cout<<max-abs(min);//abs() function gives absolute value(- becomes +)
}
