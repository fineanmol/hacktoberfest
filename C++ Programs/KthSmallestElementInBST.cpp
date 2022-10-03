#include <bits/stdc++.h>
using namespace std;

// Problem Link : https://leetcode.com/problems/kth-smallest-element-in-a-bst/
/*
Problem Statement :
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

*/

struct TreeNode {
   int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode() : val(0), left(nullptr), right(nullptr) {}
   TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
   TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/*
Approach :
  We pass k by reference 
  Do inorder traversal of tree
  if k is 0 at any time this means we have already reached kth smallest node : we simply return answer from here
  else we recur for left and right half after decrementing k
*/

void inorder(TreeNode*&T,int &k,int& ans){
    if (T==nullptr) 
        return;
        
    inorder(T->left,k,ans);
    --k;
    if (k==0) ans=T->val;
    inorder(T->right,k,ans);
}
    
int kthSmallest(TreeNode* root, int k) {
    int ans;
    inorder(root,k,ans);
    return ans;
}


int main(){
  TreeNode* T = new TreeNode();
  //buildtree...
  cout<<kthSmallest(T,1)<<'\n'; 
}
  
  
