import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Simple Calculator");
        System.out.println("Enter first number:");
        double num1 = scanner.nextDouble();
        System.out.println("Enter operator (+, -, *, /):");
        char operator = scanner.next().charAt(0);
        System.out.println("Enter second number:");
        double num2 = scanner.nextDouble();
        double result = 0;
        boolean valid = true;

        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    System.out.println("Error: Division by zero");
                    valid = false;
                }
                break;
            default:
                System.out.println("Invalid operator");
                valid = false;
        }

        if (valid) {
            System.out.println("Result: " + result);
        }

        scanner.close();
    }
}
