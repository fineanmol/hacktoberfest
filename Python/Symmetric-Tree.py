def tree(root): 
            if root==None: 
                return True
            return check(root.left,root.right) 
        
        def check(l,r): 
            if l==None or r==None: 
                return l==r 
            elif l.val!=r.val: 
                return False 
            else: 
                return check(l.left,r.right) and check(l.right,r.left) 
            
        return tree(root)
