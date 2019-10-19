# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        p1 = self.path(A, B)
        if not p1:
            return -1
        
        p2 = self.path(A, C)
        if not p2:
            return -1
        
        i = 0
        j = 0
        while i < len(p1) and j < len(p2):
            if p1[i] != p2[j]:
                return p1[i-1]
                
            i += 1
            j += 1    
       
        if i == len(p1):
            return p1[i-1]
        
        if j == len(p2):
            return p2[j-1]
        
    def path(self, A, B):
        
        if not A:
            return []
        
        if A.val == B:
            p = []
            p.append(B)
            return p 
        
        left_path = self.path(A.left, B)
        if left_path:
            left_path.insert(0, A.val)
            return left_path
         
        right_path = self.path(A.right, B)
        if right_path:
            right_path.insert(0, A.val)
            return right_path

        return []         
