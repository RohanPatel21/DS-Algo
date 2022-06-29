class Solution(object):
    def containsDuplicate(self, nums):
        ncount = {}
        for n in nums:
            if n in ncount:
                return True
            else:
                ncount[n]=2