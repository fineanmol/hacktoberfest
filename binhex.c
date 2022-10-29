#include<stdio.h>
#include<math.h>
void main()
{	
	float a[10][4];
	int i,n,j,t,k,l,m,r,f=0,p,q;
	float sum=0;
	printf("enter no.of digits\n");
	scanf("%d",&n);
	printf("Enter the matrix\n");
	for(j=0;j<n;j++)
	{
		for(i=0;i<4;i++)
		{
			scanf("%f",&a[j][i]);
		}
	}
	for(i=0;i<n;i++)
	{
	sum=(a[i][0]*pow(2,3))+a[i][1]*pow(2,2)+a[i][2]*pow(2,1)+a[i][3]*pow(2,0);
	printf("\n");
	if((sum>=0)&&(sum<=9))
	printf("%f",sum);
	
	if (sum==10)
	printf("A");
	if (sum==11)
	printf("B");
	if (sum==12)
	printf("C");
	if (sum==13)
	printf("D");
	if (sum==14)
	printf("E");
	if (sum==15)
	printf("F");
	
	
	}
	
}