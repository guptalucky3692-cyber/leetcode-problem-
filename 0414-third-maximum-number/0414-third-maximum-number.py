class Solution(object):
    def thirdMax(self, nums):
        n = sorted(set(nums),reverse= True)
        if len(n)>=3:
            return n[2]
        else:
            return n[0]

        """
        :type nums: List[int]
        :rtype: int
        """
        