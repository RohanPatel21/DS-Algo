class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        lsum = 0
        for i,j in enumerate(nums):
            if lsum == (S-lsum-j):
                return i
            lsum += j
        return -1