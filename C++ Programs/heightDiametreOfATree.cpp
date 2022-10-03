// QUESTION 1 - HEIGHT OF A BINARY TREE
// QUESTION 2 - DIAMETRE OF A BINARY TREE
// QUESTION 3 - CHECK IF A TREE IS BALNCED OR NOT

#include<iostream>
using namespace std ;

class node{
  public:

    int data ;
    node* left ;
    node* right ;

    node(int data){
        this->data = data ;
        this->left = NULL ;
        this->right = NULL ;
    }
};

node* buildTree(node* &root){
    cout<<"Enter data of node : " ;
    int value ;
    cin>>value ;
    root = new node(value) ;

    if(value == -1){
        return NULL ;
    }

    cout<<"LEFT NODE TO : "<<root->data<<endl ;
    root->left = buildTree(root->left) ;
    cout<<"RIGHT NODE TO : "<<root->data<<endl ;
    root->right = buildTree(root->right) ;

    return root ;
}

int heightOfBinaryTree(node* root){

    if(root == NULL){
        return 0 ;
    }
    
    int leftHeight = heightOfBinaryTree(root->left) ;
    int rightHeight = heightOfBinaryTree(root->right) ;

    return max(leftHeight,rightHeight) + 1 ;
}

int diametreOfTree(node* root){
    
    if(root == NULL){
        return 0 ;
    }

    int option1 = diametreOfTree(root->left) ;
    int option2 = diametreOfTree(root->right) ;
    int option3 = heightOfBinaryTree(root->left) + 1 + heightOfBinaryTree(root->right) ;

    int option4 = max(option2 , option3) ;
    return max(option1 , option4) ;
}
 
int main(){
 
node* root = NULL ;
buildTree(root) ;

cout<<"HEIGHT OF THE TREE IS : "<<heightOfBinaryTree(root) <<endl;
cout<<"DIAMETER OF THE TREE IS : "<<diametreOfTree(root)<<endl ; 
return 0 ;
}