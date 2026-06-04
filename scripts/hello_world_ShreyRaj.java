import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
 
        System.out.print("Enter your name: ");
        String username = scanner.nextLine();
 
        System.out.println("Hello, World " + username + "!");
 
        scanner.close();
    }
}
