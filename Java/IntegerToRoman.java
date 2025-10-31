import java.util.Scanner;

public class IntegerToRoman
{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter an integer: ");
    int num = sc.nextInt();

    int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    
    String roman = "";
    
    for(int i = 0; i < values.length; i++) {
      while(num >= values[i]) {
        num = num - values[i];
        roman = roman + symbols[i];
      }
    }
    
    System.out.println("Roman numeral: " + roman);
  }
}

