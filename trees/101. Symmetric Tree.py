# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.equal(root.left, root.right)

    def equal(self, left, right):
        if left and right:
            return left.val == right.val and self.equal(left.left, right.right) and self.equal(left.right, right.left)
        return left == right

        """
        :type root: TreeNode
        :rtype: bool
        """
