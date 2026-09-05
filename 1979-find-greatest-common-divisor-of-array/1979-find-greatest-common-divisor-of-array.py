class Solution(object):
    def findGCD(self, nums):
        a,b = max(nums),min(nums)
        while b!=0:
            a,b = b,a%b
        return a

        """
        :type nums: List[int]
        :rtype: int
        """
        