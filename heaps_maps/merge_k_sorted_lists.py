import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        start = ListNode(None)
        end = start
        
        list_heap = []
        for i in range(len(A)):
            heapq.heappush(list_heap, (A[i].val, A[i]))
        
        while list_heap:
            _, list_ele = heapq.heappop(list_heap)
            
            end.next = list_ele
            if list_ele.next != None:
                heapq.heappush(list_heap, (list_ele.next.val, list_ele.next))
            
            list_ele.next = None
            end = end.next
            
        return start.next
            
