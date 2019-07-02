# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def findLength(A):
    length = 0
    while A:
        length += 1
        A = A.next
    
    return length

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        
        len_A = findLength(A)
        
        if len_A == 0 or len_A == 1:
            return 1
        
        # Making half list reverse
        num_iterate = len_A // 2
        prev = None
        current = A
        while num_iterate > 0:
            n = current.next
            current.next = prev
            prev = current
            current = n
            
            num_iterate -= 1
         
        # Checking left half and right half
        left = prev
        right = None
        if len_A % 2 == 0:
            right = current
        else:
            right = current.next
        
        while left and right:
            if left.val != right.val:
                return 0
            
            left = left.next
            right = right.next
        
        return 1
