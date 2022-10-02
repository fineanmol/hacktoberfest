//Convert Decimal Value to Binary Value

#include<stdio.h> 
#include<stdlib.h> 
int main()
{
	int ar[10],n,i;
	printf("Enter any Decimal Number :: "); 
	scanf("%d",&n);
	for(i=0;n>0;i++)
	{
		ar[i]=n%2; n=n/2;
	}
	printf("\nGiven Number in Binary is :: "); 
	for(i=i-1;i>=0;i--)
	{
		printf("%d",ar[i]);
	}
return 0;
}
