/*You have been given a head to a singly linked list of integers. Write a function check to whether the list given is a 'Palindrome' or not.*/


class LinkedListNode<T> {
    	T data;
    	LinkedListNode<T> next;
    
    	public LinkedListNode(T data) {
        	this.data = data;
    	}
	}
public class Solution {

	public static boolean isPalindrome(LinkedListNode<Integer> head) {
		//Your code goes here
		if(head==null || head.next==null){
            return true;
        }
        LinkedListNode<Integer> middle=findMiddle(head);
        LinkedListNode<Integer> secondHalfStart=reverse(middle.next);
        LinkedListNode<Integer> firstHalfStart=head;
        while(secondHalfStart!=null){
            if(firstHalfStart.data!=secondHalfStart.data){
                return false;
            }
            firstHalfStart=firstHalfStart.next;
            secondHalfStart=secondHalfStart.next;
        }return true;
		//Your code goes here
	}
    public static LinkedListNode<Integer> reverse(LinkedListNode<Integer> head){
        LinkedListNode<Integer> prev=null;
        LinkedListNode<Integer> cur=head;
        LinkedListNode<Integer> next = null;
        while(cur!=null){
            next=cur.next;
            cur.next=prev;
            prev=cur;
            cur=next;
        }return prev;
    }
    public static LinkedListNode<Integer> findMiddle(LinkedListNode<Integer> head){
        LinkedListNode<Integer> fast=head;
        LinkedListNode<Integer> slow=head;
        while(fast.next!=null && fast.next.next!=null){
            fast=fast.next.next;
            slow=slow.next;
        }
        return slow;
    }
}
