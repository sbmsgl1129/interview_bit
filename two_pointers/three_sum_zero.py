'''
def skip_duplicates(A, j, k):
    
    j += 1
    k -= 1
    while j < k:
        if A[j] == A[j-1] and A[k] == A[k+1]:
            j += 1
            k -= 1
        else:
            break
    
    return (j,k)
'''
        
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        
        A.sort()
        ans = set()
        for i in range(len(A) - 2):
            
            if i > 0  and A[i] == A[i-1]:
                continue
            
            j = i + 1
            k = len(A) - 1
            while j < k:
                if A[i] + A[j] + A[k] == 0:
                    ans.add((A[i],A[j],A[k]))
                    j += 1
                    k -= 1
                elif A[i] + A[j] + A[k] < 0:
                    j += 1
                elif A[i] + A[j] + A[k] > 0:
                    k -= 1
        
        return list(ans)
            

