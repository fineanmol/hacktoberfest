#include<iostream>
using namespace std;
int main(){
	string s;
	cout<<"Enter the string: ";
	cin>>s;
	int n = s.length();
	bool ans = true;
	int i=0,j=n-1;
	while(i<j){
		if(s[i]!=s[j]){
			ans = false;
			break;
		}
		i++;
		j--;
	}
	if(ans){
		cout<<"YES";
	}
	else{
		cout<<"NO";
	}
}
