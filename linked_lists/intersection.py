# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#finding the lenght of a list
def findLength(A):
    
    length = 0
    while A:
        length += 1
        A = A.next
    
    return length
    
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        len_A = findLength(A)
        len_B = findLength(B)
        
        # making always A to have greater length
        if len_B > len_A:
            A,B = B,A
            len_A,len_B = len_B,len_A
        
        #Advancing A by those many steps
        difference = len_A - len_B
        while difference > 0:
            A = A.next
            difference -= 1
        
        while A:
            if A == B:
                return A
            A = A.next
            B = B.next
        
        return None
