class Solution(object):
    def findErrorNums(self, nums):
        n,a,b = len(nums),sum(nums),sum(set(nums))
        t = n*(n+1)//2
        return [a-b,t-b]


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        