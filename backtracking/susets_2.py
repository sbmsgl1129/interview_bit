class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        
        A.sort()
        subsets = self.recSubsets(A)
        
        subsets_uniq = set()
        for subset in subsets:
            subsets_uniq.add(tuple(subset))
        
        return sorted(list(subsets_uniq))
        
    def recSubsets(self, A):
        if not A:
            return [[]]
        
        subsets = []
        
        subSubsets = self.recSubsets(A[1:])
        for subset in subSubsets:
            subsets.append([A[0]] + subset)
            subsets.append([] + subset)
        
        return subsets
            

