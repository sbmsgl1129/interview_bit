class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        
        ans = []
        s_dict = {}
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                s = A[i] + A[j]
                if s in s_dict:
                    temp_ans = s_dict[s].copy()
                    if temp_ans[0] < i and temp_ans[1] != i and temp_ans[1] != j:
                        temp_ans.extend([i,j])
                        if not ans or temp_ans < ans:
                            ans = temp_ans
                else:
                    s_dict[s] = [i,j]
                    
        return ans
