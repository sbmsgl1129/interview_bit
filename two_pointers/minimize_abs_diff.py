class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        
        i = 0
        j = 0
        k = 0
        
        #ans  = max([A[0],B[0],C[0]) - min(A[0],B[0],C[0])
        ans   = float('inf')
        while i < len(A) and j < len(B) and k < len(C):
            min_val = min(A[i],B[j],C[k])
            max_val = max(A[i],B[j],C[k])
            
            diff = max_val - min_val
            if diff < ans:
                ans = diff
            
            if min_val == A[i]:
                i += 1
            elif min_val == B[j]:
                j += 1
            else:
                k += 1
        
        return ans
