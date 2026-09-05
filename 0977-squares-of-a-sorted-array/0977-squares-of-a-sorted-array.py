class Solution(object):
    def sortedSquares(self, nums):
        n = [num*num for num in nums]
        n.sort()
        return n
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        