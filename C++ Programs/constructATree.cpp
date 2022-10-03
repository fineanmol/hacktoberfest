// Q1 - CONSTRUCT A TREE FROM INORDER + PREORDER TRAVERSAL
#include<iostream>
using namespace std ;
 
class node
{
public:
    int data;
    node *left;
    node *right;

    node(int data)
    {
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

int findPosition(int element , int inorder[] , int n){
    for (int i = 0; i < n; i++)
    {
        if(element == inorder[i])
            return i ;
    }
    return -1 ;
}

node* solveQ1(int inorder[] , int preorder[] , int &index , int start , int end , int n){

    if( index > n-1 || start > end ){
        return nullptr ;
    }

    int element = preorder[index++] ;
    int position = findPosition(element , inorder , n) ;
    node* temp = new node(element) ;

    temp -> left = solveQ1(inorder,preorder,index,start,position-1,n) ;
    temp -> right = solveQ1(inorder,preorder,index,position+1,end,n) ;

    return temp ;

}

node* buildTreeFromInorderAndPreorderTraversal(int inorder[] , int preorder[] , int n){
    int index = 0 ;
    node* answer = solveQ1(inorder,preorder,index , 0,n-1 , n) ;
    return answer ;
}

void postOrderTraversal(node* root){

    postOrderTraversal(root->left) ;
    postOrderTraversal(root->right) ;
    cout<<root->data<<" " ;

}

int main(){

node* temp = NULL ;
int inorder[4] = {1,6,8,7} ;
int preorder[4] = {1,6,7,8} ;
node* a = buildTreeFromInorderAndPreorderTraversal(inorder,preorder,4) ;
postOrderTraversal(a) ;

return 0 ;
}