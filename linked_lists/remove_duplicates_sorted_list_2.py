# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        
        #This will keep track of elements which are not repeated
        ans = None
        ans_last = None
         
        prev = None
        curr = A
        n    = A.next if A else None
         
         
        while curr:
            if (not prev or prev.val != curr.val) and (not n or curr.val != n.val):
                if not ans:
                    ans = curr #for the first time
                    ans_last = curr
                else:
                    ans_last.next = curr
                    ans_last = curr
             
            prev = curr
            curr = n
            if curr:
                n = curr.next

        if ans_last:
            ans_last.next = None
        
        return ans
