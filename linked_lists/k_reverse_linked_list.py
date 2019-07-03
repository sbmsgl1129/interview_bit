# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def reverse_list(start, length):
    
    head = None
    tail = start
    
    curr = start 
    while length:
        n = curr.next
        curr.next = head
        head = curr
        curr = n
        
        length -= 1
    
    return (head,tail,curr)

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        
        reversed_list = None
        reversed_list_last = None
        
        curr = A
        while curr:
            head,tail,tail_next = reverse_list(curr,B)
            
            if not reversed_list:
                reversed_list = head
            else:
                reversed_list_last.next = head
            
            reversed_list_last = tail
            curr = tail_next
        
        return reversed_list
            
        
