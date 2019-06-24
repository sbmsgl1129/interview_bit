class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        
        i = 0
        j = 1
        
        repeated_ele = A[i]
        repeated_count = 1
        
        while j < len(A):
            if A[j] != A[i]:
                     i += 1
                     A[i] = A[j]
                     repeated_ele = A[j]
                     repeated_count = 1
            else:
                if repeated_count < 2:
                    i += 1
                    A[i] = A[j]
                    repeated_count += 1
                    
            j += 1
        
        return i + 1

