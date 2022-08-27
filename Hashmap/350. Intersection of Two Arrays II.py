from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        c = Counter(nums1)
        res = []
        for n in nums2:
            if c[n] > 0:
                res.append(n)
                c[n] -= 1
        return res
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
