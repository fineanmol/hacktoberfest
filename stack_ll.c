#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;
}*top=NULL,*new,*temp;
void push();
void pop();
void peek();
void display();
void main()
{
    int c=0;
    
    while(c!=5)
    {
        printf("\nEnter \n1:Push\n2:Pop\n3:Peek\n4:Display\n5:Exit");
        scanf("%d",&c);
        switch (c)
        {
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                peek();
                break;
            case 4:
                display();
                break;
            case 5:
                exit;
                break;
        }
    }
    free(new);
    free(top);
    free(temp);
}
void push()
{
    new=(struct node *)malloc(sizeof(struct node));
    printf("Enter the value");
    scanf("%d",&new->data);
    if(top==NULL)
    {
        new->next=NULL;
        top=new;
    }
    else
    {
        new->next=top;
        top=new;
    }
    printf("\nNode inserted");
}
void pop()
{
    if(top==NULL)
    {
        printf("Stack is empty");
    }
    else
    {
        temp=top;
        top=top->next;
        free(temp);
    }
}
void peek()
{
    printf("top - %d",top->data);
}
void display()
{
    temp=top;
    while(temp!=NULL)
    {
        printf("%d - ",temp->data);
        temp=temp->next;
    }
}
