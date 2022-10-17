#include<stdio.h>
#include<conio.h>
int main()
{
    int num, rev, rem;
    printf("Enter the Number: ");
    scanf("%d", &num);
    for(rev=0; num!=0; num=num/10)
    {
        rem = num%10;
        rev = (rev*10)+rem;
    }
    printf("\nReverse = %d", rev);
    getch();
    return 0;
}
