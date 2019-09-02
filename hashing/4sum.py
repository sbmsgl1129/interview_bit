class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        ans_dict = {}
        ans = []
        
        A.sort()
        #print(A)
        
        for i in range(len(A)):
            for j in  range(i+1, len(A)):
                sum_remain = B - A[i] - A[j]
                
                k = j + 1
                l = len(A) - 1
                while k < l:
                    s = A[k] + A[l]
                    if s == sum_remain:
                        if (A[i],A[j],A[k],A[l]) not in ans_dict:
                            ans_dict[(A[i],A[j],A[k],A[l])] = 1
                            ans.append([A[i],A[j],A[k],A[l]])
                        k += 1
                        l -= 1
                    elif s < sum_remain:
                        k += 1
                    else:
                        l -= 1
        
        return ans
        

