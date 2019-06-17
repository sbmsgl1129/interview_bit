class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        
        A.sort()
        
        min_xor_val = A[0] ^ A[1]
        for i in range(1, len(A) - 1):
                xor_val = A[i] ^ A[i+1]
                if xor_val < min_xor_val:
                    min_xor_val = xor_val
        
        return min_xor_val
