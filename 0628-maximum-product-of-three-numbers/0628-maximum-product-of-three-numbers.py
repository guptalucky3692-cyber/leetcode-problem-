class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        s=nums[-1]*nums[-2]*nums[-3]
        p =nums[0]*nums[1]*nums[-1]
        return max(s,p)
        """
        :type nums: List[int]
        :rtype: int
        """
        