// Diamond pattern - using c++
// Creator - namratabose32

//     *
//    ***
//   *****
//  *******
// *********
// *********
//  *******
//   *****
//    ***
//     *


#include<iostream>
using namespace std;
int main(){
	int i,j,k,n,z=1;
	cin>>n;
	for(i=1;i<=2*n;i++){
		if(i<=n){
			for(j=1;j<=n-i;j++){
				cout<<" ";
			}for(k=1;k<2*i;k++){
				cout<<"*";
			}
		}else{
			for(k=1;k<z;k++){
				cout<<" ";
			}for(j=1;j<=(2*n-i)*2+1;j++){
				cout<<"*";
			}z++;
		}cout<<endl;
	}return 0;
}