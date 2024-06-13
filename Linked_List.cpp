#include <bits/stdc++.h>
using namespace std;

class Node{
    public:
    int data;
    Node* next;
    Node(int x){
        data=x;
        next=nullptr;
        
    }
};
//1->2->3->4->5->6->
void printList(Node * head){
    Node* node=head;
    while(node){
        cout<<node->data;
        node=node->next;
    }
   
}
// Node* reverseSingleLL(Node * root){
//     Node *prev=NULL,*curr=root,*nextNode=root;
    
//     while(curr!=NULL){
//         nextNode=nextNode->next;
//         curr->next=prev;
//         prev=curr;
//         curr=nextNode;
//     }
//     return prev;
// }
// void reveseList(Node *head){
//     Node * node=head;
//     Node * node1=node->next;
//     node->next=NULL;
//     Node *node2=reverseSingleLL(node1);
//     node1->next=node2;
//     printList(node1);
// }

void addNode(Node* &tail,int x)
{
    Node* node=new Node(x);
    tail->next=node;
    tail=tail->next;
}

int main() {
	// your code goes here
	Node *head=new Node(0);
	Node* tail=head;
	
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
	    int x;
	    cin>>x;
	    addNode(tail,x);
	}
	
	printList(head->next);
// 	reveseList(head);
	return 0;
}
