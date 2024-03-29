# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        s1 = [root]
        s2 = []
        level = []
        result = []
        while s1 or s2:
            while s1:
                root = s1.pop()
                level.append(root.val)
                if root.left:
                    s2.append(root.left)
                if root.right:
                    s2.append(root.right)
            result.append(level)
            level = []
            while s2:
                root = s2.pop()
                level.append(root.val)
                if root.right:
                    s1.append(root.right)
                if root.left:
                    s1.append(root.left)
            if level != []:
                result.append(level)
                level = []
        return result
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
