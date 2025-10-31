import java.util.Scanner;
public class Factorial
{
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
System.out.print("Enter an Integer: ");
int num = sc.nextInt();
int fact = 1;
if(num < 0)
System.out.println("Invalid Input");
else
{
for(int i = 1; i <= num; i++)
fact = fact * i;
System.out.print("Factorial is "+fact);
}
}
}
