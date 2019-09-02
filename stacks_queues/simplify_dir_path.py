class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        
        stack = []
        for path in A.split('/'):
            if path == '.' or path == '':
                continue
            elif path == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        
        return '/' + '/'.join(stack)
