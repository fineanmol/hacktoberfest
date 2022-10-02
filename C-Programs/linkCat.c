#include<stdio.h>
#include<stdlib.h>


typedef struct Node {
    char c;
    struct Node* next;
} Node;


void
print(Node* root) {
    Node *current_node = root;
    while(current_node != NULL){
        printf("%c", current_node->c);
        current_node=current_node->next;
    }
}

void
append(Node** root, char ch) {
    Node *new_node = (Node*)malloc(sizeof(Node));
    if(new_node == NULL)
        exit(1);
    
    new_node->c = ch;
    new_node->next = NULL;

    if(*root == NULL){
        *root = new_node;
        return;
    }

    Node* current_node = *root;
    while(current_node->next != NULL)
        current_node=current_node->next;
    
    current_node->next = new_node;
}

void 
dalloc(Node**root) {

    Node* current_node = *root;
    while(current_node != NULL){
        Node* aux = current_node;
        current_node=current_node->next;
        free(aux);

    }
    *root = NULL;
}
