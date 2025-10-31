// LANGUAGE: Javascript
// ENV: Node.js
// AUTHOR: AngleAirdrop
// GITHUB: https://github.com/AngleAirdrop

import java.util.Scanner;

public class SimpleGreeting {
    public static void main(String[] args) {
        // Create a Scanner object to read user input
        Scanner input = new Scanner(System.in);

        System.out.println("Hello! What is your name?");
        System.out.print("Enter your name: ");

        String name = input.nextLine(); // Read user input

        System.out.println("Nice to meet you, " + name + "! Hope you have a great day.");

        input.close(); // Close the scanner
    }
}
