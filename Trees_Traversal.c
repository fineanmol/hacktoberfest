#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *left;
    struct node *right;
};

struct node *create(int data)
{
    struct node *p;
    p = malloc(sizeof(struct node));
    p->data = data;
    p->left = NULL;
    p->right = NULL;
}

void postorder(struct node *root)
{
    if (root != NULL)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", *root);
    }
    else
    {
        return;
    }
}

int main()
{
    struct node *p1 = create(1);
    struct node *p2 = create(2);
    struct node *p3 = create(3);
    struct node *p4 = create(4);
    struct node *p5 = create(5);
    struct node *p6 = create(6);
    p1->left = p2;
    p1->right = p3;
    p2->left = p4;
    p2->right = p5;
    p3->right = p6;
    printf("The postorder traversal of the given Data are as follows: ");
    postorder(p1);
    return 0;
}