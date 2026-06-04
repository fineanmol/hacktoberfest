public class Prime_Generating_Integer 
{

	public static void main(String[] args)
	{
		   int i=1,j,k,c=0,s1=0, n=9;
		     for(i=1;i<=n;i++)
		     { int s=0;
		        for(j=1;j<=i;j++)
		        {
		         if(i%j==0)
		          {s=((i%j)+i)/i%j;
		            }
		          else
		           continue;
		        for(k=1;k<=s;k++)
		         {
		            if(s%k==0)
		             c++;
		            if(c==2)
		             s1=s1+s;}
		            }
		        }
		    System.out.println("Sum="+s1);
		 }
		
		

	



	}

}
