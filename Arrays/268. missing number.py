class Solution(object):
    def missingNumber(self, nums):
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
