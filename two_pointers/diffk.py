class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        
        isDiffPresent = 0
        
        i = 0
        j = 1
        while j < len(A):
            if i == j:
                j += 1
                continue
            
            if A[j] - A[i] == B:
                isDiffPresent = 1
                break
            elif A[j] - A[i] > B:
                i += 1
            else:
                j += 1
        
        return isDiffPresent
