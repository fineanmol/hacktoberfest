//                        A Simple Java program to generate Pascal's Triangle
//                                                  1
//                                                1   1 
//                                              1   2   1
//                                            1   3   3   1
//                                          1   4   6   4   1
//

import java.util.Scanner;

public class Pascal
{
  public static void main(String[] args){
    int n = 5;
    for(int i=0; i<n; i++) {
      int a = 1;
      System.out.printf("%" + (n-i) * 2 + "s", "");
      for(int j=0; i<=j; j++){
        System.out.printf("%4d", a);
        a = a * (i-j) / (j+1);
      }
      System.out.println();
    }
  }
}
