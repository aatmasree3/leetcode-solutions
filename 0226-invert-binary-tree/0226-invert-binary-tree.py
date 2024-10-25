# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:  # Use None instead of null
            return None

        left = self.invertTree(root.left)   # Use self.invertTree
        right = self.invertTree(root.right) # Use self.invertTree
        
        temp = root.right
        root.right=root.left
        root.left=temp
        # Recursively invert the left and right subtrees
        
        # Swap the left and right subtrees

        
        return root
