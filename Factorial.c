//Program find factorial of a number using recursion
#include <stdio.h>

int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1; // Base case: factorial of 0 or 1 is 1
    } else {
        return n * factorial(n - 1); // Recursive case
    }
}

int main() {
    int number;
    printf("Enter a positive integer: ");
    scanf("%d", &number);

    if (number < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        int result = factorial(number);
        printf("Factorial of %d is %d\n", number, result);
    }

    return 0;
}
