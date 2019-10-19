# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        
        #make the stack
        self.stack = []
        temp = self.root
        while temp != None:
            self.stack.append(temp)
            temp = temp.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if stack else False

    # @return an integer, the next smallest number
    def next(self):
        node = stack.pop()
        if node.right:
            temp = node.right
            self.stack.push(temp)
            while temp
        return node.val
        

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
