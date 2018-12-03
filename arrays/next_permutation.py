#https://www.interviewbit.com/problems/next-permutation/

class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        l = len(A)
        pivot_found = False
        
        for pivot in range(l-2,-1,-1):
            if A[pivot] < A[pivot + 1]:
                pivot_found = True
                break
        
        if pivot_found:
            pivot_val = A[pivot]
            #print pivot_val
            
            A[pivot:] = sorted(A[pivot:])
            idx_next_ele = A.index(pivot_val,pivot) + 1
            next_ele     = A[idx_next_ele]
            
            #print A[pivot:]
            #print idx_next_ele
            #print next_ele
            
            A.pop(idx_next_ele)
            A.insert(pivot, next_ele)
        else:
            A.sort()
            
        return A
