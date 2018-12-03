#https://www.interviewbit.com/problems/repeat-and-missing-number-array/

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        N = len(A)
        
        sum_actual  = sum([i for i in range(1,N+1)])
        sum_array = sum(A)
        
        square_sum_actual = sum([i*i for i in range(1,N+1)]) 
        square_sum_array  = sum([num*num for num in A])
        
        diff_repeated_missing = sum_array - sum_actual
        sum_repeated_missing  = (square_sum_array - square_sum_actual) / diff_repeated_missing
        
        repeated = (sum_repeated_missing + diff_repeated_missing) / 2
        missing  = sum_repeated_missing - repeated
        
        return [int(repeated), int(missing)]
