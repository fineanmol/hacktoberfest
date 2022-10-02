

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class BST {
    static class Node {
        int data;
        Node left;
        Node right;

        Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    public static boolean search(Node root, int val) {
        if (root == null)
            return false;
        if (root.data == val)
            return true;
        if (val < root.data) {
            return search(root.left, val);
        } else {
            return search(root.right, val);
        }

    }

    public static Node insert(Node root, int data) {
        if (root == null) {
            Node node = new Node(data);
            root = node;
            return root;
        }
        if (data < root.data) {
            root.left = insert(root.left, data);
        } else {
            root.right = insert(root.right, data);
        }
        return root;
    }

    private static Node delete(Node root, int key) {

        if (root == null)
            return null;

        if (key < root.data) {
            // left
            root.left = delete(root.left, key); // it will connect root.left to the answer root geting from the call
        } else if (key > root.data) {
            // right
            root.right = delete(root.right, key); // it will connect root.right to the answer root geting from the call
        }

        if (root.data == key) // key found
        {
            // 0 child
            if (root.left == null && root.right == null) {
                root = null;
                return root;
            }

            // 1 child

            if (root.right == null) {
                return root.left;
            } else if (root.left == null) {
                return root.right;
            }
            // 2 child
            if (root.left != null && root.right != null) {
                int rightMin = minValue(root.right); // getting Minimum value from the right side to maintain the BST
                root.data = rightMin; // Now, root.data = minimum value from the right
                root.right = delete(root.right, root.data); // Now, call root.right with key as a root.data i.e.(delete
                                                            // the childNode)
            }
        }
        return root;
    }

    private static int minValue(Node root) {
        int minv = root.data;
        while (root.left != null) {
            minv = root.left.data;
            root = root.left;
        }

        return minv;
    }

    public static void inOrder(Node root) {
        if (root == null) {
            return;
        }
        inOrder(root.left);
        System.out.print(root.data + " ");
        inOrder(root.right);
    }

    private static boolean isValidBST(Node root, int leftRange, int rightRange) {

        // Time Complexity O(n) because we traverse every node
        // Spacew complexity O(h)
        if (root == null)
            return true;

        if ((root.data > leftRange) || (root.data < rightRange))
            return true;

        return isValidBST(root.left, leftRange, root.data) && isValidBST(root.right, root.data + 1, rightRange);

    }

   

 

    public static void main(String[] args) {
        Node root = null;

        root=insert(root, 6);
        root=insert(root, 2);
        root=insert(root, 8);
        root=insert(root, 0);
        root=insert(root, 4);
        root=insert(root, 7);
        root=insert(root, 9);
        root=insert(root, 3);
        root=insert(root, 5);
        inOrder(root);
       
       

         Scanner s =new Scanner(System.in);
         int choice;
        System.out.printf("\n\t 1.insert\n\t 2.search\n\t 3.Delete\n\t 4.Min-value \n\t  5.EXIT");
       
    do
     {
             System.out.println("\n Enter the Choice:");
             choice=s.nextInt();
             switch(choice)
             {
                 case 1:
                 {
                     System.out.println("Enter a value");
                     int val=s.nextInt();
                     root=insert(root, val);
                     break;
                 }
                 case 2:
                 {
                     System.out.println("Enter a value for search");
                     int val=s.nextInt();
                     System.out.println(search(root, val));
                    break;
                 }
                 case 3:
                 {
                     System.out.println("Enter a value for search");
                     int key=s.nextInt();
                     delete(root, key);
                     break;
                 }
                 case 4:
                 {
                     System.out.println(minValue(root));
                     break;
                 }
                 case 5:
                {
                     System.out.println("\n\t EXIT POINT ");
                     break;
                 }
                 default:
                 {
                     System.out.println("\n\t Please Enter a Valid Choice(1/2/3/4)");
                 }
                    
             }
         }
         while(choice!=4);
         s.close();
     }
      
    }
}
