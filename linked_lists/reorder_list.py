# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        
        if not A:
            return A
        
        slow = A
        fast = A
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        stack = []
        while slow.next:
            stack.append(slow.next)
            slow = slow.next
            
        curr = A
        last_ele = None
        while stack:
            last_ele = stack.pop()
            
            next_tmp = curr.next
            curr.next = last_ele
            last_ele.next = next_tmp
            
            curr = next_tmp
        
        #Removing last node reference
        if curr.next == last_ele:
            curr.next = None
        else:
            curr.next.next = None
        
        return A
