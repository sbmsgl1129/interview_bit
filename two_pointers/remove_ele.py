class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        ans = 0
        i = -1
        j = 0
        while j < len(A):
            if A[j] != B:
                i += 1
                A[i] = A[j]
                ans  += 1
            
            j += 1
        return ans
