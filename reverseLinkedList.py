class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            nxt = curr.next      
            curr.next = prev     
            prev = curr          
            curr = nxt           
        return prev 



