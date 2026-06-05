#include<bits/stdc++.h>
using namespace std;

struct node
{
    int data;
    struct node *next;
};

struct node *Create(int n)
{
    struct node *head,*temp;
    head=(struct node*)malloc(sizeof(struct node));
    head->data=1;
    head->next=NULL;
    temp=head;
    for(int i=2;i<=n;i++)
    {
        struct node* newnode=(struct node*)malloc(sizeof(struct node));
        newnode->data=i;
        newnode->next=NULL;
        temp->next=newnode;
        temp=newnode;
    }
    return head;
}

struct node *Insert(struct node *head,int val,int pos)
{
    struct node *temp=head;
    struct node *newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=val;
    if(pos==1)
    {
        newnode->next=head;
        head=newnode;
    }
    else
    {
        int j=1;
        while(j<pos-1)
        {
            temp=temp->next;
            j++;
        }
        newnode->next=temp->next;
        temp->next=newnode;
    }
    return head;
}

struct node *Delete(struct node *head,int pos)
{
    struct node *temp=head,*delNode;
    if(pos==1)
    {
        head=head->next;
        free(temp);
    }
    else
    {
        int j=1;
        while(j<pos-1)
        {
            temp=temp->next;
            j++;
        }
        delNode=temp->next;
        temp->next=temp->next->next;
        free(delNode);
    }
    return head;
}

void printLL(struct node *head)
{
    struct node *temp;
    temp=head;
    while(temp!=NULL)
    {
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    cout<<endl;
}

int main()
{
    struct node *head;
    int n,value,pos;
    
    //Number of Nodes In Linked List
    cout<<"Enter The Number Of Nodes"<<endl;
    cin>>n;   
    
    //Creating The Linked List
    head=Create(n);
    
    //Printing The Linked List
    cout<<"Linked List:"<<endl;
    printLL(head);
    
    //Insertion In Linked List
    cout<<"Enter Value To Be Inserted In Linked List"<<endl;
    cin>>value;
    cout<<"Enter Position"<<endl;
    cin>>pos;
    if(pos>n+1)
    {
        cout<<"Position Not Available"<<endl;
    }
    else
    {
        head=Insert(head,value,pos);
        //Printing The Linked List
        cout<<"Linked List:"<<endl;
        printLL(head);    
    }
    
    //Deletion In Linked List
    cout<<"Enter The Postion For Deletion"<<endl;
    cin>>pos;
    if(pos<1 || pos>n)
    {
        cout<<"Position Not Available"<<endl;
    }
    else
    {
        head=Delete(head,pos);
        //Printing The Linked List
        cout<<"Linked List:"<<endl;
        printLL(head);
    }
    
    return 0;
}
