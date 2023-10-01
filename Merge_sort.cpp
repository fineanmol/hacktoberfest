#include <bits/stdc++.h>
using namespace std;

void merge(int arr[],int l,int mid,int h){
    
    int len1=mid-l+1;
    int len2=h-mid;
    
    int b[len1],c[len2];int k=l;
    for(int i=0;i<len1;i++){
        b[i]=arr[k++];
    }
    
    for(int i=0;i<len2;i++){
        c[i]=arr[k++];
    }
    
    //Here we are mergeing two sorted arrays(b & c) in array arr.
    int i=0,j=0;
    k=l;
    while(i<len1&&j<len2){
        if(b[i]<c[j])
        arr[k++]=b[i++];
        else arr[k++]=c[j++];
    }
    
    while(i<len1){
        arr[k++]=b[i++];
    }
    
    while(j<len2){
        arr[k++]=c[j++];
    }
    
}
void mergesort(int arr[],int l,int h){
    if(l>=h)
    return;
    int mid=l+(h-l)/2;
    mergesort(arr,l,mid);
    mergesort(arr,mid+1,h);
    merge(arr,l,mid,h);
}
int main() {
	// your code goes here
	
	//o(nlog(n))
	int arr[8]={2,4,5,6,1,7,9,0};
	mergesort(arr,0,7);
	for(int i=0;i<8;i++){
	    cout<<arr[i]<<" ";
	}
	return 0;
}
