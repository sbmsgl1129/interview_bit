class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        
        '''
        if A <= 0:
            return []
            
        if A == 1:
            return ['()']
        
        ans = set()
        sub_ans = self.generateParenthesis(A-1)
        
        # previous list inside the big one outside
        for l in sub_ans:
            ans.add('(' + l + ')')
        
        # previous list on left of new list
        for l in sub_ans:
            ans.add(l + '()')
        
        # previous list on right of new list
        for l in sub_ans:
            ans.add('()' + l)
        
        ans = list(ans)
        
        return sorted(ans)
        '''  
        
        if A <= 0:
            return []
        
        ans = []
        temp = ''
        num_left = 0
        num_right = 0
        self.generateParenthesisRec(A, ans, temp, num_left, num_right)
        
        return sorted(ans)
        
    def generateParenthesisRec(self, A, ans, temp, num_left, num_right):
        if num_left == A:
            temp += ')'*(A - num_right)
            ans.append(temp)
            return
        
        self.generateParenthesisRec(A, ans, temp + '(', num_left + 1, num_right)
        
        if num_right < num_left:
            self.generateParenthesisRec(A, ans, temp + ')', num_left, num_right + 1)
        
        return
