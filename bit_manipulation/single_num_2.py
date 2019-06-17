class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        '''
        ones = 0
        twos = 0
      
        for num in A:
            
            ## Adding to twos if it appeared in ones
            twos |= ones & num
            
            ## Contains elemnets which appears once till now
            ## All double elements will be removed bcoz of XOR
            ## Elements occuring third time will be removed below
            ones ^= num
            
            ## Removing element which is appearing third time
            not_threes = ~(ones & twos)
            ones &= not_threes
            twos &= not_threes
        
        return ones
        '''
        
        # Another way of doing it
        
        # Assuming 32 bit wide integers
        ans = 0
        for i in range(32):
            current_bit = 1 << i
            total = 0
            
            for num in A:
                if num & current_bit:
                    total += 1
            
            # if sum has a remainder (which will be one), set that bit in ans
            # Brilliant way to do that
            if total % 3:
                ans |= current_bit
        
        return ans
