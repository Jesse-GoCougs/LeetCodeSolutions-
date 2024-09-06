# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        visited = []
        self.inOrderHelper(root, visited)
        return visited

    def inOrderHelper(self, root, visited):
        if not root:
            return 
        self.inOrderHelper(root.left, visited)
        visited.append(root.val)
        self.inOrderHelper(root.right, visited)