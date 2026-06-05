import java.util.*;
import java.io.*;

class Node {
    Node left;
    Node right;
    int data;
    
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Solution {

	/* 
    
    class Node 
    	int data;
    	Node left;
    	Node right;
	*/
	public static void levelOrder(Node root) {
        
        Queue<Node> q = new LinkedList<>();
        
        q.add(root);
        
        while(!q.isEmpty()){
            
            Node currNode = q.remove();
            
            if (currNode == null){
                return;
            
            
            // if(q.isEmpty()){
            //     break;
            // }
            // else{
            //     q.add(root.left);
            //     q.add(root.right);
            //     // q.add(currNode.data);
            // }
            
            
        }
        
        else{
            System.out.print(currNode.data + " ");
        }
        
        if(currNode.left != null){
            q.add(currNode.left);
        }
        
        if(currNode.right != null){
            q.add(currNode.right);
        }
    }
      
    }

	public static Node insert(Node root, int data) {
        if(root == null) {
            return new Node(data);
        } else {
            Node cur;
            if(data <= root.data) {
                cur = insert(root.left, data);
                root.left = cur;
            } else {
                cur = insert(root.right, data);
                root.right = cur;
            }
            return root;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        Node root = null;
        while(t-- > 0) {
            int data = scan.nextInt();
            root = insert(root, data);
        }
        scan.close();
        levelOrder(root);
    }	
}
