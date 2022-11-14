#include<stdio.h>

void binary_search(int array[], int min, int max, int data)
{
    int mid;
    mid = (min + max) / 2;          //check the mid of the array
    if (data == array[mid])
    {
        printf("Data found at position : %d\n",  mid);
    }
    else if (data > array[mid])
    {
        min = mid + 1;
        binary_search(array, min, max, data);
    }
    else
    {
        max = mid - 1;
        binary_search(array, min, max, data);
    }
}

int main()
{
    int array[10] = {1,2,3,4,5,6,7,8,9,10};
    int size = 10, data;
    int min = 0, max = size-1;

    printf("Enter the data to search : ");
    scanf("%d", &data);

    binary_search(array, min, max, data);
    return 0;
}
