#include <stdio.h>

void swap(int* a,int* b){
    int t=*a;*a=*b;*b=t;
}

int part(int a[],int l,int h){
    int p=a[h],i=l-1,j;
    for(j=l;j<=h-1;j++){
        if(a[j]<=p){
            i++;
            swap(&a[i],&a[j]);
        }
    }
    swap(&a[i+1],&a[h]);
    return i+1;
}

void qs(int a[],int l,int h){
    if(l<h){
        int pi=part(a,l,h);
        qs(a,l,pi-1);
        qs(a,pi+1,h);
    }
}

void print(int a[],int n){
    for(int i=0;i<n;i++) printf("%d ",a[i]);
    printf("\n");
}

int main(){
    int a[]={10,7,8,9,1,5},n=sizeof(a)/sizeof(a[0]);
    print(a,n);
    qs(a,0,n-1);
    print(a,n);
    return 0;
}
