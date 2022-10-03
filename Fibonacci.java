import java.util.Scanner;

public class Fibonacci {

    public static void main(String[] args) {

        System.out.println("Enter the number of terms of Fibonacci Series:");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int fb1 = 1;
        int fb2 = 1;
        int fbn = 0;
        int sum = 0;

        if (n <= 0) {
            System.out.println("Please correct number of items and try again.");
            // return;
        }

        System.out.println("The first " + n + " Fibonacci numbers are:");
        for (int i = 1; i <= n; i++) {
            switch (i) {
                case 1:
                    fbn = fb1;
                    break;
                case 2:
                    fbn = fb2;
                    break;
                default:
                    fbn = fb1 + fb2;
                    fb1 = fb2;
                    fb2 = fbn;
            }
            sum += fbn;
            System.out.print(fbn + " ");
        }
        System.out.println();
        System.out.printf("The sum is %d \n", sum);
        System.out.printf("The average is %.4f \n", (float) sum / n);
        sc.close();
    }

}