

import java.util.*;
import java.lang.*;
import java.io.*;

class MyCode
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner scan=new Scanner(System.in);
		int T=scan.nextInt();
		while(T-->0)
		{
		   int N=scan.nextInt();
		   String s=scan.next();
		   int count=0;
		   HashMap<Integer, Integer> mp = new HashMap<>();
		   HashMap<Integer, Integer> mpl = new HashMap<>();
		   for(int i = 0; i < N; i++)
            {
                int val=Integer.parseInt(String.valueOf(s.charAt(i)));
         
        // Stores count of distinct
        // values of arr[i] - x * i
        mp.put(val-i,
               mp.getOrDefault(val-i, 0) + 1);
            
            }
             for(int i = 0; i < N; i++)
            {
                int val=Integer.parseInt(String.valueOf(s.charAt(i)));
         
        
                mpl.put(val+i,
              mpl.getOrDefault(val+i, 0) + 1);
            }
 
    // Iterate over the Map
    for(int v : mp.values())
    {
         
        // Increase count of pairs
       // System.out.print(v);
        
        if(v>1)
            count +=(v*(v-1)/2);
    }
    //System.out.println();
     for(int v : mpl.values())
    {
         
        // Increase count of pairs
       
       // System.out.print(v);
        if(v>1)
            count +=(v*(v-1)/2);
    }
    //System.out.println();
    // Print the count of such pairs
    System.out.println(count);
		}
	}
}
