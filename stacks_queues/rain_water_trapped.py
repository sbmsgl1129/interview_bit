from collections import deque

def dq_insert(dq, num, idx):
    len_dq = len(dq)
    stack  = []
    
    while dq:
        if num > dq[0][0]:
            dq.clear()
            break
        
        stack.append(dq.popleft())
    
    dq.appendleft((num,idx))
    while stack:
        dq.appendleft(stack.pop())
    
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        output = []
        dq = deque()
        
        for idx in range(min(B, len(A))):
            dq_insert(dq, A[idx], idx)
        
        output.append(dq[0][0])
        
        for idx in range(B, len(A)):
            if (A[idx - B],idx-B) in dq:
                dq.remove((A[idx - B],idx-B))
            dq_insert(dq, A[idx],idx)            

            output.append(dq[0][0])
        
        
        return output
