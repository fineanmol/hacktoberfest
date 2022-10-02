#ifndef queue_h
#define queue_h
#include <iostream>
using namespace std;

struct Node
{
    int data;
    struct Node *next;
} *front = NULL, *rear = NULL;

// struct queue
// {
//     int size;
//     int front;
//     int rear;
//     Node **Q;
// };

// Initialising the queue object.

void enqueue(int x)
{
    struct Node *t;
    t = new Node;
    if (t == NULL)
    {
        cout << "Queue is full." << endl;
    }
    else
    {
        t->data = x;
        t->next = NULL;
        if (front == NULL)
        {
            front = rear = t;
        }
        else
        {
            rear->next = t;
            rear = t;
        }
    }
}

// Deletion of object in circular queue.

int dequeue()
{
    int x = -1;
    struct Node *t;

    if (front == NULL)
    {
        cout << "Queue is empty" << endl;
    }
    else
    {
        x = front->data;
        t = front;
        front = front->next;
        delete t;
    }
    return x;
}

// Function for checking if the queue is empty or not.

int isEmpty()
{
    return front == NULL;
}

#endif // queue_h