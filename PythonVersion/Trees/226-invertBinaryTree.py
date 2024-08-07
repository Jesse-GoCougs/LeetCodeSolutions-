# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = 
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if root == None:
                return 
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left 

        dfs(root)
        return root