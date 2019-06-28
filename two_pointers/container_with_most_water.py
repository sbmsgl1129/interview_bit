class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        
        
        ans = 0
        
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] < A[j]:
                if A[i]*(j-i) > ans:
                    ans = A[i]*(j-i)
                i += 1
            elif A[i] > A[j]:
                if A[j]*(j-i) > ans:
                    ans = A[j]*(j-i)
                j -= 1
            else:
                if A[j]*(j-i) > ans:
                    ans = A[j]*(j-i)
                
                i += 1
                j -= 1
        
        return ans

