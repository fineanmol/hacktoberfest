public static int height(Node root) 
{
  if(root==null)
  	return -1;
  if(root.left==null && root.right ==null)
  	return 0;
  return  1 + Math.max(height(root.left),height(root.right));
}


// node Structure for reference
    public class Node
    {
        public int data;
        public Node left;
        public Node right;
        public Node(int data)
        {
            this.data = data;
        }
    }
