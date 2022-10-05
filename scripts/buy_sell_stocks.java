import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        // write your code here
        Scanner scn = new Scanner (System.in);
        int n = scn.nextInt();
        int[] prices = new int[n];
        for (int i=0; i<n; i++)
        {
            prices[i] = scn.nextInt();
        }
        
        int lsf = Integer.MAX_VALUE;
        int op = 0;
        int pist = 0;
        for(int i=0; i<prices.length;i++)
        {
           if(prices[i]<lsf)
           {
               lsf = prices[i];
           }
           
           pist = prices[i] -lsf;
           
           if(pist>op)
           {
               op= pist;
           }
        }
    System.out.println(op);
}
}