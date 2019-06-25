from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        
        '''

        
        while i < j:
            if A[i] == 0:
                i += 1
            elif A[j] == 2:
                j -= 1
            else:
                break
        '''
        i = 0
        j = len(A) - 1       
        k = i
        while k <= j:
            if A[k] == 0:
                A[i],A[k] = A[k],A[i]
                i += 1
                k += 1
            elif A[k] == 2:
                A[j],A[k] = A[k],A[j]
                j -= 1
            else:
                k += 1
        
        '''
        count = defaultdict(int)
        for num in A:
            count[num] += 1
        
        i = 0
        for key in range(0,3):
            for _ in range(count[key]):
                A[i] = key
                i += 1
        '''
                
        return A
