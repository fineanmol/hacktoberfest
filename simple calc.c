/*
 * Simple Calculator Program
 * This program performs basic arithmetic operations: addition, subtraction,
 * multiplication, and division based on user input.
 */ 
#include <stdio.h>

int main() {
    double num1, num2;
    char operator;
    char choice;

    do {
    // Ask the user for input
    printf("Enter first number: ");
    scanf("%lf", &num1);

    printf("Enter second number: ");
    scanf("%lf", &num2);

    printf("Enter an operator (+, -, *, /): ");
    scanf(" %c", &operator); // space before %c helps catch any stray newline characters

    // Perform the selected operation
    switch (operator) {
        case '+':
            printf("Result: %.2lf\n", num1 + num2);
            break;
        case '-':
            printf("Result: %.2lf\n", num1 - num2);
            break;
        case '*':
            printf("Result: %.2lf\n", num1 * num2);
            break;
        case '/':
            if (num2 != 0)
                printf("Result: %.2lf\n", num1 / num2);
            else
                printf("Error: Division by zero is not allowed.\n");
            break;
        default:
            printf("Invalid operator.\n");
    }
    // Ask if the user wants to perform another calculation
    printf("Do you want to perform another calculation? (y/n): ");
    scanf(" %c", &choice);
    num1 = num2 = 0; // Reset numbers for next calculation
    } while (choice == 'y' || choice == 'Y');
    printf("Thank you for using the calculator. Goodbye!\n");
    return 0;
}
