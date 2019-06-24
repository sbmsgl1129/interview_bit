class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        
        i = 0
        j = 0
        len_B = len(B)
        initial_len_A = len(A)
        current_len_A = initial_len_A
        
        while j < len_B:
            if A[i] < B[j]:
                i += 1
            else:
                A.insert(i,B[j])
                i += 1
                j += 1
                current_len_A += 1
                
            
            if i == current_len_A:
                A.extend(B[j:])
                j = len_B
        
        print(' '.join([str(x) for x in A]) + ' ')
        
        return
