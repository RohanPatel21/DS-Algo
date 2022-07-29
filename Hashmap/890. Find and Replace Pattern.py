class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def get_pattern(s):
            lookup = {}
            output = []
            i = 0
            for c in s:
                if c in lookup:
                    output.append(lookup[c])
                else:
                    i += 1
                    lookup[c] = i
                    output.append(i)
            return (output)

        p = get_pattern(pattern)
        output = []
        for word in words:
            if get_pattern(word) == p:
                output.append(word)
        return output

        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
