class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        
        ans = float('inf')
        
        i = 0
        j = 0
        k = 0
        
        while i < len(A) and j < len(B) and k < len(C):
            t1  = abs(A[i] - B[j])
            t2  = abs(B[j] - C[k]) 
            t3  = abs(C[k] - A[i])
            
            max_difference = max(t1, t2, t3)
            
            if max_difference < ans:
                ans = max_difference
                
            if max_difference == t1:
                if A[i] < B[j]:
                    i += 1
                else:
                    j += 1
            elif max_difference == t2:
                if B[j] < C[k]:
                    j += 1
                else:
                    k += 1
            elif max_difference == t3:
                if C[k] < A[i]:
                    k += 1
                else:
                    i += 1         
        
        return ans

