#include<iostream>

using namespace std;

struct node
{
    int data;
    node *next;
    node *prev;
};



node *front = NULL;
node *rear = NULL;


bool isEmpty()
{
    if(front == NULL)
        return true;

    return false;
}

node* getNode(int val)
{
    node *temp = new node;
    temp->data = val;
    temp->next = NULL;
    temp->prev = NULL;

    return temp;
}


void insertFront(int val)
{
    node *newNode = getNode(val);

    if(front == NULL)
        front = rear = newNode;
    else
    {
        newNode->next = front;
        front->prev = newNode;
        front = newNode;
    }
}

void deleteFront()
{
    if(front == NULL)
        cout<<"Deque is Empty"<<endl;
    else
    {
        node *temp = front;
        front = front->next;

        if(front == NULL)
            rear = NULL;
        else
            front->prev = NULL;

        free(temp);
    }
}

void insertRear(int val)
{
    node *newNode = getNode(val);
    
    if(rear == NULL)
        front = rear = newNode;
    else
    {
        rear->next = newNode;
        newNode->prev = rear;
        rear = newNode;
    }
}

void deleteRear()
{
    if(front == NULL)
        cout<<"Deque is Empty"<<endl;
    else
    {
        node *temp = rear;
        rear = rear->prev;

        if(rear == NULL)
            front = NULL;
        else
            rear->next = NULL;

        free(temp);
    }
}

int getFront()
{
    if(isEmpty())
        return -1;

    return front->data;
}

int getRear()
{
    if(isEmpty())
        return -1;
    
    return rear->data;
}

void printDeque()
{
    if(front == NULL)
        cout<<"Deque is Empty"<<endl;
    else
    {
        cout<<"Deque:";
        node *temp = front;
    
        while(temp != NULL)
        {
            cout<<temp->data<<" ";
            temp = temp->next;
        }

        cout<<endl;
    }    
}


int main()
{
    cout<<"=>insertFront(10)"<<endl;
    insertFront(10);
    printDeque();

    cout<<"=>insertFront(20)"<<endl;
    insertFront(20);
    printDeque();
   
    cout<<"=>insertRear(30)"<<endl;
    insertRear(30);
    printDeque();

    cout<<"=>insertRear(40)"<<endl;
    insertRear(40);
    printDeque();

    cout<<"=>getFront():"<<getFront()<<endl;
    cout<<"=>getRear(): "<<getRear()<<endl;

    cout<<"=>deleteFront()"<<endl;
    deleteFront();
    printDeque();

    cout<<"=>deleteRear()"<<endl;
    deleteRear();
    printDeque();

    cout<<"=>insertFront(100)"<<endl;
    insertFront(100);
    printDeque();

    cout<<"=>deleteFront()"<<endl;
    deleteFront();
    printDeque();

    cout<<"=>insertRear(300)"<<endl;
    insertRear(300);
    printDeque();
    
    cout<<"=>deleteRear()"<<endl;
    deleteRear();
    printDeque();

    cout<<"=>deleteFront()"<<endl;
    deleteFront();
    printDeque();

    cout<<"=>deleteRear()"<<endl;
    deleteRear();
    printDeque();

    return 0;
}