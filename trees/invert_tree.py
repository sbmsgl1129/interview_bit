# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        
        if not A or (not A.left and not A.right):
            return A
        
        self.invertTree(A.left)
        self.invertTree(A.right)
        
        A.left, A.right = A.right, A.left
        
        return A

