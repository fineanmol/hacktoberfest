#include<bits/stdc++.h>
using namespace std;

int main(){
  string s;
  cin>>s;
  int n=s.length();
  int ans=INT_MAX;
  map<char,int> m;
  for(int i=0;i<n;i++){
    m[s[i]]++;
  }
  map<char,int> m1;
  int i=0,j=0;
  while(j<n){
    m1[s[j]]++;
    if(m1.size()<m.size())
      j++;
    else if(m1.size()==m.size()){
      while(m1.size()==m.size() && i<j){
        ans=min(ans,j-i+1);
        m1[s[i]]--;
        if(m1[s[i]]==0)m1.erase(s[i]);
        i++;
      }
      j++;
    }
  }
  cout<<"Smallest Distinct Window is "<<ans<<endl;
  return 0;
}
