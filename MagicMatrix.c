//Program to check whether given matrix is magic matrix (has all sum of rows and columns and diagonals are equal) or not
#include <stdio.h>

int main() {
    int a[50][50];
    int i, j, x, y;
    int sum_ref,row_sum,col_sum,diag1_sum,diag2_sum;

    // Input for number of rows and columns
    printf("\nEnter number of rows and columns : ");
    scanf("%d%d", &x, &y);

    // Input for first matrix
    printf("Enter elements of matrix:\n");
    for (i = 0; i < x; i++) {
        for (j = 0; j < y; j++) {
            printf("Element [%d][%d]: ",i+1, j+1);
            scanf("%d", &a[i][j]);
        }
    }

    // Displaying the matrix
    printf("\nEntered matrix is:\n");
    for (i = 0; i < x; i++) {
        for (j = 0; j < y; j++) {
            printf("%d\t", a[i][j]);
        }
        printf("\n");
    }

    sum_ref=0;
    for(j=0;j<y;j++) {
        sum_ref=sum_ref+a[0][j];
    }

    for(i=1;i<x;i++) {
        row_sum=0;
        for(j=0;j<y;j++) {
            row_sum=row_sum+a[i][j];
        }
        if(row_sum!=sum_ref) {
            printf("\nGiven matrix is not magic matrix.");
            return 0;
        }
    }
     for(j=0;j<y;j++) {
        col_sum=0;
        for(i=0;i<x;i++) {
            col_sum=col_sum+a[i][j];
        }
        if(col_sum!=sum_ref) {
            printf("\nGiven matrix is not magic matrix.");
            return 0;
        }
    }
    diag1_sum=0;
    for(i=0;i<x;i++) {
        diag1_sum=diag1_sum+a[i][i];
    }
    if(diag1_sum!=sum_ref) {
        printf("\nGiven matrix is not magic matrix.");
        return 0;
    }
    diag2_sum=0;
    for(i=0;i<x;i++) {
        diag2_sum=diag2_sum+a[i][x-i-1];
    }
    if(diag2_sum!=sum_ref) {
        printf("\nGiven matrix is not magic matrix.");
        return 0;
    }

printf("\nGiven matrix is MAGIC MATRIX!!");
return 0;
}
