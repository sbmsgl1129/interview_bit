# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


def reverseList(A, length):
    
    prev = None
    curr = A
    while length > 0:
        n = curr.next
        curr.next = prev
        prev = curr
        curr = n
        
        length -= 1
    
    return (prev,curr)
    
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        
        prev = None
        curr = A
        
        rev_start = None
        rev_end   = None
        
        i = 1
        while True:
            if i == B:
                # It will reverse the list b/w m an n nodes
                # and retur the list start
                rev_end = curr
                rev_start,new_curr = reverseList(curr,C-B+1)
                
                # Manipulating pointers to correctly arrange start abd end
                if prev:
                    prev.next = rev_start
                rev_end.next = new_curr
            
                break
            
            prev = curr
            curr = curr.next
            
            i += 1
        

        return A if B != 1 else rev_start
