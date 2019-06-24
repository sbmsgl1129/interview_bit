class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        
        num_bits_set = 0
        for i in range(32):
            if A & (1 << i):
                num_bits_set += 1
        
        return num_bits_set
                

