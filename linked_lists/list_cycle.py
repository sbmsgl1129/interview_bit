# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        
        slow = A
        fast = A
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        if not (fast and fast.next):
            return None
            
        cycle = A
        while cycle != slow:
            cycle = cycle.next
            slow  = slow.next
        
        return cycle

