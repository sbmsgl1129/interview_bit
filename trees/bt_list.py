# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        self.flattenRec(A)
        
        return A

    def flattenRec(self,A):
        
        if not A.left and not A.right:
            return A
        
        e1 = None
        if A.left:
            e1 = self.flattenRec(A.left)
        
        e2 = None
        if A.right:
            e2 = self.flattenRec(A.right)
        
        end = None
        temp = A.right
        if A.left:
            A.right = A.left
            A.left = None
        
        if temp:
            if e1:
                e1.right = temp
            end = e2
        else:
            end = e1
        
        return end
