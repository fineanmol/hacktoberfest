package compi_prog;

public class prime {
		
		 public static void main(String aergs[])
		 {
		    
		     int i,j,l=0;
		    for(i=1;i<0;i++)
		     { int k=0;
		      for(j=1;j<=i;i++)
		       { 
		        if(i%j==0)
		         k++; 
		         if(k==2)
		           l++;
		         if(l==10001)
		         System.out.print(i);
		       }
		        
		         
		       
		    }
		 }
		

	}


