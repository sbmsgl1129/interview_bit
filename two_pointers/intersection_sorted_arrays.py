class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        
        ans = []
        
        len_A = len(A)
        len_B = len(B)
        
        i = 0
        j = 0
        while i < len_A  and j < len_B:
            if A[i] == B[j]:
                ans.append(A[i])
                i += 1
                j += 1
                
            elif A[i] < B[j]:
                i += 1
            elif A[i] > B[j]:
                j += 1
        
        return ans
