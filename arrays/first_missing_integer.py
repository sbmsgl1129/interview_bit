#https://www.interviewbit.com/problems/first-missing-integer/

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        
        size = len(A)
        max_missing_positive = size + 1
        
        A = [num*max_missing_positive for num in A]
        for num in A:
            actual_num = num // max_missing_positive
            if actual_num >= 1 and actual_num <= size:
                is_previously_added  = A[actual_num -1] % max_missing_positive
                if not is_previously_added:
                    A[actual_num - 1] = A[actual_num - 1] + actual_num
                
        firstMissingPositive = 1
        for num in A:
            if num % max_missing_positive != firstMissingPositive:
                return firstMissingPositive
            
            firstMissingPositive += 1
        
        return firstMissingPositive
