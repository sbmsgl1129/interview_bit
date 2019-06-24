class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        
        ans = 0
        mod = 10**9 + 7
        
        '''
        for i in range(len(A) - 1):
            for j in range(i+1, len(A)):
               diff_bits = self.count_set_bits(A[i]^A[j])
               
               ## Adding two times as we have to add for both
               ## (A[i],A[j]) and (A[j],A[i])
               ans = (ans + diff_bits) % mod
               ans = (ans + diff_bits) % mod
        
        return ans
        '''
        
        len_A = len(A)
        num_ones = [0]*32
        for num in A:
            i = 0
            while i <= 31:
                if num & (1<<i):
                    num_ones[i] += 1
                i += 1
        
        for num in num_ones:
            ans = (ans + (2*num*(len_A-num)) % mod) % mod
        
        return ans
    '''
    def count_set_bits(self,A):
        
        count = 0
        while A > 0:
            count += 1
            A &= (A - 1)
        
        return count
    '''

