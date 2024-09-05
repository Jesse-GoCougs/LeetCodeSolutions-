# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        return self.buildString(root)

    def buildString(self,root):
        if not root:
            return ""
        result = str(root.val)
        if root.left:
            result += '(' + self.buildString(root.left) + ')'
        if root.right:
            if not root.left:
                result += "()"
            result +=  '(' + self.buildString(root.right) + ')'
        return result 