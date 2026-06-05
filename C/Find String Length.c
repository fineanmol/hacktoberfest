//Find a string length. Check if string length same as no of characters in the string?

#include <stdio.h> 
int main()
{
	char firstname[20], middlename[20], surname[20]; 
	printf("Input your firstname: ");
	scanf("%s", firstname); 
	printf("Input your middlename: "); 
	scanf("%s", middlename); 
	printf("Input your surname: "); 
	scanf("%s", surname);
	printf("Your name is: %s %s %s\n", firstname, middlename, surname); 
	printf("Your name is: %s %s %s\n", surname, firstname, middlename); 
	return 0;
}
