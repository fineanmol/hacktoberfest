//Program to find smallest and largest element in an array

#include <stdio.h>

int main() {
    int n, i,max,min;
    int arr[100];
    printf("Enter the number of elements: ");
    scanf("%d",&n);
    printf("\nEnter %d integers: ",n);
    for(i=0;i<n;i++) {
        scanf("%d",&arr[i]);
    }
    printf("\nEntered array: [");
    for (i=0;i<n;i++) {
        printf("%d",arr[i]);
        if(i<n-1) {
            printf(", ");
        }
    }
    printf("]");
    max=arr[0];
    for(i=1;i<n;i++) {
        if(arr[i]>max) {
            max=arr[i];
        
        }
    }
    max=arr[0];
    for(i=1;i<n;i++) {
        if(arr[i]>max) {
            max=arr[i];    
        }
    }
    min=arr[0];
    for(i=1;i<n;i++) {
        if(arr[i]<min) {
            min=arr[i];
        }
    }
    printf("\nLargest element: %d",max);
    printf("\nSmallest element: %d",min);
   
    return 0;
}
