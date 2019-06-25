class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        
        closestSum = 0
        difference = float('inf')
        
        A.sort()
        for i in range(len(A) - 2):
            r = B - A[i]
            
            j = i + 1
            k = len(A) - 1
            while j != k - 1:
                if A[j] + A[k] < r:
                    j += 1
                elif A[j] + A[k] > r:
                    k -= 1
                else:
                    break
            
            s = A[i] + A[j] + A[k]
            d = abs(B - s)
            if d < difference:
                difference = d
                closestSum = s
        
        return closestSum
