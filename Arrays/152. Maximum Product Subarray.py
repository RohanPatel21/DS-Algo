class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        cur_min, cur_max = 1, 1
        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1
                continue
            tmp = cur_max * n
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            res = max(res, cur_max)
        return res

        """
        :type nums: List[int]
        :rtype: int
        """
