# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        
        stack = []
        postorder  = []
        
        curnode = A
        while True:
            if curnode:
                stack.append((curnode,1))
                curnode = curnode.left
            elif stack:
                node = stack.pop()
                if node[1] == 2 or not node[0].right:
                    postorder.append(node[0].val)
                elif node[0].right:
                    curnode = node[0].right
                    stack.append((node[0],2))
            else:
                return postorder

