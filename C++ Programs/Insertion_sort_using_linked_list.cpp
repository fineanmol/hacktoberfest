/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>

using namespace std;  

struct Node  // strcuture node
{
    int data;
    struct Node *next;
};
struct Node *head = NULL;
void insert(int x)
{
    // struct Node link = (struct Node)malloc(sizeof(struct Node));
    struct Node *link = (struct Node *)malloc(sizeof(struct Node));
    link->data = x;
    link->next = NULL;
    if(head==NULL)   
    {
    link->next = head;
    head = link;
    }
    else
    {
       struct Node *current, *temp = NULL;
       current=head;
       
       bool ans=true;
        while(current!=NULL)
        {
           
         if(link->data<=current->data)
         {
             if(temp==NULL)
             {
              link->next=current;
              head=link;
              ans=false;
              break;
             }
             else
             {
            temp->next=link;
            link->next=current;
            ans=false;
            break;
             }
             if(!ans)
             break;
         }
          temp=current;
          current=current->next;
        }
        if(ans)
        {
            temp->next=link;
            link->next=NULL;
        }
    }
}



void disp()
{

    struct Node *prt = head;

    printf("List is : \n");
    while (prt != NULL)
    {
        printf("%d\t", prt->data);
        prt = prt->next;
    }
    printf("\n");
}
int main()
{
    int x;
    for(int i=0;i<5;i++)
    {
      cout<<"Give Data of Node "<<i+1<<":";
      cin>>x;
      insert(x);
    }
    
disp();
    return 0;
}

