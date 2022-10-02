#include <stdio.h>

void main()
{
    printf("<---------\tAnkit Pandey\t--------\t\n---------\tRoll No : 21E80003\t-->\n");
    int n;
    printf("Enter the Number of Elements of array : ");
    scanf("%d", &n);
    int arr[n];

    // Taking inputs for the array
    for (int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int max = arr[0];
    int min = arr[0];
    for (int i=1;i<n;i++){
        if (max< arr[i]){
            max= arr[i];
        }
        if (min> arr[i]){
            min= arr[i];
        }
    }
    printf("Maximum Number in the array is %d and Minimum is %d \n",max,min);
}