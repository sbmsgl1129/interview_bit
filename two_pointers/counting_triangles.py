class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        
        A.sort()
        
        mod = 10**9 + 7
        ans = 0
        
        for i in range(len(A) - 2):
            
            k = i + 2
            for j in range(i+1, len(A) - 1):
                while k < len(A) and A[i] + A[j] > A[k]:
                    k += 1
                ans = (ans  + (k - j -1)) % mod
        
        return ans

