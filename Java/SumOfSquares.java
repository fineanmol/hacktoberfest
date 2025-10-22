/*
Program to find sum of positive square elements in the array.

Sample input 1:
Size of  Array : 4
Elements in Array : 1 2 3 4
Sample output 1:
30
Explanation :
(1 + 4 + 9 + 16) = 30


Sample input 2:
4
-1 -2 -3 -4
Sample output 2:
30
Explanation :
(1 + 4 + 9 + 16) = 30

*/

import java.util.*;
import java.lang.*;
import java.io.*;
public class SumOfSquares
{
   public static void main(String[] args) 
   {
    Scanner sc = new Scanner(System.in);
  int n = sc.nextInt();
  int arr[] = new int[n];
  for(int i = 0 ; i<n ; i++)
  {
  arr[i] = sc.nextInt();
  }
  System.out.print(SumOfSquare(arr,n));  // Calling The Method
}
 
static long SumOfSquare(int arr[],int n)  // Method Declaration
{
long sum = 0;
for(int i = 0 ; i<n ; i++)
{
sum = sum + arr[i]*arr[i];
}
return sum;
}
}
