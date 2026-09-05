class Solution(object):
    def findNonMinOrMax(self, nums):
        maxt,mint = max(nums),min(nums)
        for n in nums:
            if n!= maxt and n!= mint:
                return n
        return -1

        """
        :type nums: List[int]
        :rtype: int
        """
        