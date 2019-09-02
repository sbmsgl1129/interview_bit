from collections import defaultdict

def dict_equal(dictA, dictB):
    
    if len(dictA) != len(dictB):
        return False
    
    for key in dictA:
        if key not in dictB:
            return False
        if dictA[key] != dictB[key]:
            return False
    
    return True

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        
        ans = []
        
        list_hash = defaultdict(int)
        for word in B:
            list_hash[word] += 1
            
        length_of_word = len(B[0])
        
        for i in range(len(A)):
            j = i
            iterations = 0
            words_covered = defaultdict(int)
            while j < len(A) and iterations < len(B):
                
                if A[j:j+length_of_word] not in list_hash:
                    break
                
                words_covered[A[j:j+length_of_word]] += 1
                j = j + length_of_word
                iterations += 1
            
            if iterations == len(B) and dict_equal(list_hash, words_covered):
                ans.append(i)
                
        
        return ans
