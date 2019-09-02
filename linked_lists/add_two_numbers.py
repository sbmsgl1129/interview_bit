# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        
        sum_list_head = None
        sum_list_last = None
        carry = 0
        while A and B:
            sum_val = A.val + B.val
            sum_val += carry
            
            carry = sum_val // 10
            sum_val %= 10
            
            sum_list_node = ListNode(sum_val)
            if not sum_list_head:
                sum_list_head = sum_list_node
            else:
                sum_list_last.next = sum_list_node
                
            sum_list_last = sum_list_node
            
            
            A = A.next
            B = B.next
        
        # if B gets completed and A is still there
        while A:
            sum_val = A.val + carry
            carry = sum_val // 10
            sum_val %= 10
            
            sum_list_node = ListNode(sum_val)
            if not sum_list_head:
                sum_list_head = sum_list_node
            else:
                sum_list_last.next = sum_list_node
                
            sum_list_last = sum_list_node
            
            
            A = A.next
        
        # if A gets completed and B is still there
        while B:
            sum_val = B.val + carry
            carry = sum_val // 10
            sum_val %= 10
            
            sum_list_node = ListNode(sum_val)
            if not sum_list_head:
                sum_list_head = sum_list_node
            else:
                sum_list_last.next = sum_list_node
                
            sum_list_last = sum_list_node
            
            
            B = B.next
        
        # For the remanining carry
        if carry != 0:
            sum_list_node = ListNode(carry)
            sum_list_last.next = sum_list_node
        
        return sum_list_head
