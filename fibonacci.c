#include<stdio.h>
int Fibonacci(int);
int main()
{
	int n,i;
	printf("Enter a number you want to generate fibonacci series\n");
	scanf("%d",&n);
	printf("Fibonacci series\n");
	for(i=0;i<n;i++)
	{
		printf("%d\n",Fibonacci(i));
	}
	return 0;
}
int Fibonacci(int n)
{
	if(n == 0)
		return 0;
	else if(n == 1)
		return 1;
	else
		return(Fibonacci(n-1) + Fibonacci(n-2));
}


