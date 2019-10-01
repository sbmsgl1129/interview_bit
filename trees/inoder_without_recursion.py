# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack  = []
        inorder = []
        
        curnode = A
        while True:
            if curnode is not None:
                stack.append(curNode)
                curnode = curnode.left
            elif stack:
                node = stack.pop()
                inorder.append(node.val)
                curnode  = node.right
            else:
                return inorder
