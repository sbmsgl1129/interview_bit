from functools import cmp_to_key

def cutsomSort(a, b):
    
    if a == b:
        return 0
    
    modified_a = a + b
    modified_b = b + a
    
    return -1 if modified_a < modified_b else 1

class Solution:
        # @param A : tuple of integers
        # @return a strings
        def largestNumber(self, A):
            if any(A):
                return ''.join(sorted(map(str, A), key=cmp_to_key(cutsomSort), reverse=True))
            else:
                return 0
        
