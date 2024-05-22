# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.maxLength = 0  # To store the maximum length of the ZigZag path

    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Start the DFS from the root node in both left and right directions
        self.dfs(root, 0, True)  # True indicates we can move left next
        self.dfs(root, 0, False)  # False indicates we can move right next
        return self.maxLength

    def dfs(self, node, length, isLeft):
        if not node:
            return

        # Update the maximum length found so far
        self.maxLength = max(self.maxLength, length)

        # If we moved to the left previously, we now try to move to the right, and vice versa
        if isLeft:
            self.dfs(node.left, length + 1, False)  # Try to move left
            self.dfs(node.right, 1, True)  # Switch direction to right
        else:
            self.dfs(node.right, length + 1, True)  # Try to move right
            self.dfs(node.left, 1, False)  # Switch direction to left
