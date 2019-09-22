import math

binomialCoefficients = [[0] * 101 for _ in range(101)]

# Returns value of Binomial Coefficient C(n, k) 
def binomialCoefficient(n, k): 
    global binomialCoefficients
    
    if n < k:
        return 0
    
    if k == 0 or k == n:
        return 1
    
    if binomialCoefficients[n][k] != 0:
        return binomialCoefficients[n][k]
    
    ans = binomialCoefficient(n-1, k-1) + binomialCoefficient(n-1, k)
    binomialCoefficients[n][k] = ans % 1000000007
    
    return binomialCoefficients[n][k]
    '''
    # since C(n, k) = C(n, n - k) 
    if(k > n - k): 
        k = n - k 
    # initialize result 
    res = 1
    # Calculate value of 
    # [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1] 
    for i in range(k): 
        res = (res * (n - i)) 
        res = res / (i + 1) 
    
    return int(res)
    '''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return self.countMaxHeaps(A)
    
    def countMaxHeaps(self, A):
        if A == 1:
            return 1
        
        if A == 2:
            return 1
        
        numLevels = int(math.floor(math.log2(A)))
        
        numElementsLastLevel = A - pow(2, numLevels) + 1
        maxElementsLastLevelHalf = pow(2, numLevels-1)
        
        numElementsLeftSubTree  = pow(2, numLevels-1) - 1 + min(numElementsLastLevel, maxElementsLastLevelHalf)
        numElementsRightSubTree = A - numElementsLeftSubTree - 1
        
        ans = binomialCoefficient(A-1, numElementsLeftSubTree)
        ans = (ans*self.countMaxHeaps(numElementsLeftSubTree)) % 1000000007
        ans = (ans * self.countMaxHeaps(numElementsRightSubTree)) % 1000000007
        
        return ans
