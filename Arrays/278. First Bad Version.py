class Solution(object):
    def firstBadVersion(self, n):
        high = n
        low = 1
        res = -1
        while low<=high :
            mid = (low+high)/2
            if isBadVersion(mid):
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res