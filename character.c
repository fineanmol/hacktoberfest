// input a character and change its case (lower to upper and vice versa)
#include<stdio.h>
int main()
{
    char ch;
    printf("enter a character:");
    scanf("%c",&ch);
    if(ch>='a'&& ch<='z'){
        ch=ch-32;
    }
    else if (ch>='A'&& ch<='Z')
    {
        ch=ch+32;
    }
    printf("The converted character is: %c \n",ch);
    return 0;
}
