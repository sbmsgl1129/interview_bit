class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        if not A:
            return [[]]
        
        A.sort()
        sub_subsets = self.subsets(A[:-1])
        #final_subsets = sub_subsets.copy()
        final_subsets = []
        for s in sub_subsets:
            final_subsets.append(s.copy())
        for s in final_subsets:
            s.append(A[-1])
        
        final_subsets.extend(sub_subsets)
        final_subsets.sort()
        
        return final_subsets
            

