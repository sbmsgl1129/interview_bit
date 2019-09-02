class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        
        mapping = { '0' : ['0'],
                    '1' : ['1'],
                    '2' : ['a','b','c'],
                    '3' : ['d','e','f'],
                    '4' : ['g','h','i'],
                    '5' : ['j', 'k', 'l'],
                    '6' : ['m','n','o'],
                    '7' : ['p','q','r','s'],
                    '8' : ['t','u','v'],
                    '9' : ['w','x','y','z'] }
        
        return self.letterCombinationRec(A, mapping)
    
    def letterCombinationRec(self, A, mapping):
        
        if len(A) == 1:
            return mapping[A]
        else:
            all_combinations = []
            all_combinations_prev = self.letterCombinationRec(A[1:], mapping)
            for char in mapping[A[0]]:
                for combination in all_combinations_prev:
                    all_combinations.append(char + combination)
                    
            
            return all_combinations
