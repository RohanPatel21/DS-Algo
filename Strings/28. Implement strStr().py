class Solution(object):
    def strStr(self, haystack, needle):
        if needle == '':
            return 0
        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                x = haystack[i + j]
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1

        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
