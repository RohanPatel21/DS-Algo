"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        if not root:
            return None
        cur, nxt = root, root.left
        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return root
        """
        :type root: Node
        :rtype: Node
        """
