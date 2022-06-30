class Solution(object):
    def sortedSquares(self, nums):
        l = 0
        r = len(nums) - 1
        res = len(nums) * [0]
        for i in reversed(range(len(nums))):
            if abs(nums[l]) < abs(nums[r]):
                pow = nums[r]
                r -= 1
            else:
                pow = nums[l]
                l += 1
            res[i] = pow * pow
        return res

