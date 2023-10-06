import java.util.*;

public class Amstrong {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        int n1 = sc.nextInt();
        int num = n1;
        int n = 0;

        while (num != 0) {
            num /= 10;
            ++n;
        }

        num = n1;
        int sum = 0;
        while (num != 0) {
            int d = num % 10;
            sum += Math.pow(d, n);
            num /= 10;
        }
        System.out.print(n1 == sum);

    }

}
