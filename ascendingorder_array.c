//Program to arrange numbers of array in ascending order
#include <stdio.h>

int main() {
    int n, i, j, temp;
    int arr[100];
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d integers: ", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("\nEntered array: [");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
        if (i < n - 1) {
            printf(", ");
        }
    }
    printf("]\n");
    // Sorting array in ascending order using bubble sort
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // Swap arr[j] and arr[j+1]
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    printf("\nSorted array in ascending order: [");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
        if(i < n - 1) {
            printf(", ");
        }
    }
    printf("]\n");

    return 0;    
}
