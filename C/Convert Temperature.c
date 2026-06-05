//Convert Temperature
#include <conio.h>
#include <stdio.h> 
#define size 10 
float f2c(float f){
	float c = ((f-32)*5)/9; 
	return(c);
}
void main()
{
	int n,i;float f[size],t;
	printf("\nEnter number of Input for Fahrenheit to Celcius : "); 
	scanf("%d",&n);
	printf("\n\n");
	for(i = 0; i < n ; i++)
	{
		printf("Enter Temp Fahrenheit : "); 
		scanf("%f",&t);
		f[i] = t;
	}

	printf("\n\n"); 
	printf("\tFahrenheit\t\tCelcius"); 
	for(i = 0; i < n ; i++)
	{
		t = f[i];
		printf("\n\t %.2f \t\t\t %.2f",t,f2c(t));
	}
getch();
}
