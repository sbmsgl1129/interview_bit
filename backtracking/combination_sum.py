class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    
    def combinationSum(self, A, B):
        A.sort()
        
        combination = []
        combinations = set()
        idx = 0
        self.generateAllCombinations(A, B, idx, combination, combinations)
        
        return sorted(list(combinations))

    def generateAllCombinations(self, A, B, idx, combination, combinations):
        
        for i in range(idx, len(A)):
            if A[i] < B:
                combination.append(A[i])
                self.generateAllCombinations(A, B - A[i], i, combination, combinations)
                combination.pop()
            elif A[i] == B:
                combination.append(A[i])
                combinations.add(tuple(combination.copy()))
                combination.pop()
                return
            
        return
