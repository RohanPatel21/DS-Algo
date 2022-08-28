class Solution(object):
    def isValid(self, s):
        stack = []
        closeopen = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in closeopen:
                if stack and stack[-1] == closeopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        """
        :type s: str
        :rtype: bool
        """
