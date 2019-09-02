class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        
        o = ['+', '-', '*', '/']
        stack = []
        for char in A:
            if char == '(' or char in o:
                stack.append(char)
            elif char == ')':
                operator = stack.pop()
                if not stack:
                    return 1
                if operator not in o:
                    return 1
                
                stack.pop()
        
        return 0
