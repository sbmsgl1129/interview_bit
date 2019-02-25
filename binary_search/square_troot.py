class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):

        start = 0
        end   = A
        #last_square = -1 # enum would be better choice

        while start <= end:
            mid = (start + end) // 2
            square_val = mid*mid

            if square_val == A:
                return mid
            
            if square_val > A:
                end = mid - 1
                #last_square = 1
            elif square_val < A:
                start = mid + 1
                #last_square = 0

        return end