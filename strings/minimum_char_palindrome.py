def isPalindrome(A):
    if A == A[::-1]:
        return True
    else:
        return False

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
    
        str_len = len(A)
        
        for i in range(str_len, 1, -1):
            if A[0] == A[i-1] and isPalindrome(A[0:i]):
                return str_len - i
        
        return str_len - 1
