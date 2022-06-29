class Solution(object):
    def searchInsert(self, nums, target):
        high = len(nums) - 1
        low = 0
        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
        return low
