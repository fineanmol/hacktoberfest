//Find Square Root using Newton's method

#include <stdio.h> 
float sqt(int num)
{
	int start = 1, end = num; 
	int tmp;
	float ans;
	while (start <= end)
	 { 
	 	tmp = (start + end) / 2; if (tmp * tmp == num) 
	 	{
	 	 ans = tmp;
		 break;
		}
		if (tmp * tmp < num) 
		 {
	 	 	start = tmp + 1;
		 	ans = tmp;
		 }
		else 
		 {
			 end = tmp - 1;
	     }
	  }

float incr = 0.1;
for (int i = 0; i < 5; i++)
 { 
 	while (ans * ans <= num) 
 		{ 
 			ans += incr; 
 		}
		ans = ans - incr; 
		incr = incr / 10;
  }
return ans; 
} 


int main()
{
	int n;
	printf("Enter The Value:"); 
	scanf("%d",&n);
	printf("Square root is : %.3f ", sqt(n)); 
	return 0;
}
