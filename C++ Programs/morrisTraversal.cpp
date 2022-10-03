// MORRIS TRAVERSAL - INORDER TRAVERSAL 

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

node *buildTree(node *&root)
{
    cout << "Enter data of node : ";
    int value;
    cin >> value;
    root = new node(value);

    if (value == -1)
    {
        return NULL;
    }

    cout << "LEFT NODE TO : " << root->data << endl;
    root->left = buildTree(root->left);
    cout << "RIGHT NODE TO : " << root->data << endl;
    root->right = buildTree(root->right);

    return root;
}

void morrisTraversalInorder(node* root){

    node* curr = root ;

    while(curr != NULL){
 
        if(curr->left == NULL){
            cout<<curr->data<<" " ;
            curr = curr->right ;
        }
        else{
            node * prev = curr->left ;
            while(prev->right != NULL && prev->right != curr){
                prev = prev->right ;
            }
            if(prev->right == NULL){
            prev->right = curr ;
            curr = curr -> left ;
        }
        else{
            prev->right = NULL ;
            cout<<curr->data<<" " ;
            curr = curr->right ;
        }
    }
    }
}
 
int main(){
 
node* root = NULL ;
buildTree(root) ;
cout<<endl ;
morrisTraversalInorder(root) ;

return 0 ;
}