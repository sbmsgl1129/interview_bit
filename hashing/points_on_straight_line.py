from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        
        if not A:
            return 0
        
        ans = 1
        
        '''
        for i in range(len(A)):
            slope_dict = defaultdict(int)
            dup = 1
            for j in range(i+1, len(A)):
                if A[i] == A[j] and B[i] == B[j]:
                   dup += 1
                elif A[i] == A[j]:
                    slope_dict['H'] += 1
                else:
                    slope = 1.0 * (B[j] - B[i]) / (A[j] - A[i])
                    slope_dict[slope] += 1
            
            if slope_dict:
                ans = max(ans, max(slope_dict.values()) + dup)
            else:
                ans = max(ans, dup)
        '''       
        
        slope_dict = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[j] - A[i] == 0:
                    slope = str(A[j]) + '-inf'
                else:
                    slope = 1.0 * (B[j] - B[i]) / (A[j] - A[i]) 
                
                if slope in slope_dict:
                    slope_dict[slope].add((i,A[i],B[i]))
                    slope_dict[slope].add((j,A[j],B[j]))
                else:
                    slope_dict[slope] = set([(i,A[i],B[i]),(j,A[j],B[j])])
        
        for key in slope_dict.keys():
            if len(slope_dict[key]) > ans:
                ans = len(slope_dict[key])
        
        return ans
