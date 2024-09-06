# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.hasPath(root, targetSum, 0)

    def hasPath(self, root, targetSum, currSum):
        
        if not root:
            return False
        currSum += root.val
        print(currSum)
        if currSum == targetSum and not root.left and not root.right:
            return True
        return  self.hasPath(root.left, targetSum, currSum) or self.hasPath(root.right, targetSum, currSum)        