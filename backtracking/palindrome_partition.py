'''
for i in range(A):
    if A[:i] is palindrome, 
        then recursive call A[i:] -> list of lists
        for each list in lists:
            add A[:i] and make a new list of lists
            
'''
def palindrome(s):
    if not s:
        return False
    
    if s == s[::-1]:
        return True

class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        
        if not A:
            return [[]]
        
        partitions = []
        for i in range(1, len(A)+1):
            if palindrome(A[:i]):
                sub_partitions = self.partition(A[i:])
                for sub_partition in sub_partitions:
                    partitions.append([A[:i]] + sub_partition)
        
        return partitions

