from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        uniq = []
        
        d = defaultdict(int)
        for i in range(B):
            d[A[i]] += 1
        
        d_len = len(d)
        uniq.append(d_len)
        
        for i in range(B, len(A)):
            d[A[i-B]] -= 1
            if d[A[i-B]] == 0:
                d_len -= 1
                del d[A[i-B]]
            
            if A[i] not in d:
                d_len += 1
            d[A[i]] += 1
            
            uniq.append(d_len)
        
        return uniq
