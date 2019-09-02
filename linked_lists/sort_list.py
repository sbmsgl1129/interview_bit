# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def split(node, steps):
    fin = None
    prev = None
    
    while node and steps:
        steps -= 1
        prev = node
        node = node.next
    
    if prev:
        fin = prev.next
        prev.next = None
    
    return fin
    
def merge(left, right, tail):
    
    while left and right:
        if left.val < right.val:
            tail.next = left
            tail = left
            left = left.next
        else:
            tail.next = right
            tail = right
            right = right.next
        
    
    tail.next = left if left else right
    while tail.next:
        tail = tail.next
    
    return tail

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        
        len_A = 0
        tmp = A
        while tmp:
            len_A += 1
            tmp = tmp.next
        
        dummy = ListNode(None)
        dummy.next = A
        
        step = 1
        while step < len_A :
            left = None
            right = None
            
            curr = dummy.next
            tail = dummy
            
            while curr:
                left = curr
                right = split(curr, step)
                curr = split(right, step)
                tail = merge(left,right, tail)
            
            step = step << 1
        
        return dummy.next
