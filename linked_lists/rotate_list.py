# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def length(A):
    len_A = 0
    while A:
        len_A += 1
        A = A.next
    
    return len_A

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        #empty list
        if not A:
            return A
        
        len_A = length(A)
        
        to_rotate = B % len_A
        if to_rotate == 0:
            return A
        
        # Three things to-do:
        # - End of list should point to begin
        # - We should have a new pointer to head
        # - prev to head should have its next set to none
        
        # Setting the correct rotate_head
        rotate_head = A
        rotate_head_prev = None
        rotate_head_distance = len_A - to_rotate
        while rotate_head_distance:
            rotate_head_prev = rotate_head
            rotate_head = rotate_head.next
            
            rotate_head_distance -= 1
        
        # Setting rotate_head_prev to None
        rotate_head_prev.next = None
        
        # Setting the last pointer to previous head
        temp = rotate_head
        while temp.next:
            temp = temp.next
        temp.next = A
        
        return rotate_head

