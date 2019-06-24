class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        
        i = 0
        j = 1
        while j < len(A):
            if A[j] != A[i]:
                i += 1
                A[i] = A[j]
            
            j += 1
        
        return i + 1
