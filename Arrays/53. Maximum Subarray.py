class Solution(object):
    def maxSubArray(self, nums):
        maxsum = -10000000
        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            if (maxsum < cursum):
                maxsum = cursum
            if cursum < 0:
                cursum = 0
        return maxsum
