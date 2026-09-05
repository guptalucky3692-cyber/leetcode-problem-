class Solution(object):
    def findDisappearedNumbers(self, nums):
        t = [i for i in range(1,len(nums)+1)]
        return list(set(t)-set(nums))
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        